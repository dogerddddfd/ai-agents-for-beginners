# Azure AI Search 设置指南

本指南将帮助您使用 Azure 门户设置 Azure AI Search。按照以下步骤创建和配置您的 Azure AI Search 服务。

## 先决条件

开始之前，请确保您拥有以下内容：

- Azure 订阅。如果您没有 Azure 订阅，可以在 [Azure 免费账户](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 创建一个免费账户。

## 步骤 1：创建 Azure 存储账户

1. 按照此说明 [创建 Azure 存储账户](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 创建新的 Azure 存储账户。
   **注意**：确保存储账户类型为标准通用用途 V2。

## 步骤 2：创建 Azure AI Search 服务

1. 登录 [Azure 门户](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左侧导航窗格中，点击 **创建资源**。
3. 在搜索框中，输入 "Azure AI Search" 并从结果列表中选择 **Azure AI Search**。
4. 点击 **创建** 按钮。
5. 在 **基本信息** 选项卡中，提供以下信息：
   - **订阅**：选择您的 Azure 订阅。
   - **资源组**：创建新的资源组或选择现有资源组。
   - **资源名称**：为您的搜索服务输入唯一的名称。
   - **区域**：选择离您的用户最近的区域。
   - **定价层**：选择适合您需求的定价层。您可以从免费层开始测试。
6. 点击 **查看 + 创建**。
7. 查看设置并点击 **创建** 以创建搜索服务。

## 步骤 3：开始使用 Azure AI Search

1. 部署完成后，导航到 Azure 门户中的搜索服务。
2. 在搜索服务概述窗格中，复制 URL。它应该类似于 `https://<service-name>.search.windows.net`。
3. 在设置 > 密钥窗格中，复制查询密钥。
4. 按照 [快速入门指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 页面中的步骤创建索引、上传数据并执行搜索查询。

## 步骤 4：使用 Azure AI Search 工具

Azure AI Search 与各种工具集成，以增强您的搜索能力。您可以使用 Azure CLI、Python SDK、.NET SDK 和其他工具进行高级配置和操作。

### 使用 Azure CLI

1. 按照 [安装 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 中的说明安装 Azure CLI。
2. 使用以下命令登录到 Azure CLI：

   ```bash
   az login
   ```

3. 将 Azure AI Search 实例的端点和 API 密钥存储到环境变量中。

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### 使用 Python SDK

1. 安装适用于 Python 的 Azure Cognitive Search 客户端库：

   ```bash
   pip install azure-search-documents
   ```

2. 使用以下 Python 代码创建索引并上传文档：

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### 使用 .NET SDK

1. 运行以下命令创建索引并上传文档：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. 以下是 `AzureSearch.cs` 的 .NET 代码：

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

有关更详细的信息，请参考以下文档：

- [创建 Azure Cognitive Search 服务](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [开始使用 Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 结论

您已经使用 Azure 门户和集成工具成功设置了 Azure AI Search。现在您可以探索 Azure AI Search 的更多高级功能和能力，以增强您的搜索解决方案。

如需进一步帮助，请访问 [Azure Cognitive Search 文档](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。