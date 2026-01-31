# Azure AI 智能体服务开发

在本练习中，你将使用 [Azure AI Foundry 门户](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) 中的 Azure AI 智能体服务工具创建一个用于航班预订的智能体。该智能体将能够与用户交互并提供有关航班的信息。

## 先决条件

要完成本练习，你需要以下内容：
1. 具有有效订阅的 Azure 账户。[免费创建账户](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
2. 你需要有权限创建 Azure AI Foundry 中心，或者已有为你创建的中心。
    - 如果你的角色是贡献者或所有者，你可以按照本教程中的步骤操作。

## 创建 Azure AI Foundry 中心

> **注意：** Azure AI Foundry 以前称为 Azure AI Studio。

1. 按照 [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) 博客文章中的指南创建 Azure AI Foundry 中心。
2. 当你的项目创建完成后，关闭显示的任何提示，并查看 Azure AI Foundry 门户中的项目页面，该页面应类似于以下图像：

    ![Azure AI Foundry 项目](./images/azure-ai-foundry.png)

## 部署模型

1. 在项目左侧窗格的 **我的资产** 部分中，选择 **模型 + 端点** 页面。
2. 在 **模型 + 端点** 页面的 **模型部署** 选项卡中，在 **+ 部署模型** 菜单中选择 **部署基础模型**。
3. 在列表中搜索 `gpt-4o-mini` 模型，然后选择并确认它。

    > **注意：** 减少 TPM 有助于避免过度使用你正在使用的订阅中可用的配额。

    ![模型已部署](./images/model-deployment.png)

## 创建智能体

现在你已经部署了模型，可以创建智能体。智能体是一种对话式 AI 模型，可用于与用户交互。

1. 在项目左侧窗格的 **构建和自定义** 部分中，选择 **智能体** 页面。
2. 单击 **+ 创建智能体** 创建新智能体。在 **智能体设置** 对话框下：
    - 为智能体输入名称，例如 `FlightAgent`。
    - 确保选择你之前创建的 `gpt-4o-mini` 模型部署
    - 根据你希望智能体遵循的提示设置 **指令**。以下是一个示例：
    ```
    你是 FlightAgent，一个专门处理与航班相关查询的虚拟助手。你的角色包括帮助用户搜索航班、检索航班详情、检查座位可用性以及提供实时航班状态。请按照以下说明确保你的回复清晰有效：

    ### 任务说明：
    1. **识别意图**：
       - 根据用户的请求识别其意图，重点关注以下类别之一：
         - 搜索航班
         - 使用航班 ID 检索航班详情
         - 检查指定航班的座位可用性
         - 使用航班号提供实时航班状态
       - 如果意图不明确，请礼貌地要求用户澄清或提供更多详细信息。
        
    2. **处理请求**：
        - 根据识别的意图执行所需任务：
        - 对于航班搜索：请求出发地、目的地、出发日期和可选的返回日期等详细信息。
        - 对于航班详情：请求有效的航班 ID。
        - 对于座位可用性：请求航班 ID 和日期并验证输入。
        - 对于航班状态：请求有效的航班号。
        - 对提供的数据进行验证（例如，日期、航班号或 ID 的格式）。如果信息不完整或无效，请友好地请求澄清。

    3. **生成响应**：
    - 使用友好、简洁和支持性的语气。
    - 根据每个任务的输出提供清晰可行的建议。
    - 如果未找到数据或发生错误，请向用户温和地解释并提供替代操作（例如，优化搜索、尝试其他查询）。
    ```
> [!NOTE]
> 有关详细提示，你可以查看 [此存储库](https://github.com/ShivamGoyal03/RoamMind) 获取更多信息。
    
> 此外，你可以添加 **知识库** 和 **操作** 来增强智能体的能力，以提供更多信息并根据用户请求执行自动化任务。在本练习中，你可以跳过这些步骤。
    
![智能体设置](./images/agent-setup.png)

3. 要创建新的多 AI 智能体，只需单击 **新智能体**。新创建的智能体将显示在智能体页面上。


## 测试智能体

创建智能体后，你可以在 Azure AI Foundry 门户的 playground 中测试它，看看它如何响应用户查询。

1. 在智能体的 **设置** 窗格顶部，选择 **在 playground 中尝试**。
2. 在 **Playground** 窗格中，你可以通过在聊天窗口中键入查询来与智能体交互。例如，你可以要求智能体搜索 28 日从西雅图到纽约的航班。

    > **注意：** 智能体可能不会提供准确的响应，因为本练习中未使用实时数据。目的是测试智能体基于提供的指令理解和响应用户查询的能力。

    ![智能体 Playground](./images/agent-playground.png)

3. 测试智能体后，你可以通过添加更多意图、训练数据和操作来进一步自定义它，以增强其能力。

## 清理资源

测试完智能体后，你可以将其删除以避免产生额外费用。
1. 打开 [Azure 门户](https://portal.azure.com) 并查看你在本练习中部署中心资源的资源组的内容。
2. 在工具栏上，选择 **删除资源组**。
3. 输入资源组名称并确认要删除它。

## 资源

- [Azure AI Foundry 文档](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Foundry 门户](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Studio 入门](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure 上的 AI 智能体基础](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)