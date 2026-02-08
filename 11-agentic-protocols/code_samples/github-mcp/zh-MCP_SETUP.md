# MCP 服务器集成指南

## 先决条件
- 已安装 Node.js（版本 14 或更高）
- npm 包管理器
- 带有所需依赖项的 Python 环境

## 设置步骤

1. **安装 MCP 服务器包**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **启动 MCP 服务器**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   服务器应该启动并显示连接 URL。

3. **验证连接**
   - 在 Chainlit 界面中查找插件图标（🔌）
   - 插件图标旁边应该出现一个数字（1），表示连接成功
   - 控制台应该显示："GitHub plugin setup completed successfully"（以及额外的状态行）

## 故障排除

### 常见问题

1. **端口冲突**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   解决方案：使用以下命令更改端口：
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **身份验证问题**
   - 确保 GitHub 凭据已正确配置
   - 检查 .env 文件包含所需的令牌
   - 验证 GitHub API 访问权限

3. **连接失败**
   - 确认服务器在预期端口上运行
   - 检查防火墙设置
   - 验证 Python 环境具有所需的包

## 连接验证

当满足以下条件时，您的 MCP 服务器已正确连接：
1. 控制台显示 "GitHub plugin setup completed successfully"
2. 连接日志显示 "✓ MCP Connection Status: Active"
3. GitHub 命令在聊天界面中正常工作

## 环境变量

在您的 .env 文件中需要以下内容：
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # 可选，默认为 3000
```

## 测试连接

在聊天中发送此测试消息：
```
Show me the repositories for username: [GitHub Username]
```
成功的响应将显示仓库信息。
