# 使用 Microsoft Agent Framework Workflow 构建多智能体应用

本教程将引导您了解并使用 Microsoft Agent Framework 构建多智能体应用程序。我们将探索多智能体系统的核心概念，深入了解框架 Workflow 组件的架构，并通过 Python 和 .NET 中的不同工作流模式的实际示例进行讲解。

## 1. 理解多智能体系统

AI 智能体是一种超越标准大型语言模型 (LLM) 能力的系统。它可以感知环境、做出决策并采取行动来实现特定目标。多智能体系统涉及多个这样的智能体协作解决单个智能体难以或无法单独处理的问题。

### 常见应用场景

  * **复杂问题解决**：将大型任务（例如，规划公司范围的活动）分解为由专业智能体处理的较小子任务（例如，预算智能体、物流智能体、营销智能体）。
  * **虚拟助手**：主助手智能体将调度、研究和预订等任务委派给其他专业智能体。
  * **自动化内容创建**：一个智能体起草内容，另一个智能体审查其准确性和语调，第三个智能体发布内容的工作流程。

### 多智能体模式

多智能体系统可以以多种模式组织，这些模式决定了它们如何交互：

  * **顺序**：智能体按预定义顺序工作，如装配线。一个智能体的输出成为下一个智能体的输入。
  * **并发**：智能体并行处理任务的不同部分，最终聚合结果。
  * **条件**：工作流根据智能体的输出采取不同的路径，类似于 if-then-else 语句。

## 2. Microsoft Agent Framework Workflow 架构

Agent Framework 的工作流系统是一个高级编排引擎，旨在管理多个智能体之间的复杂交互。它基于图结构架构，使用 [Pregel 风格的执行模型](https://kowshik.github.io/JPregel/pregel_paper.pdf)，其中处理在称为"超级步骤"的同步步骤中进行。

### 核心组件

该架构由三个主要部分组成：

1.  **执行器**：这些是基本处理单元。在我们的示例中，`Agent` 是一种执行器。每个执行器可以有多个消息处理程序，这些处理程序会根据接收到的消息类型自动调用。
2.  **边**：这些定义了执行器之间消息传递的路径。边可以有条件，允许通过工作流图动态路由信息。
3.  **工作流**：此组件编排整个过程，管理执行器、边和整体执行流程。它确保消息按正确顺序处理并为可观察性流式传输事件。

*工作流系统核心组件的示意图。*

这种结构允许使用基本模式（如顺序链、用于并行处理的扇出/扇入以及用于条件流的开关逻辑）构建健壮且可扩展的应用程序。

## 3. 实际示例和代码分析

现在，让我们探讨如何使用该框架实现不同的工作流模式。我们将查看每个示例的 Python 和 .NET 代码。

### 案例 1：基本顺序工作流

这是最简单的模式，其中一个智能体的输出直接传递给另一个智能体。我们的场景涉及一个酒店 `FrontDesk` 智能体提供旅行建议，然后由 `Concierge` 智能体审查。

*基本 FrontDesk → Concierge 工作流的示意图。*

#### 场景背景

一位旅行者询问巴黎的建议。

1.  设计简洁的 `FrontDesk` 智能体建议参观卢浮宫博物馆。
2.  优先考虑真实体验的 `Concierge` 智能体收到此建议。它审查该建议并提供反馈，建议更本地化、更少旅游景点的替代方案。

#### Python 实现分析

在 Python 示例中，我们首先定义并创建两个智能体，每个都有特定的指令。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

接下来，使用 `WorkflowBuilder` 构建图。将 `front_desk_agent` 设置为起点，并创建一条边将其输出连接到 `reviewer_agent`。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最后，使用初始用户提示执行工作流。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) 实现分析

.NET 实现遵循非常相似的逻辑。首先，为智能体的名称和指令定义常量。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

使用 `OpenAIClient` 创建智能体，然后 `WorkflowBuilder` 通过添加从 `frontDeskAgent` 到 `reviewerAgent` 的边来定义顺序流。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

然后使用用户的消息运行工作流，并流式返回结果。

### 案例 2：多步骤顺序工作流

此模式扩展了基本序列以包含更多智能体。它非常适合需要多个阶段细化或转换的流程。

#### 场景背景

用户提供客厅的图像并要求提供家具报价。

1.  **Sales-Agent**：识别图像中的家具项目并创建列表。
2.  **Price-Agent**：获取项目列表并提供详细的价格明细，包括预算、中档和高端选项。
3.  **Quote-Agent**：接收定价列表并将其格式化为 Markdown 格式的正式报价文档。

*Sales → Price → Quote 工作流的示意图。*

#### Python 实现分析

定义了三个智能体，每个都有专门的角色。使用 `add_edge` 构建工作流以创建链：`sales_agent` → `price_agent` → `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

输入是包含文本和图像 URI 的 `ChatMessage`。框架处理将每个智能体的输出传递给序列中的下一个智能体，直到生成最终报价。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C#) 实现分析

.NET 示例与 Python 版本镜像。创建了三个智能体（`salesagent`、`priceagent`、`quoteagent`）。`WorkflowBuilder` 按顺序链接它们。

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

用户消息由图像数据（作为字节）和文本提示构成。`InProcessExecution.StreamAsync` 方法启动工作流，并从流中捕获最终输出。

### 案例 3：并发工作流

当任务可以同时执行以节省时间时，使用此模式。它涉及到向多个智能体的"扇出"和聚合结果的"扇入"。

#### 场景背景

用户要求计划前往西雅图的旅行。

1.  **分发器（扇出）**：用户的请求同时发送给两个智能体。
2.  **Researcher-Agent**：研究 12 月前往西雅图旅行的景点、天气和关键考虑因素。
3.  **Plan-Agent**：独立创建详细的逐日旅行 itinerary。
4.  **聚合器（扇入）**：收集研究人员和规划人员的输出，并将其作为最终结果一起呈现。

*并发 Researcher 和 Planner 工作流的示意图。*

#### Python 实现分析

`ConcurrentBuilder` 简化了此模式的创建。您只需列出参与的智能体，构建器会自动创建必要的扇出和扇入逻辑。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

框架确保 `research_agent` 和 `plan_agent` 并行执行，并且它们的最终输出被收集到一个列表中。

#### .NET (C#) 实现分析

在 .NET 中，此模式需要更明确的定义。创建自定义执行器（`ConcurrentStartExecutor` 和 `ConcurrentAggregationExecutor`）来处理扇出和扇入逻辑。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

然后 `WorkflowBuilder` 使用 `AddFanOutEdge` 和 `AddFanInEdge` 构建包含这些自定义执行器和智能体的图。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 案例 4：条件工作流

条件工作流引入分支逻辑，允许系统基于中间结果采取不同的路径。

#### 场景背景

此工作流自动创建和发布技术教程。

1.  **Evangelist-Agent**：根据给定的大纲和 URL 编写教程草稿。
2.  **ContentReviewer-Agent**：审查草稿。它检查字数是否超过 200 字。
3.  **条件分支**：
      * **如果批准（`Yes`）**：工作流继续到 `Publisher-Agent`。
      * **如果拒绝（`No`）**：工作流停止并输出拒绝原因。
4.  **Publisher-Agent**：如果草稿获得批准，此智能体将内容保存到 Markdown 文件。

#### Python 实现分析

此示例使用自定义函数 `select_targets` 实现条件逻辑。此函数传递给 `add_multi_selection_edge_group`，并基于审阅者输出的 `review_result` 字段指导工作流。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

使用 `to_reviewer_result` 等自定义执行器来解析智能体的 JSON 输出并将其转换为选择函数可以检查的强类型对象。

#### .NET (C#) 实现分析

.NET 版本使用类似的方法，带有条件函数。定义 `Func<object?, bool>` 来检查 `ReviewResult` 对象的 `Result` 属性。

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` 方法的 `condition` 参数允许 `WorkflowBuilder` 创建分支路径。只有当条件 `GetCondition(expectedResult: "Yes")` 返回 true 时，工作流才会沿着到 `publishExecutor` 的边前进。否则，它会沿着到 `sendReviewerExecutor` 的路径前进。

## 结论

Microsoft Agent Framework Workflow 为编排复杂的多智能体系统提供了强大而灵活的基础。通过利用其基于图的架构和核心组件，开发人员可以在 Python 和 .NET 中设计和实现复杂的工作流。无论您的应用程序需要简单的顺序处理、并行执行还是动态条件逻辑，该框架都提供了构建强大、可扩展且类型安全的 AI 驱动解决方案的工具。