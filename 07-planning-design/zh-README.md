[![Planning Design Pattern](./images/lesson-7-thumbnail.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(点击上面的图片观看本课程的视频)_

# 规划设计

## 介绍

本课程将涵盖以下内容：

* 定义明确的整体目标并将复杂任务分解为可管理的任务。
* 利用结构化输出获得更可靠、更易于机器读取的响应。
* 应用事件驱动方法处理动态任务和意外输入。

## 学习目标

完成本课程后，您将了解：

* 为 AI 代理识别并设定整体目标，确保其明确知道需要实现什么。
* 将复杂任务分解为可管理的子任务，并将它们组织成逻辑序列。
* 为代理配备合适的工具（例如搜索工具或数据分析工具），决定何时以及如何使用它们，并处理出现的意外情况。
* 评估子任务结果，衡量性能，并迭代行动以改进最终输出。

## 定义整体目标并分解任务

![定义目标和任务](./images/defining-goals-tasks.png)

大多数现实世界的任务太复杂，无法一步完成。AI 代理需要一个简洁的目标来指导其规划和行动。例如，考虑这个目标：

    "生成一个 3 天的旅行行程。"

虽然陈述简单，但仍需要细化。目标越明确，代理（以及任何人类协作者）就越能专注于实现正确的结果，例如创建包含航班选项、酒店推荐和活动建议的综合行程。

### 任务分解

大型或复杂的任务在拆分为更小、面向目标的子任务时会变得更易于管理。
对于旅行行程示例，您可以将目标分解为：

* 航班预订
* 酒店预订
* 汽车租赁
* 个性化

然后，每个子任务可以由专门的代理或流程处理。一个代理可能专门搜索最佳航班优惠，另一个专注于酒店预订，依此类推。然后，一个协调或"下游"代理可以将这些结果编译成一个面向最终用户的连贯行程。

这种模块化方法还允许进行增量增强。例如，您可以添加专门用于食物推荐或当地活动建议的代理，并随着时间的推移完善行程。

### 结构化输出

大型语言模型（LLM）可以生成结构化输出（例如 JSON），更易于下游代理或服务解析和处理。这在多代理上下文中特别有用，在这种情况下，我们可以在收到规划输出后执行这些任务。请参考这个 <a href="https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html" target="_blank">博客文章</a> 了解快速概述。

以下 Python 代码片段演示了一个简单的规划代理如何将目标分解为子任务并生成结构化计划：

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
                      Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### 具有多代理编排的规划代理

在此示例中，语义路由器代理接收用户请求（例如，"我需要为我的旅行制定酒店计划。"）。

然后，规划器：

* 接收酒店计划：规划器接收用户的消息，并基于系统提示（包括可用代理详细信息）生成结构化旅行计划。
* 列出代理及其工具：代理注册表保存代理列表（例如，用于航班、酒店、汽车租赁和活动）以及它们提供的功能或工具。
* 将计划路由到相应的代理：根据子任务的数量，规划器要么将消息直接发送给专用代理（对于单任务场景），要么通过群聊管理器协调多代理协作。
* 总结结果：最后，规划器总结生成的计划以确保清晰。
以下 Python 代码示例说明了这些步骤：

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

以下是前面代码的输出，您可以使用此结构化输出来路由到 `assigned_agent` 并向最终用户总结旅行计划。

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

包含前面代码示例的笔记本可在此处 [07-autogen.ipynb](07-autogen.ipynb) 获取。

### 迭代规划

有些任务需要来回或重新规划，其中一个子任务的结果会影响下一个。例如，如果代理在预订航班时发现意外的数据格式，它可能需要在继续进行酒店预订之前调整策略。

此外，用户反馈（例如，人类决定他们更喜欢早班航班）可以触发部分重新规划。这种动态、迭代的方法确保最终解决方案符合现实世界的约束和不断变化的用户偏好。

例如示例代码

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

有关更全面的规划，请查看 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">博客文章</a> 以解决复杂任务。

## 总结

在本文中，我们研究了如何创建一个可以动态选择已定义可用代理的规划器示例。规划器的输出分解任务并分配代理以便执行。假设代理可以访问执行任务所需的函数/工具。除了代理之外，您还可以包括其他模式，如反射、总结器和轮询聊天，以进一步自定义。

## 其他资源

AutoGen Magentic One - 一个用于解决复杂任务的通用多代理系统，在多个具有挑战性的代理基准测试中取得了令人印象深刻的结果。参考：<a href="https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one" target="_blank">autogen-magentic-one</a>。在此实现中，协调器创建特定于任务的计划并将这些任务委托给可用的代理。除了规划之外，协调器还采用跟踪机制来监控任务的进展并根据需要重新规划。

### 对规划设计模式还有更多问题？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者会面，参加办公时间并获得 AI 代理问题的答案。

## 上一课

[构建可信的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一课

[多代理设计模式](../08-multi-agent/README.md)