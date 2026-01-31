[![探索 AI 代理框架](./images/lesson-2-thumbnail.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(点击上面的图片观看本课程的视频)_

# 探索 AI 代理框架

AI 代理框架是设计用于简化 AI 代理的创建、部署和管理的软件平台。这些框架为开发人员提供预构建的组件、抽象和工具，简化复杂 AI 系统的开发。

这些框架通过为 AI 代理开发中的常见挑战提供标准化方法，帮助开发人员专注于应用程序的独特方面。它们增强了构建 AI 系统的可扩展性、可访问性和效率。

## 介绍

本课程将涵盖：

- 什么是 AI 代理框架，它们使开发人员能够实现什么目标？
- 团队如何使用这些框架快速原型设计、迭代和改进其代理的能力？
- Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>、<a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> 和 <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> 创建的框架和工具有什么区别？
- 我能否直接集成现有的 Azure 生态系统工具，还是需要独立解决方案？
- 什么是 Azure AI Agents 服务，它如何帮助我？

## 学习目标

本课程的目标是帮助您理解：

- AI 代理框架在 AI 开发中的作用。
- 如何利用 AI 代理框架构建智能代理。
- AI 代理框架启用的关键功能。
- AutoGen、Semantic Kernel 和 Azure AI Agent Service 之间的区别。

## 什么是 AI 代理框架，它们使开发人员能够做什么？

传统的 AI 框架可以帮助您将 AI 集成到应用程序中，并通过以下方式使这些应用程序变得更好：

- **个性化**：AI 可以分析用户行为和偏好，提供个性化的推荐、内容和体验。
示例：像 Netflix 这样的流媒体服务使用 AI 根据观看历史推荐电影和节目，增强用户参与度和满意度。
- **自动化和效率**：AI 可以自动化重复任务，简化工作流程，提高运营效率。
示例：客户服务应用程序使用 AI 驱动的聊天机器人处理常见查询，减少响应时间，让人工代理能够处理更复杂的问题。
- **增强用户体验**：AI 可以通过提供语音识别、自然语言处理和预测文本等智能功能来改善整体用户体验。
示例：像 Siri 和 Google Assistant 这样的虚拟助手使用 AI 来理解和响应语音命令，使用户更容易与设备交互。

### 听起来都很棒，那么为什么我们需要 AI 代理框架？

AI 代理框架代表的不仅仅是 AI 框架。它们旨在启用智能代理的创建，这些代理可以与用户、其他代理和环境交互以实现特定目标。这些代理可以表现出自主行为，做出决策，并适应不断变化的条件。让我们看看 AI 代理框架启用的一些关键功能：

- **代理协作与协调**：启用多个 AI 代理的创建，这些代理可以一起工作、通信和协调以解决复杂任务。
- **任务自动化和管理**：提供自动化多步骤工作流程、任务委派和代理之间动态任务管理的机制。
- **上下文理解和适应**：使代理能够理解上下文，适应不断变化的环境，并基于实时信息做出决策。

因此，总而言之，代理允许您做更多事情，将自动化提升到新的水平，创建可以适应环境并从中学习的更智能系统。

## 如何快速原型设计、迭代和改进代理的能力？

这是一个快速发展的领域，但大多数 AI 代理框架都有一些共同点，可以帮助您快速原型设计和迭代，即模块组件、协作工具和实时学习。让我们深入了解这些：

- **使用模块化组件**：AI SDK 提供预构建组件，如 AI 和内存连接器、使用自然语言或代码插件的函数调用、提示模板等。
- **利用协作工具**：设计具有特定角色和任务的代理，使它们能够测试和完善协作工作流程。
- **实时学习**：实现反馈循环，使代理能够从交互中学习并动态调整其行为。

### 使用模块化组件

像 Microsoft Semantic Kernel 和 LangChain 这样的 SDK 提供预构建组件，如 AI 连接器、提示模板和内存管理。

**团队如何使用这些**：团队可以快速组装这些组件以创建功能原型，而无需从头开始，允许快速实验和迭代。

**实际工作原理**：您可以使用预构建的解析器从用户输入中提取信息，使用内存模块存储和检索数据，以及使用提示生成器与用户交互，而无需从头构建这些组件。

**示例代码**。让我们看一下如何使用带有自动函数调用的 Semantic Kernel Python 和 .Net 中的预构建 AI 连接器，让模型响应用户输入的示例：

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

从这个例子中，您可以看到如何利用预构建的解析器从用户输入中提取关键信息，例如航班预订请求的出发地、目的地和日期。这种模块化方法允许您专注于高级逻辑。

### 利用协作工具

像 CrewAI、Microsoft AutoGen 和 Semantic Kernel 这样的框架促进了多个可以一起工作的代理的创建。

**团队如何使用这些**：团队可以设计具有特定角色和任务的代理，使它们能够测试和完善协作工作流程，提高整体系统效率。

**实际工作原理**：您可以创建一个代理团队，其中每个代理都有专门的功能，例如数据检索、分析或决策制定。这些代理可以通信和共享信息以实现共同目标，例如回答用户查询或完成任务。

**示例代码（AutoGen）**：

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

在前面的代码中，您可以看到如何创建一个涉及多个代理一起分析数据的任务。每个代理执行特定功能，任务通过协调代理来实现预期结果。通过创建具有专门角色的专用代理，您可以提高任务效率和性能。

### 实时学习

高级框架提供实时上下文理解和适应能力。

**团队如何使用这些**：团队可以实现反馈循环，使代理能够从交互中学习并动态调整其行为，从而持续改进和完善能力。

**实际工作原理**：代理可以分析用户反馈、环境数据和任务结果，以更新其知识库，调整决策算法，并随着时间的推移提高性能。这种迭代学习过程使代理能够适应不断变化的条件和用户偏好，增强整体系统有效性。

## AutoGen、Semantic Kernel 和 Azure AI Agent Service 框架之间有什么区别？

有很多方法可以比较这些框架，但让我们看看它们在设计、功能和目标用例方面的一些关键区别：

## AutoGen

AutoGen 是由 Microsoft Research 的 AI Frontiers Lab 开发的开源框架。它专注于事件驱动的分布式*代理*应用程序，支持多个 LLM 和 SLM、工具和高级多代理设计模式。

AutoGen 围绕代理的核心概念构建，代理是能够感知环境、做出决策并采取行动以实现特定目标的自主实体。代理通过异步消息进行通信，使它们能够独立并行工作，增强系统可扩展性和响应性。

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">代理基于 actor 模型</a>。根据 Wikipedia，actor 是*并发计算的基本构建块。响应接收到的消息，actor 可以：做出本地决策，创建更多 actor，发送更多消息，并确定如何响应接收到的下一条消息*。

**用例**：自动化代码生成、数据分析任务，以及为规划和研究功能构建自定义代理。

以下是 AutoGen 的一些重要核心概念：

- **代理**。代理是一个软件实体，它：
  - **通过消息通信**，这些消息可以是同步的或异步的。
  - **维护自己的状态**，可以通过传入消息修改。
  - **执行操作**以响应接收到的消息或其状态的变化。这些操作可能会修改代理的状态并产生外部效果，例如更新消息日志、发送新消息、执行代码或进行 API 调用。
    
  这里有一个简短的代码片段，您可以在其中创建自己的具有聊天功能的代理：

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    在前面的代码中，`MyAgent` 已创建并继承自 `RoutedAgent`。它有一个消息处理程序，打印消息内容，然后使用 `AssistantAgent` 委托发送响应。特别注意我们如何将 `self._delegate` 分配给 `AssistantAgent` 的实例，这是一个可以处理聊天完成的预构建代理。


    让我们让 AutoGen 了解这个代理类型并接下来启动程序：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    在前面的代码中，代理向运行时注册，然后向代理发送消息，导致以下输出：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **多代理**。AutoGen 支持创建多个可以一起工作以实现复杂任务的代理。代理可以通信、共享信息和协调他们的行动以更有效地解决问题。要创建多代理系统，您可以定义具有专门功能和角色的不同类型的代理，例如数据检索、分析、决策制定和用户交互。让我们看看这样的创建是什么样子，以便我们了解它：

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    在前面的代码中，我们有一个向运行时注册的 `GroupChatManager`。这个管理器负责协调不同类型代理之间的交互，例如作家、插图画家、编辑和用户。

- **代理运行时**。该框架提供运行时环境，启用代理之间的通信，管理它们的身份和生命周期，并执行安全和隐私边界。这意味着您可以在安全和受控的环境中运行代理，确保它们可以安全有效地交互。有两种运行时值得关注：
  - **独立运行时**。这是单进程应用程序的不错选择，其中所有代理都在同一编程语言中实现并在同一进程中运行。以下是它如何工作的说明：
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">独立运行时</a>   
应用程序堆栈

    *代理通过运行时通过消息进行通信，运行时管理代理的生命周期*

  - **分布式代理运行时**，适用于多进程应用程序，其中代理可能在不同的编程语言中实现并在不同的机器上运行。以下是它如何工作的说明：
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">分布式运行时</a>

## Semantic Kernel + 代理框架

Semantic Kernel 是一个企业级 AI 编排 SDK。它由 AI 和内存连接器以及代理框架组成。

让我们首先介绍一些核心组件：

- **AI 连接器**：这是与外部 AI 服务和数据源的接口，可在 Python 和 C# 中使用。

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    这里有一个简单的例子，说明如何创建一个内核并添加聊天完成服务。Semantic Kernel 创建与外部 AI 服务的连接，在这种情况下是 Azure OpenAI Chat Completion。

- **插件**：这些封装应用程序可以使用的函数。既有现成的插件，也有可以创建的自定义插件。一个相关的概念是"提示函数"。不是为函数调用提供自然语言提示，而是向模型广播某些函数。基于当前聊天上下文，模型可能会选择调用这些函数之一来完成请求或查询。以下是一个例子：

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    在这里，您首先有一个模板提示 `skPrompt`，为用户输入文本留出空间 `$userInput`。然后创建内核函数 `SummarizeText`，然后将其导入到内核中，插件名称为 `SemanticFunctions`。注意函数名称，它帮助 Semantic Kernel 理解函数的作用以及何时应该调用它。

- **原生函数**：还有框架可以直接调用以执行任务的原生函数。以下是从文件中检索内容的此类函数的示例：

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **内存**：为 AI 应用程序抽象和简化上下文管理。内存的概念是 LLM 应该知道的事情。您可以将此信息存储在向量存储中，最终成为内存数据库或向量数据库等。以下是一个非常简化的场景示例，其中*事实*被添加到内存中：

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";" )[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";" )[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    这些事实然后存储在内存集合 `SummarizedAzureDocs` 中。这是一个非常简化的例子，但您可以看到如何将信息存储在内存中以供 LLM 使用。

那么，这就是 Semantic Kernel 框架的基础，那么代理框架呢？

## Azure AI 代理服务

Azure AI 代理服务是最近的添加，在 Microsoft Ignite 2024 上引入。它允许开发和部署具有更灵活模型的 AI 代理，例如直接调用开源 LLM 如 Llama 3、Mistral 和 Cohere。

Azure AI 代理服务提供更强大的企业安全机制和数据存储方法，使其适合企业应用程序。

它与 AutoGen 和 Semantic Kernel 等多代理编排框架开箱即用。

此服务目前处于公共预览状态，支持 Python 和 C# 构建代理。

使用 Semantic Kernel Python，我们可以创建带有用户定义插件的 Azure AI 代理：

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### 核心概念

Azure AI 代理服务具有以下核心概念：

- **代理**。Azure AI 代理服务与 Azure AI Foundry 集成。在 AI Foundry 中，AI 代理充当"智能"微服务，可用于回答问题（RAG）、执行操作或完全自动化工作流程。它通过将生成式 AI 模型的力量与允许它访问和与现实世界数据源交互的工具相结合来实现这一点。以下是代理的示例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在这个例子中，创建了一个代理，模型为 `gpt-4o-mini`，名称为 `my-agent`，指令为 `You are helpful agent`。该代理配备了工具和资源来执行代码解释任务。

- **线程和消息**。线程是另一个重要概念。它表示代理和用户之间的对话或交互。线程可用于跟踪对话进度，存储上下文信息，管理交互状态。以下是线程的示例：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    在前面的代码中，创建了一个线程。此后，向线程发送消息。通过调用 `create_and_process_run`，请求代理在线程上执行工作。最后，获取并记录消息以查看代理的响应。消息指示用户和代理之间的对话进度。同样重要的是要理解，消息可以是不同类型的，例如文本、图像或文件，即代理的工作导致例如图像或文本响应。作为开发人员，您可以使用此信息进一步处理响应或将其呈现给用户。

- **与其他 AI 框架集成**。Azure AI 代理服务可以与 AutoGen 和 Semantic Kernel 等其他框架交互，这意味着您可以在这些框架之一中构建应用程序的一部分，例如使用代理服务作为编排器，或者您可以在代理服务中构建所有内容。

**用例**：Azure AI 代理服务专为需要安全、可扩展和灵活的 AI 代理部署的企业应用程序而设计。

## 这些框架之间有什么区别？
 
确实，这些框架之间有很多重叠，但它们在设计、功能和目标用例方面存在一些关键差异：
 
- **AutoGen**：是一个实验框架，专注于多代理系统的前沿研究。它是实验和原型设计复杂多代理系统的最佳场所。
- **Semantic Kernel**：是一个生产就绪的代理库，用于构建企业代理应用程序。专注于事件驱动的分布式代理应用程序，支持多个 LLM 和 SLM、工具以及单/多代理设计模式。
- **Azure AI 代理服务**：是 Azure Foundry 中用于代理的平台和部署服务。它提供与 Azure Found 支持的服务的连接，如 Azure OpenAI、Azure AI Search、Bing Search 和代码执行。
 
仍然不确定选择哪一个？

### 用例
 
让我们通过一些常见用例来帮助您：
 
> Q: 我正在实验、学习和构建概念验证代理应用程序，我希望能够快速构建和实验
>


> A: AutoGen 对于这种情况是一个不错的选择，因为它专注于事件驱动的分布式代理应用程序，并支持高级多代理设计模式。

> Q: 什么使 AutoGen 比 Semantic Kernel 和 Azure AI 代理服务更适合这种用例？
>
> A: AutoGen 专为事件驱动的分布式代理应用程序而设计，使其非常适合自动化代码生成和数据分析任务。它提供了有效构建复杂多代理系统所需的工具和功能。

> Q: 听起来 Azure AI 代理服务也可以在这里工作，它有代码生成和更多的工具？

>
> A: 是的，Azure AI 代理服务是一个用于代理的平台服务，添加了多个模型、Azure AI Search、Bing Search 和 Azure Functions 的内置功能。它使您可以轻松地在 Foundry 门户中构建代理并大规模部署它们。
 
> Q: 我仍然很困惑，只给我一个选择
>
> A: 一个很好的选择是首先在 Semantic Kernel 中构建您的应用程序，然后使用 Azure AI 代理服务部署您的代理。这种方法允许您轻松持久化您的代理，同时利用 Semantic Kernel 中构建多代理系统的能力。此外，Semantic Kernel 在 AutoGen 中有一个连接器，使其易于一起使用这两个框架。
 
让我们在表格中总结关键差异：

| 框架 | 重点 | 核心概念 | 用例 |
| --- | --- | --- | --- |
| AutoGen | 事件驱动的分布式代理应用程序 | 代理、角色、函数、数据 | 代码生成、数据分析任务 |
| Semantic Kernel | 理解和生成类人文本内容 | 代理、模块化组件、协作 | 自然语言理解、内容生成 |
| Azure AI 代理服务 | 灵活模型、企业安全、代码生成、工具调用 | 模块化、协作、流程编排 | 安全、可扩展、灵活的 AI 代理部署 |

这些框架的理想用例是什么？

## 我能否直接集成现有的 Azure 生态系统工具，还是需要独立解决方案？

答案是肯定的，您可以直接将现有的 Azure 生态系统工具与 Azure AI 代理服务集成，尤其是因为它已构建为与其他 Azure 服务无缝协作。例如，您可以集成 Bing、Azure AI Search 和 Azure Functions。它还与 Azure AI Foundry 深度集成。

对于 AutoGen 和 Semantic Kernel，您也可以与 Azure 服务集成，但可能需要从代码中调用 Azure 服务。另一种集成方式是使用 Azure SDK 从您的代理中与 Azure 服务交互。此外，如前所述，您可以使用 Azure AI 代理服务作为在 AutoGen 或 Semantic Kernel 中构建的代理的编排器，这将提供对 Azure 生态系统的轻松访问。

## 示例代码

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## 对 AI 代理框架还有更多问题？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者见面，参加办公时间并获得 AI 代理问题的答案。

## 参考资料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution</a>

## 上一课

[AI 代理入门与代理用例](../01-intro-to-ai-agents/README.md)

## 下一课

[理解代理设计模式](../03-agentic-design-patterns/README.md)
