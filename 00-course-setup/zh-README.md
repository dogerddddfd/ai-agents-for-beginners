# 课程设置

## 介绍

本课程将介绍如何运行本课程的代码示例。

## 加入其他学习者并获取帮助

在开始克隆仓库之前，加入 [AI Agents For Beginners Discord 频道](https://aka.ms/ai-agents/discord) 以获取设置帮助、课程相关问题的解答，或与其他学习者建立联系。

## 克隆或分叉此仓库

首先，请克隆或分叉 GitHub 仓库。这将创建您自己的课程材料版本，以便您可以运行、测试和调整代码！

您可以通过点击链接 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">分叉仓库</a> 来完成此操作。

现在您应该拥有自己分叉的课程版本，链接如下：

![分叉的仓库](./images/forked-repo.png)

### 浅克隆（推荐用于工作坊 / Codespaces）

  >当您下载完整历史记录和所有文件时，完整仓库可能会很大（约 3 GB）。如果您只是参加工作坊或只需要几个课程文件夹，浅克隆（或稀疏克隆）可以通过截断历史记录和/或跳过 blobs 来避免大部分下载。

#### 快速浅克隆 — 最小历史记录，所有文件

在以下命令中用您的分叉 URL 替换 `<your-username>`（如果您愿意，也可以使用上游 URL）。

要仅克隆最新的提交历史记录（小下载）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

要克隆特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）克隆 — 最小 blobs + 仅选定文件夹

这使用部分克隆和稀疏检出（需要 Git 2.25+ 并推荐支持部分克隆的现代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

进入仓库文件夹：

```bash|powershell
cd ai-agents-for-beginners
```

然后指定您需要的文件夹（以下示例显示两个文件夹）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

克隆并验证文件后，如果您只需要文件并想释放空间（无 git 历史记录），请删除仓库元数据（💀 不可逆 — 您将失去所有 Git 功能：无提交、拉取、推送或历史记录访问）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推荐避免本地大型下载）

- 通过 [GitHub UI](https://github.com/codespaces) 为此仓库创建新的 Codespace。  

- 在新创建的 codespace 的终端中，运行上面的浅克隆/稀疏克隆命令之一，仅将您需要的课程文件夹带入 Codespace 工作区。
- 可选：在 Codespaces 内克隆后，删除 .git 以回收额外空间（见上面的删除命令）。
- 注意：如果您更喜欢直接在 Codespaces 中打开仓库（无需额外克隆），请注意 Codespaces 将构建 devcontainer 环境，可能仍然会配置超出您需要的内容。在新的 Codespace 中克隆浅拷贝可以让您更好地控制磁盘使用。

#### 提示

- 如果您想编辑/提交，请始终用您的分叉替换克隆 URL。
- 如果您以后需要更多历史记录或文件，您可以获取它们或调整稀疏检出以包含其他文件夹。

## 运行代码

本课程提供了一系列 Jupyter Notebooks，您可以运行它们来获得构建 AI 代理的实践经验。

代码示例使用以下任一方式：

**需要 GitHub 账户 - 免费**：

1) Semantic Kernel Agent Framework + GitHub Models Marketplace。标记为 (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace。标记为 (autogen.ipynb)

**需要 Azure 订阅**：

3) Azure AI Foundry + Azure AI Agent Service。标记为 (azureaiagent.ipynb)

我们鼓励您尝试所有三种类型的示例，看看哪一种最适合您。

无论您选择哪种选项，它都会决定您需要遵循以下哪些设置步骤：

## 要求

- Python 3.12+
  - **注意**：如果您没有安装 Python3.12，请确保安装它。 然后使用 python3.12 创建您的 venv，以确保从 requirements.txt 文件安装正确的版本。
  
    >示例

    创建 Python venv 目录：

    ```bash|powershell
    python -m venv venv
    ```

    然后激活 venv 环境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Windows 命令提示符
    venv\Scripts\activate
    ```

- .NET 10+：对于使用 .NET 的示例代码，请确保安装 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本。然后，检查您安装的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- GitHub 账户 - 用于访问 GitHub Models Marketplace
- Azure 订阅 - 用于访问 Azure AI Foundry
- Azure AI Foundry 账户 - 用于访问 Azure AI Agent Service

我们在本仓库的根目录中包含了一个 `requirements.txt` 文件，其中包含运行代码示例所需的所有 Python 包。

您可以通过在仓库根目录的终端中运行以下命令来安装它们：

```bash|powershell
pip install -r requirements.txt
```

我们建议创建 Python 虚拟环境以避免任何冲突和问题。

## 设置 VSCode

确保您在 VSCode 中使用正确版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 为使用 GitHub Models 的示例设置

### 步骤 1：获取您的 GitHub 个人访问令牌 (PAT)

本课程利用 GitHub Models Marketplace，提供对大型语言模型 (LLM) 的免费访问，您将使用这些模型来构建 AI 代理。

要使用 GitHub Models，您需要创建一个 [GitHub 个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)。

您可以通过访问 GitHub 账户中的 <a href="https://github.com/settings/personal-access-tokens" target="_blank">个人访问令牌设置</a> 来完成此操作。

请在创建令牌时遵循 [最小权限原则](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely)。这意味着您应该只给令牌运行本课程代码示例所需的权限。

1. 通过导航到 **开发者设置**，选择屏幕左侧的 `Fine-grained tokens` 选项

   ![开发者设置](./images/profile_developer_settings.png)

   然后选择 `Generate new token`。

   ![生成令牌](./images/fga_new_token.png)

2. 为您的令牌输入一个描述性名称，反映其用途，以便以后容易识别。

    🔐 令牌持续时间建议

    建议持续时间：30 天
    为了更安全的姿势，您可以选择更短的时间段，例如 7 天 🛡️
    这是一个设定个人目标并在学习动力高涨时完成课程的好方法 🚀。

    ![令牌名称和过期时间](./images/token-name-expiry-date.png)

3. 将令牌的范围限制为您的此仓库分叉。

    ![将范围限制为分叉仓库](./images/token_repository_limit.png)

4. 限制令牌的权限：在 **Permissions** 下，点击 **Account** 选项卡，然后点击 "+ Add permissions" 按钮。会出现一个下拉菜单。请搜索 **Models** 并勾选它。

    ![添加 Models 权限](./images/add_models_permissions.png)

5. 在生成令牌之前验证所需的权限。 ![验证权限](./images/verify_permissions.png)

6. 在生成令牌之前，确保您准备好将令牌存储在安全的地方，如密码管理器保险库中，因为在创建后不会再次显示。 ![安全存储令牌](./images/store_token_securely.png)

复制您刚刚创建的新令牌。现在您将把它添加到本课程包含的 `.env` 文件中。

### 步骤 2：创建您的 `.env` 文件

要创建您的 `.env` 文件，请在终端中运行以下命令。

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

这将复制示例文件并在您的目录中创建一个 `.env` 文件，您可以在其中填写环境变量的值。

复制令牌后，在您喜欢的文本编辑器中打开 `.env` 文件，并将您的令牌粘贴到 `GITHUB_TOKEN` 字段中。

![GitHub 令牌字段](./images/github_token_field.png)

现在您应该能够运行本课程的代码示例了。

## 为使用 Azure AI Foundry 和 Azure AI Agent Service 的示例设置

### 步骤 1：获取您的 Azure 项目端点

按照此处的步骤在 Azure AI Foundry 中创建中心和项目：[中心资源概述](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

创建项目后，您需要检索项目的连接字符串。

您可以通过转到 Azure AI Foundry 门户中项目的 **概述** 页面来完成此操作。

![项目连接字符串](./images/project-endpoint.png)

### 步骤 2：创建您的 `.env` 文件

要创建您的 `.env` 文件，请在终端中运行以下命令。

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

这将复制示例文件并在您的目录中创建一个 `.env` 文件，您可以在其中填写环境变量的值。

复制令牌后，在您喜欢的文本编辑器中打开 `.env` 文件，并将您的令牌粘贴到 `PROJECT_ENDPOINT` 字段中。

### 步骤 3：登录 Azure

作为安全最佳实践，我们将使用 [无密钥身份验证](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) 通过 Microsoft Entra ID 向 Azure OpenAI 进行身份验证。 

接下来，打开终端并运行 `az login --use-device-code` 登录到您的 Azure 账户。

登录后，在终端中选择您的订阅。

## 其他环境变量 - Azure Search 和 Azure OpenAI 

对于 Agentic RAG 课程 - 课程 5 - 有使用 Azure Search 和 Azure OpenAI 的示例。

如果您想运行这些示例，您需要将以下环境变量添加到您的 `.env` 文件中：

### 概述页面（项目）

- `AZURE_SUBSCRIPTION_ID` - 在项目的 **概述** 页面上查看 **项目详细信息**。

- `AZURE_AI_PROJECT_NAME` - 在项目的 **概述** 页面顶部查找。

- `AZURE_OPENAI_SERVICE` - 在 **概述** 页面的 **Azure OpenAI Service** 的 **包含的功能** 选项卡中找到。

### 管理中心

- `AZURE_OPENAI_RESOURCE_GROUP` - 转到 **管理中心** 的 **概述** 页面上的 **项目属性**。

- `GLOBAL_LLM_SERVICE` - 在 **连接的资源** 下，找到 **Azure AI Services** 连接名称。如果未列出，请在资源组下的 **Azure 门户** 中检查 AI Services 资源名称。

### 模型 + 端点页面

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 选择您的嵌入模型（例如 `text-embedding-ada-002`）并从模型详细信息中记下 **部署名称**。

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 选择您的聊天模型（例如 `gpt-4o-mini`）并从模型详细信息中记下 **部署名称**。

### Azure 门户

- `AZURE_OPENAI_ENDPOINT` - 查找 **Azure AI services**，点击它，然后转到 **资源管理**，**密钥和端点**，向下滚动到 "Azure OpenAI endpoints"，并复制显示 "Language APIs" 的那个。

- `AZURE_OPENAI_API_KEY` - 从同一屏幕复制 KEY 1 或 KEY 2。

- `AZURE_SEARCH_SERVICE_ENDPOINT` - 找到您的 **Azure AI Search** 资源，点击它，然后查看 **概述**。

- `AZURE_SEARCH_API_KEY` - 然后转到 **设置**，然后 **密钥** 复制主或辅助管理员密钥。

### 外部网页

- `AZURE_OPENAI_API_VERSION` - 访问 [API 版本生命周期](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) 页面下的 **Latest GA API release**。

### 设置无密钥身份验证

我们将使用与 Azure OpenAI 的无密钥连接，而不是硬编码您的凭据。为此，我们将导入 `DefaultAzureCredential` 并稍后调用 `DefaultAzureCredential` 函数来获取凭据。

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## 遇到问题？

如果您在运行此设置时遇到任何问题，请加入我们的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社区 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">创建问题</a>。

## 下一课

您现在可以运行本课程的代码了。祝您学习更多关于 AI 代理世界的知识！ 

[AI 代理简介和代理用例](../01-intro-to-ai-agents/README.md)