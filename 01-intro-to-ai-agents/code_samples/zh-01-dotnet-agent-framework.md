# 🌍 使用 Microsoft Agent Framework (.NET) 的 AI 旅行代理

## 📋 场景概述

本示例演示如何使用适用于 .NET 的 Microsoft Agent Framework 构建智能旅行规划代理。该代理可以自动为世界各地的随机目的地生成个性化的一日游行程。

### 关键功能：

- 🎲 **随机目的地选择**：使用自定义工具选择度假地点
- 🗺️ **智能旅行规划**：创建详细的逐日行程
- 🔄 **实时流式传输**：支持即时和流式响应
- 🛠️ **自定义工具集成**：演示如何扩展代理功能

## 🔧 技术架构

### 核心技术

- **Microsoft Agent Framework**：用于 AI 代理开发的最新 .NET 实现
- **GitHub Models 集成**：使用 GitHub 的 AI 模型推理服务
- **OpenAI API 兼容性**：利用 OpenAI 客户端库和自定义端点
- **安全配置**：基于环境的 API 密钥管理

### 关键组件

1. **AIAgent**：处理对话流程的主要代理编排器
2. **自定义工具**：代理可用的 `GetRandomDestination()` 函数
3. **聊天客户端**：基于 GitHub Models 的对话界面
4. **流式支持**：实时响应生成功能

### 集成模式

```mermaid
graph LR
    A[用户请求] --> B[AI 代理]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination 工具]
    C --> E[旅行行程]
    D --> E
```

## 🚀 入门指南

### 先决条件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本
- [GitHub Models API 访问令牌](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### 必需的环境变量

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```

```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```

### 示例代码

要运行代码示例：

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

完整代码请参见 [`01-dotnet-agent-framework.cs`](./01-dotnet-agent-framework.cs)。

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

// 工具函数：随机目的地生成器
// 此静态方法将作为可调用工具提供给代理
// [Description] 属性帮助 AI 了解何时使用此函数
// 这演示了如何为 AI 代理创建自定义工具
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // 世界各地的热门度假目的地列表
    // 代理将从这些选项中随机选择
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };

    // 生成随机索引并返回选定的目的地
    // 使用 System.Random 进行简单的随机选择
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// 从环境变量中提取配置
// 检索 GitHub Models API 端点，如果未指定则默认为 https://models.github.ai/inference
// 检索模型 ID，如果未指定则默认为 openai/gpt-5-mini
// 检索用于身份验证的 GitHub 令牌，如果未指定则抛出异常
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// 配置 OpenAI 客户端选项
// 创建配置选项以指向 GitHub Models 端点
// 这会将 OpenAI 客户端调用重定向到 GitHub 的模型推理服务
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// 使用 GitHub Models 配置初始化 OpenAI 客户端
// 使用 GitHub 令牌创建 OpenAI 客户端进行身份验证
// 配置它使用 GitHub Models 端点而不是直接使用 OpenAI
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// 创建具有旅行规划功能的 AI 代理
// 初始化 OpenAI 客户端，获取指定模型的聊天客户端，并创建 AI 代理
// 使用旅行规划指令和随机目的地工具配置代理
// 代理现在可以使用 GetRandomDestination 函数规划旅行
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// 执行代理：规划一日游
// 运行代理并启用流式传输以实时显示响应
// 显示代理在生成内容时的思考和响应
// 通过即时反馈提供更好的用户体验
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 关键要点

1. **代理架构**：Microsoft Agent Framework 为在 .NET 中构建 AI 代理提供了清晰、类型安全的方法
2. **工具集成**：使用 `[Description]` 属性装饰的函数成为代理可用的工具
3. **配置管理**：环境变量和安全凭证处理遵循 .NET 最佳实践
4. **OpenAI 兼容性**：GitHub Models 集成通过 OpenAI 兼容的 API 无缝工作

## 🔗 其他资源

- [Microsoft Agent Framework 文档](https://learn.microsoft.com/agent-framework)
- [GitHub Models 市场](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET 单文件应用](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)
