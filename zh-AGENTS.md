# AGENTS.md

## 项目概述

本仓库包含「AI Agents for Beginners」—— 一门全面的教育课程，教授构建 AI 代理所需的所有知识。该课程由 15+ 课时组成，涵盖 AI 代理的基础知识、设计模式、框架和生产部署。

**核心技术：**
- Python 3.12+
- Jupyter Notebooks 用于交互式学习
- AI 框架：Semantic Kernel、AutoGen、Microsoft Agent Framework (MAF)
- Azure AI 服务：Azure AI Foundry、Azure AI Agent Service
- GitHub Models Marketplace（提供免费层级）

**架构：**
- 基于课时的结构（00-15+ 目录）
- 每个课时包含：README 文档、代码示例（Jupyter 笔记本）和图片
- 通过自动化翻译系统支持多语言
- 每个课时提供多种框架选项（Semantic Kernel、AutoGen、Azure AI Agent Service）

## 设置命令

### 先决条件
- Python 3.12 或更高版本
- GitHub 账号（用于 GitHub Models - 免费层级）
- Azure 订阅（可选，用于 Azure AI 服务）

### 初始设置

1. **克隆或复刻仓库：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **创建并激活 Python 虚拟环境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```

3. **安装依赖：**
   ```bash
   pip install -r requirements.txt
   ```

4. **设置环境变量：**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件，添加你的 API 密钥和端点
   ```

### 必需的环境变量

对于 **GitHub Models（免费）**：
- `GITHUB_TOKEN` - 来自 GitHub 的个人访问令牌

对于 **Azure AI 服务**（可选）：
- `PROJECT_ENDPOINT` - Azure AI Foundry 项目端点
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API 密钥
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端点 URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 聊天模型的部署名称
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 嵌入模型的部署名称
- 如 `.env.example` 中所示的其他 Azure 配置

## 开发工作流

### 运行 Jupyter 笔记本

每个课时包含多个不同框架的 Jupyter 笔记本：

1. **启动 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **导航到课时目录**（例如，`01-intro-to-ai-agents/code_samples/`）

3. **打开并运行笔记本：**
   - `*-semantic-kernel.ipynb` - 使用 Semantic Kernel 框架
   - `*-autogen.ipynb` - 使用 AutoGen 框架
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework（.NET）
   - `*-azureaiagent.ipynb` - 使用 Azure AI Agent Service

### 使用不同的框架

**Semantic Kernel + GitHub Models：**
- 可通过 GitHub 账号使用免费层级
- 适合学习和实验
- 文件模式：`*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models：**
- 可通过 GitHub 账号使用免费层级
- 多代理编排能力
- 文件模式：`*-autogen.ipynb`

**Microsoft Agent Framework (MAF)：**
- Microsoft 最新的框架
- 支持 Python 和 .NET
- 文件模式：`*-agent-framework.ipynb`

**Azure AI Agent Service：**
- 需要 Azure 订阅
- 生产就绪功能
- 文件模式：`*-azureaiagent.ipynb`

## 测试说明

这是一个教育仓库，包含示例代码而非带有自动化测试的生产代码。要验证你的设置和更改：

### 手动测试

1. **测试 Python 环境：**
   ```bash
   python --version  # 应该是 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **测试笔记本执行：**
   ```bash
   # 将笔记本转换为脚本并运行（测试导入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **验证环境变量：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 运行单个笔记本

在 Jupyter 中打开笔记本并按顺序执行单元格。每个笔记本都是自包含的，包括：
- 导入语句
- 配置加载
- 示例代理实现
- markdown 单元格中的预期输出

## 代码风格

### Python 约定

- **Python 版本**：3.12+
- **代码风格**：遵循标准 Python PEP 8 约定
- **笔记本**：使用清晰的 markdown 单元格解释概念
- **导入**：按标准库、第三方、本地导入分组

### Jupyter 笔记本约定

- 在代码单元格前包含描述性的 markdown 单元格
- 在笔记本中添加输出示例作为参考
- 使用与课程概念匹配的清晰变量名
- 保持笔记本执行顺序线性（单元格 1 → 2 → 3...）

### 文件组织

```
<lesson-number>-<lesson-name>/
├── README.md                     # 课时文档
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## 构建和部署

### 构建文档

本仓库使用 Markdown 进行文档编写：
- 每个课时文件夹中的 README.md 文件
- 仓库根目录的主 README.md
- 通过 GitHub Actions 的自动化翻译系统

### CI/CD 管道

位于 `.github/workflows/`：

1. **co-op-translator.yml** - 自动翻译成 50+ 种语言
2. **welcome-issue.yml** - 欢迎新的 issue 创建者
3. **welcome-pr.yml** - 欢迎新的 pull request 贡献者

### 部署

这是一个教育仓库 - 没有部署过程。用户：
1. 复刻或克隆仓库
2. 在本地或 GitHub Codespaces 中运行笔记本
3. 通过修改和实验示例进行学习

## Pull Request 指南

### 提交前

1. **测试你的更改：**
   - 完整运行受影响的笔记本
   - 验证所有单元格执行无错误
   - 检查输出是否适当

2. **文档更新：**
   - 如果添加新概念，更新 README.md
   - 在笔记本中为复杂代码添加注释
   - 确保 markdown 单元格解释目的

3. **文件更改：**
   - 避免提交 `.env` 文件（使用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目录
   - 当笔记本输出展示概念时保留它们
   - 删除临时文件和备份笔记本（`*-backup.ipynb`）

### PR 标题格式

使用描述性标题：
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### 必需检查

- 笔记本应执行无错误
- README 文件应清晰准确
- 遵循仓库中现有的代码模式
- 与其他课时保持一致性

## 其他说明

### 常见问题

1. **Python 版本不匹配：**
   - 确保使用 Python 3.12+
   - 某些包可能不适用于较旧版本
   - 使用 `python3 -m venv` 明确指定 Python 版本

2. **环境变量：**
   - 始终从 `.env.example` 创建 `.env`
   - 不要提交 `.env` 文件（它在 `.gitignore` 中）
   - GitHub 令牌需要适当的权限

3. **包冲突：**
   - 使用新的虚拟环境
   - 从 `requirements.txt` 安装，而不是单个包
   - 一些笔记本可能需要在其 markdown 单元格中提到的额外包

4. **Azure 服务：**
   - Azure AI 服务需要活跃订阅
   - 某些功能是区域特定的
   - GitHub Models 适用免费层级限制

### 学习路径

推荐的课时学习顺序：
1. **00-course-setup** - 从这里开始进行环境设置
2. **01-intro-to-ai-agents** - 了解 AI 代理基础知识
3. **02-explore-agentic-frameworks** - 学习不同的框架
4. **03-agentic-design-patterns** - 核心设计模式
5. 按顺序继续学习编号课时

### 框架选择

根据你的目标选择框架：
- **学习/原型设计**：Semantic Kernel + GitHub Models（免费）
- **多代理系统**：AutoGen
- **最新功能**：Microsoft Agent Framework (MAF)
- **生产部署**：Azure AI Agent Service

### 获取帮助

- 加入 [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查看课时 README 文件获取特定指导
- 检查主 [README.md](./README.md) 获取课程概述
- 参考 [Course Setup](./00-course-setup/README.md) 获取详细的设置说明

### 贡献

这是一个开放的教育项目。欢迎贡献：
- 改进代码示例
- 修复拼写错误或错误
- 添加澄清注释
- 建议新的课时主题
- 翻译成其他语言

查看 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解当前需求。

## 项目特定上下文

### 多语言支持

本仓库使用自动化翻译系统：
- 支持 50+ 种语言
- 翻译位于 `/translations/<lang-code>/` 目录
- GitHub Actions 工作流处理翻译更新
- 源文件在仓库根目录为英文

### 课时结构

每个课时遵循一致的模式：
1. 带链接的视频缩略图
2. 书面课时内容（README.md）
3. 多个框架的代码示例
4. 学习目标和先决条件
5. 链接的额外学习资源

### 代码示例命名

格式：`<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - 第 4 课时，Semantic Kernel
- `07-autogen.ipynb` - 第 7 课时，AutoGen
- `14-python-agent-framework.ipynb` - 第 14 课时，MAF Python
- `14-dotnet-agent-framework.ipynb` - 第 14 课时，MAF .NET

### 特殊目录

- `translated_images/` - 翻译的本地化图片
- `images/` - 英文内容的原始图片
- `.devcontainer/` - VS Code 开发容器配置
- `.github/` - GitHub Actions 工作流和模板

### 依赖项

`requirements.txt` 中的关键包：
- `autogen-agentchat`、`autogen-core`、`autogen-ext` - AutoGen 框架
- `semantic-kernel` - Semantic Kernel 框架
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`、`azure-ai-projects` - Azure AI 服务
- `azure-search-documents` - Azure AI Search 集成
- `chromadb` - 用于 RAG 示例的向量数据库
- `chainlit` - 聊天 UI 框架
- `browser_use` - 代理的浏览器自动化
- `mcp[cli]` - Model Context Protocol 支持
- `mem0ai` - 代理的内存管理