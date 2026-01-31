# 探索 Microsoft Agent Framework

![Agent Framework](./images/lesson-14-thumbnail.png)

### 简介

本课程将涵盖：

- 理解 Microsoft Agent Framework：关键特性和价值
- 探索 Microsoft Agent Framework 的关键概念
- 比较 MAF 与 Semantic Kernel 和 AutoGen：迁移指南

## 学习目标

完成本课程后，您将了解如何：

- 使用 Microsoft Agent Framework 构建生产就绪的 AI 代理
- 将 Microsoft Agent Framework 的核心特性应用到您的代理用例中
- 迁移和集成现有的代理框架和工具

## 代码示例

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 的代码示例可以在本仓库的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 文件中找到。

## 理解 Microsoft Agent Framework

![Framework Intro](./images/framework-intro.png)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 建立在 Semantic Kernel 和 AutoGen 的经验和学习基础之上。它提供了灵活性，可以解决生产和研究环境中看到的各种代理用例，包括：

- **顺序代理编排** - 在需要逐步工作流程的场景中。
- **并发编排** - 在代理需要同时完成任务的场景中。
- **群聊编排** - 在代理可以共同协作完成一个任务的场景中。
- **交接编排** - 在代理在子任务完成时相互交接任务的场景中。
- **磁编排** - 在管理代理创建和修改任务列表并处理子代理协调以完成任务的场景中。

为了在生产中交付 AI 代理，MAF 还包括以下功能：

- **可观测性** - 通过使用 OpenTelemetry，AI 代理的每一个动作，包括工具调用、编排步骤、推理流程和通过 Azure AI Foundry 仪表板的性能监控。
- **安全性** - 通过在 Azure AI Foundry 上本地托管代理，包括基于角色的访问、私有数据处理和内置内容安全等安全控制。
- **持久性** - 代理线程和工作流可以暂停、恢复和从错误中恢复，从而实现更长时间运行的流程。
- **控制** - 支持人工参与的工作流程，其中任务被标记为需要人工批准。

Microsoft Agent Framework 还注重互操作性：

- **云无关** - 代理可以在容器、本地和多个不同的云中运行。
- **提供商无关** - 可以通过您首选的 SDK（包括 Azure OpenAI 和 OpenAI）创建代理。
- **集成开放标准** - 代理可以利用 Agent-to-Agent (A2A) 和模型上下文协议 (MCP) 等协议来发现和使用其他代理和工具。
- **插件和连接器** - 可以连接到数据和内存服务，如 Microsoft Fabric、SharePoint、Pinecone 和 Qdrant。

让我们看看这些功能如何应用于 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的关键概念

### 代理

![Agent Framework](./images/agent-components.png)

**创建代理**

创建代理是通过定义推理服务（LLM 提供商）、AI 代理要遵循的一组指令以及分配的 `name` 来完成的：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上面使用的是 `Azure OpenAI`，但也可以使用各种服务创建代理，包括 `Azure AI Foundry Agent Service`：

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`、`ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 协议的远程代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**运行代理**

代理使用 `.run` 或 `.run_stream` 方法运行，分别用于非流式或流式响应。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每个代理运行还可以有选项来自定义参数，例如代理使用的 `max_tokens`、代理能够调用的 `tools`，甚至代理使用的 `model` 本身。

这在需要特定模型或工具来完成用户任务的情况下很有用。

**工具**

工具可以在定义代理时定义：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# When creating a ChatAgent directly 

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在运行代理时定义：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tool provided for this run only )
```

**代理线程**

代理线程用于处理多轮对话。线程可以通过以下方式创建：

- 使用 `get_new_thread()`，使线程能够随时间保存
- 运行代理时自动创建线程，且线程仅在当前运行期间存在。

创建线程的代码如下：

```python
# Create a new thread. 
thread = agent.get_new_thread() # Run the agent with the thread. 
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

然后，您可以序列化线程以存储供以后使用：

```python
# Create a new thread. 
thread = agent.get_new_thread() 

# Run the agent with the thread. 

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialize the thread for storage. 

serialized_thread = await thread.serialize() 

# Deserialize the thread state after loading from storage. 

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**代理中间件**

代理与工具和 LLM 交互以完成用户的任务。在某些场景中，我们希望在这些交互之间执行或跟踪。代理中间件使我们能够通过以下方式做到这一点：

*函数中间件*

这种中间件允许我们在代理和它将调用的函数/工具之间执行操作。例如，当您可能想要对函数调用进行一些日志记录时，就会使用这种中间件。

在下面的代码中，`next` 定义是否应该调用下一个中间件或实际函数。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-processing: Log before function execution
    print(f"[Function] Calling {context.function.name}")

    # Continue to next middleware or function execution
    await next(context)

    # Post-processing: Log after function execution
    print(f"[Function] {context.function.name} completed")
```

*聊天中间件*

这种中间件允许我们在代理和 LLM 之间的请求之间执行或记录操作。

这包含重要信息，例如发送到 AI 服务的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-processing: Log before AI call
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continue to next middleware or AI service
    await next(context)

    # Post-processing: Log after AI response
    print("[Chat] AI response received")

```

**代理内存**

如 `Agentic Memory` 课程所述，内存是使代理能够在不同上下文中运行的重要元素。MAF 提供了几种不同类型的内存：

*内存存储*

这是在应用程序运行时存储在线程中的内存。

```python
# Create a new thread. 
thread = agent.get_new_thread() # Run the agent with the thread. 
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*持久消息*

此内存用于在不同会话之间存储对话历史记录。它使用 `chat_message_store_factory` 定义：

```python
from agent_framework import ChatMessageStore

# Create a custom message store
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*动态内存*

此内存在代理运行前添加到上下文中。这些内存可以存储在外部服务中，如 mem0：

```python
from agent_framework.mem0 import Mem0Provider

# Using Mem0 for advanced memory capabilities
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**代理可观测性**

可观测性对于构建可靠且可维护的代理系统非常重要。MAF 集成了 OpenTelemetry，提供跟踪和度量，以实现更好的可观测性。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # do something
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 工作流

MAF 提供了工作流，这些工作流是完成任务的预定义步骤，并将 AI 代理作为这些步骤中的组件。

工作流由不同的组件组成，允许更好的控制流。工作流还支持 **多代理编排** 和 **检查点** 以保存工作流状态。

工作流的核心组件是：

**执行器**

执行器接收输入消息，执行分配的任务，然后生成输出消息。这使工作流朝着完成更大的任务前进。执行器可以是 AI 代理或自定义逻辑。

**边**

边用于定义工作流中消息的流动。这些可以是：

*直接边* - 执行器之间的简单一对一连接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*条件边* - 在满足某些条件后激活。例如，当酒店房间不可用时，执行器可以建议其他选项。

*开关案例边* - 根据定义的条件将消息路由到不同的执行器。例如，如果旅行客户有优先访问权，他们的任务将通过另一个工作流处理。

*扇出边* - 将一条消息发送到多个目标。

*扇入边* - 收集来自不同执行器的多条消息并发送到一个目标。

**事件**

为了提供对工作流更好的可观测性，MAF 为执行提供了内置事件，包括：

- `WorkflowStartedEvent` - 工作流执行开始
- `WorkflowOutputEvent` - 工作流产生输出
- `WorkflowErrorEvent` - 工作流遇到错误
- `ExecutorInvokeEvent` - 执行器开始处理
- `ExecutorCompleteEvent` - 执行器完成处理
- `RequestInfoEvent` - 发出请求

## 从其他框架迁移（Semantic Kernel 和 AutoGen）

### MAF 与 Semantic Kernel 之间的差异

**简化的代理创建**

Semantic Kernel 依赖于为每个代理创建 Kernel 实例。MAF 使用更简化的方法，通过使用主要提供商的扩展。

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at reccomending trips to customers based on their preferences.", name="TripRecommender" )
```

**代理线程创建**

Semantic Kernel 要求手动创建线程。在 MAF 中，代理直接分配线程。

```python
thread = agent.get_new_thread() # Run the agent with the thread. 
```

**工具注册**

在 Semantic Kernel 中，工具注册到 Kernel，然后将 Kernel 传递给代理。在 MAF 中，工具在代理创建过程中直接注册。

```python
agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]
```

### MAF 与 AutoGen 之间的差异

**团队与工作流**

`Teams` 是 AutoGen 中代理事件驱动活动的事件结构。MAF 使用 `Workflows`，通过基于图的架构将数据路由到执行器。

**工具创建**

AutoGen 使用 `FunctionTool` 包装函数以供代理调用。MAF 使用 @ai_function，其操作类似，但也会自动为每个函数推断架构。

**代理行为**

在 AutoGen 中，代理默认是单轮代理，除非 `max_tool_iterations` 设置为更高的值。在 MAF 中，`ChatAgent` 默认是多轮的，这意味着它会一直调用工具，直到用户的任务完成。

## 代码示例

Microsoft Agent Framework 的代码示例可以在本仓库的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 文件中找到。

## 对 Microsoft Agent Framework 还有更多问题？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者见面，参加办公时间并获得您的 AI Agents 问题的答案。