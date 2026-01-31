[![How to Design Good AI Agents](./images/lesson-4-thumbnail.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(点击上方图片观看本课视频)_

# 工具使用设计模式

工具很有趣，因为它们允许 AI 代理拥有更广泛的能力。通过添加工具，代理不再局限于有限的操作集，而是可以执行各种操作。在本章中，我们将探讨工具使用设计模式，该模式描述了 AI 代理如何使用特定工具来实现其目标。

## 介绍

在本课程中，我们希望回答以下问题：

- 什么是工具使用设计模式？
- 它可以应用于哪些用例？
- 实现该设计模式需要哪些元素/构建块？
- 使用工具使用设计模式构建可信赖的 AI 代理有哪些特殊考虑？

## 学习目标

完成本课程后，您将能够：

- 定义工具使用设计模式及其目的。
- 识别工具使用设计模式适用的用例。
- 理解实现该设计模式所需的关键元素。
- 认识到使用此设计模式确保 AI 代理可信赖性的考虑因素。

## 什么是工具使用设计模式？

**工具使用设计模式** 专注于赋予 LLM 与外部工具交互以实现特定目标的能力。工具是可以由代理执行以执行操作的代码。工具可以是简单的函数，如计算器，也可以是对第三方服务的 API 调用，如股票价格查询或天气预报。在 AI 代理的上下文中，工具被设计为由代理响应 **模型生成的函数调用** 来执行。

## 它可以应用于哪些用例？

AI 代理可以利用工具完成复杂任务、检索信息或做出决策。工具使用设计模式通常用于需要与外部系统（如数据库、Web 服务或代码解释器）动态交互的场景。这种能力对于许多不同的用例都很有用，包括：

- **动态信息检索**：代理可以查询外部 API 或数据库以获取最新数据（例如，查询 SQLite 数据库进行数据分析，获取股票价格或天气信息）。
- **代码执行和解释**：代理可以执行代码或脚本来解决数学问题、生成报告或进行模拟。
- **工作流自动化**：通过集成任务调度器、电子邮件服务或数据管道等工具来自动化重复或多步骤的工作流。
- **客户支持**：代理可以与 CRM 系统、票务平台或知识库交互以解决用户查询。
- **内容生成和编辑**：代理可以利用语法检查器、文本摘要器或内容安全评估器等工具来协助内容创建任务。

## 实现工具使用设计模式需要哪些元素/构建块？

这些构建块使 AI 代理能够执行各种任务。让我们看看实现工具使用设计模式所需的关键元素：

- **函数/工具模式**：可用工具的详细定义，包括函数名称、目的、必需参数和预期输出。这些模式使 LLM 能够了解可用的工具以及如何构建有效的请求。

- **函数执行逻辑**：根据用户的意图和对话上下文，控制工具如何以及何时被调用。这可能包括规划模块、路由机制或条件流程，这些流程动态确定工具的使用。

- **消息处理系统**：管理用户输入、LLM 响应、工具调用和工具输出之间的对话流程的组件。

- **工具集成框架**：将代理连接到各种工具的基础设施，无论是简单的函数还是复杂的外部服务。

- **错误处理和验证**：处理工具执行失败、验证参数和管理意外响应的机制。

- **状态管理**：跟踪对话上下文、以前的工具交互和持久数据，以确保多轮交互的一致性。

接下来，让我们更详细地了解函数/工具调用。
 
### 函数/工具调用

函数调用是我们使大型语言模型 (LLM) 能够与工具交互的主要方式。您经常会看到 "函数" 和 "工具" 互换使用，因为 "函数"（可重用代码块）是代理用来执行任务的 "工具"。为了使函数的代码被调用，LLM 必须将用户的请求与函数描述进行比较。为此，包含所有可用函数描述的模式被发送到 LLM。然后，LLM 选择最适合任务的函数并返回其名称和参数。所选函数被调用，其响应被发送回 LLM，LLM 使用这些信息来响应用户的请求。

对于开发人员来说，要实现代理的函数调用，您需要：

1. 支持函数调用的 LLM 模型
2. 包含函数描述的模式
3. 每个描述的函数的代码

让我们使用获取城市当前时间的示例来说明：

1. **初始化支持函数调用的 LLM**：

    并非所有模型都支持函数调用，因此检查您使用的 LLM 是否支持非常重要。     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支持函数调用。我们可以通过初始化 Azure OpenAI 客户端开始。 

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **创建函数模式**：

    接下来，我们将定义一个 JSON 模式，其中包含函数名称、函数功能描述以及函数参数的名称和描述。
    然后，我们将这个模式与用户请求（查找旧金山的时间）一起传递给之前创建的客户端。需要注意的是，返回的是 **工具调用**，**不是** 问题的最终答案。如前所述，LLM 返回它为任务选择的函数名称以及将传递给它的参数。

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **执行任务所需的函数代码**：

    现在 LLM 已经选择了需要运行的函数，需要实现并执行执行任务的代码。
    我们可以用 Python 实现获取当前时间的代码。我们还需要编写代码来从 response_message 中提取名称和参数以获得最终结果。

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

函数调用是大多数（如果不是全部）代理工具使用设计的核心，但是从头实现它有时可能具有挑战性。
正如我们在 [第 2 课](../02-explore-agentic-frameworks/) 中了解到的，代理框架为我们提供了预构建的构建块来实现工具使用。
 
## 使用代理框架的工具使用示例

以下是如何使用不同的代理框架实现工具使用设计模式的一些示例：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> 是一个开源 AI 框架，适用于使用大型语言模型 (LLM) 的 .NET、Python 和 Java 开发人员。它通过一个称为 <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a> 的过程，自动向模型描述您的函数及其参数，从而简化了使用函数调用的过程。它还处理模型和代码之间的来回通信。使用 Semantic Kernel 等代理框架的另一个优点是，它允许您访问预构建的工具，如 <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">文件搜索</a> 和 <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">代码解释器</a>。

下图说明了 Semantic Kernel 的函数调用过程：

![函数调用](./images/functioncalling-diagram.png)

在 Semantic Kernel 中，函数/工具被称为 <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">插件</a>。我们可以通过将之前看到的 `get_current_time` 函数转换为包含该函数的类来将其转换为插件。我们还可以导入 `kernel_function` 装饰器，它接收函数的描述。然后，当您使用 GetCurrentTimePlugin 创建内核时，内核会自动序列化函数及其参数，在过程中创建要发送给 LLM 的模式。

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是一个较新的代理框架，旨在使开发人员能够安全地构建、部署和扩展高质量、可扩展的 AI 代理，而无需管理底层的计算和存储资源。它对于企业应用程序特别有用，因为它是一个完全托管的服务，具有企业级安全性。

与直接使用 LLM API 开发相比，Azure AI Agent Service 提供了一些优势，包括：

- 自动工具调用 – 无需解析工具调用、调用工具并处理响应；所有这些现在都在服务器端完成
- 安全管理数据 – 您可以依靠线程存储所需的所有信息，而不是管理自己的对话状态
- 开箱即用的工具 – 可用于与数据源交互的工具，如 Bing、Azure AI Search 和 Azure Functions。

Azure AI Agent Service 中可用的工具可分为两类：

1. 知识工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">使用 Bing 搜索进行基础</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">文件搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. 操作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函数调用</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">代码解释器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定义的工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service 允许我们将这些工具作为 `toolset` 一起使用。它还利用 `threads` 来跟踪特定对话的消息历史。

假设您是一家名为 Contoso 的公司的销售代理。您想要开发一个可以回答有关销售数据问题的对话代理。

下图说明了如何使用 Azure AI Agent Service 分析销售数据：

![Agentic Service In Action](./images/agent-service-in-action.jpg)

要使用服务中的任何这些工具，我们可以创建一个客户端并定义一个工具或工具集。为了实际实现这一点，我们可以使用以下 Python 代码。LLM 将能够查看工具集并决定是使用用户创建的函数 `fetch_sales_data_using_sqlite_query` 还是使用预构建的代码解释器，具体取决于用户请求。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize toolset
toolset = ToolSet()

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用设计模式构建可信赖的 AI 代理有哪些特殊考虑？

LLM 动态生成的 SQL 的一个常见关注点是安全性，特别是 SQL 注入或恶意操作（如删除或篡改数据库）的风险。虽然这些担忧是合理的，但可以通过正确配置数据库访问权限来有效缓解。对于大多数数据库，这涉及将数据库配置为只读。对于 PostgreSQL 或 Azure SQL 等数据库服务，应用程序应被分配只读（SELECT）角色。

在安全环境中运行应用程序进一步增强了保护。在企业场景中，数据通常从运营系统中提取并转换到具有用户友好架构的只读数据库或数据仓库中。这种方法确保数据是安全的，针对性能和可访问性进行了优化，并且应用程序具有受限的只读访问权限。

## 示例代码

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 对工具使用设计模式还有更多问题？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) 与其他学习者见面，参加办公时间并获得 AI 代理问题的答案。

## 其他资源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## 上一课

[理解代理设计模式](../03-agentic-design-patterns/README.md)

## 下一课

[代理 RAG](../05-agentic-rag/README.md)