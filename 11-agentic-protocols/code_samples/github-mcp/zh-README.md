# Github MCP 服务器示例

## 描述

这是为 Microsoft Reactor 举办的 AI Agents 黑客马拉松创建的演示。

该工具用于根据用户的 Github 仓库推荐黑客马拉松项目。实现方式如下：

1. **Github Agent** - 使用 Github MCP 服务器检索仓库和关于这些仓库的信息。
2. **Hackathon Agent** - 接收来自 Github Agent 的数据，根据项目、用户使用的语言以及 AI Agents 黑客马拉松的项目轨道，提出创意黑客马拉松项目想法。
3. **Events Agent** - 基于黑客马拉松代理的建议，事件代理将从 AI Agent 黑客马拉松系列中推荐相关活动。

## 运行代码

### 环境变量

此演示使用 Azure Open AI 服务、Semantic Kernel、Github MCP 服务器和 Azure AI 搜索。

确保您设置了正确的环境变量以使用这些工具：

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## 运行 Chainlit 服务器

为了连接到 MCP 服务器，此演示使用 Chainlit 作为聊天界面。

要运行服务器，请在终端中使用以下命令：

```bash
chainlit run app.py -w
```

这应该在 `localhost:8000` 上启动您的 Chainlit 服务器，并使用 `event-descriptions.md` 内容填充您的 Azure AI 搜索索引。

## 连接到 MCP 服务器

要连接到 Github MCP 服务器，请选择"在此输入您的消息..."聊天框下方的"插头"图标：

![MCP Connect](./images/mcp-chainlit-1.png)

从那里您可以点击"连接 MCP"以添加连接到 Github MCP 服务器的命令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[您的个人访问令牌]
```

将"[您的个人访问令牌]"替换为您实际的个人访问令牌。

连接后，您应该在插头图标旁边看到一个 (1) 以确认它已连接。如果没有，请尝试使用 `chainlit run app.py -w` 重新启动 chainlit 服务器。

## 使用演示

要启动推荐黑客马拉松项目的代理工作流程，您可以输入如下消息：

"为 Github 用户 koreyspace 推荐黑客马拉松项目"

路由代理将分析您的请求，并确定哪个代理组合（GitHub、Hackathon 和 Events）最适合处理您的查询。代理们将共同努力，基于 GitHub 仓库分析、项目构思和相关技术活动提供全面的推荐。
