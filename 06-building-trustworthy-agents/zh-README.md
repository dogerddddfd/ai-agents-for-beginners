[![可信AI代理](./images/lesson-6-thumbnail.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(点击上面的图片观看本课视频)_

# 构建可信的AI代理

## 简介

本课程将涵盖：

- 如何构建和部署安全有效的AI代理
- 开发AI代理时的重要安全考虑因素
- 开发AI代理时如何维护数据和用户隐私

## 学习目标

完成本课程后，您将了解如何：

- 识别和缓解创建AI代理时的风险
- 实施安全措施，确保数据和访问得到适当管理
- 创建维护数据隐私并提供优质用户体验的AI代理

## 安全性

让我们首先了解如何构建安全的代理应用程序。安全性意味着AI代理按照设计执行。作为代理应用程序的构建者，我们有方法和工具来最大化安全性：

### 构建系统消息框架

如果您曾经使用大型语言模型（LLMs）构建AI应用程序，您就会知道设计强大的系统提示或系统消息的重要性。这些提示为LLM如何与用户和数据交互建立了元规则、指令和指南。

对于AI代理，系统提示更为重要，因为AI代理需要高度具体的指令来完成我们为其设计的任务。

为了创建可扩展的系统提示，我们可以使用系统消息框架来构建应用程序中的一个或多个代理：

![构建系统消息框架](./images/system-message-framework.png)

#### 步骤1：创建元系统消息

元提示将被LLM用于生成我们创建的代理的系统提示。我们将其设计为模板，以便在需要时可以高效地创建多个代理。

以下是我们给LLM的元系统消息示例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 步骤2：创建基本提示

下一步是创建描述AI代理的基本提示。您应该包括代理的角色、代理将完成的任务以及代理的任何其他职责。

例如：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 步骤3：向LLM提供基本系统消息

现在，我们可以通过提供元系统消息作为系统消息和我们的基本系统消息来优化这个系统消息。

这将生成一个更好地设计用于指导我们的AI代理的系统消息：

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### 步骤4：迭代和改进

这个系统消息框架的价值在于能够更轻松地扩展创建多个代理的系统消息，并随着时间的推移改进系统消息。很少有系统消息在第一次使用时就能完全适合您的完整用例。通过更改基本系统消息并通过系统运行它来进行小的调整和改进，您可以比较和评估结果。

## 了解威胁

要构建可信的AI代理，重要的是了解并缓解AI代理的风险和威胁。让我们看看AI代理面临的一些不同威胁以及如何更好地规划和准备应对它们。

![了解威胁](./images/understanding-threats.png)

### 任务和指令

**描述：** 攻击者尝试通过提示或操纵输入来更改AI代理的指令或目标。

**缓解措施：** 执行验证检查和输入过滤器，以在AI代理处理之前检测潜在危险的提示。由于这些攻击通常需要与代理频繁交互，限制对话中的轮数是防止这些类型攻击的另一种方法。

### 对关键系统的访问

**描述：** 如果AI代理可以访问存储敏感数据的系统和服务，攻击者可能会破坏代理与这些服务之间的通信。这些可能是直接攻击或通过代理间接获取有关这些系统的信息的尝试。

**缓解措施：** AI代理应该仅在必要的基础上访问系统，以防止这些类型的攻击。代理和系统之间的通信也应该是安全的。实施身份验证和访问控制是保护这些信息的另一种方法。

### 资源和服务过载

**描述：** AI代理可以访问不同的工具和服务来完成任务。攻击者可以利用这种能力通过AI代理发送大量请求来攻击这些服务，这可能导致系统故障或高成本。

**缓解措施：** 实施政策以限制AI代理可以向服务发出的请求数量。限制对AI代理的对话轮数和请求是防止这些类型攻击的另一种方法。

### 知识库中毒

**描述：** 这种类型的攻击不直接针对AI代理，而是针对AI代理将使用的知识库和其他服务。这可能涉及损坏AI代理将用于完成任务的数据或信息，导致对用户的偏见或意外响应。

**缓解措施：** 定期验证AI代理将在其工作流程中使用的数据。确保对此数据的访问是安全的，并且只有受信任的个人才能更改，以避免这种类型的攻击。

### 级联错误

**描述：** AI代理访问各种工具和服务来完成任务。攻击者造成的错误可能导致AI代理连接的其他系统失败，导致攻击变得更加广泛且难以排查。

**缓解措施：** 避免这种情况的一种方法是让AI代理在有限的环境中运行，例如在Docker容器中执行任务，以防止直接的系统攻击。当某些系统响应错误时，创建回退机制和重试逻辑是防止更大系统故障的另一种方法。

## 人工参与循环

构建可信AI代理系统的另一种有效方法是使用人工参与循环（Human-in-the-Loop）。这创建了一个流程，用户可以在运行期间向代理提供反馈。用户本质上在多代理系统中充当代理，并通过提供对运行过程的批准或终止来发挥作用。

![人工参与循环](./images/human-in-the-loop.png)

以下是使用AutoGen实现此概念的代码片段：

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## 结论

构建可信的AI代理需要仔细设计、强大的安全措施和持续的迭代。通过实施结构化的元提示系统、了解潜在威胁并应用缓解策略，开发人员可以创建既安全又有效的AI代理。此外，采用人工参与循环方法确保AI代理与用户需求保持一致，同时最大限度地减少风险。随着AI的不断发展，在安全、隐私和道德考虑方面保持积极态度将是培养AI驱动系统中的信任和可靠性的关键。

### 对构建可信AI代理还有更多问题？

加入[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者见面，参加办公时间并获得AI代理问题的答案。

## 其他资源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">负责任的AI概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式AI模型和AI应用程序的评估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系统消息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">风险评估模板</a>

## 上一课

[代理式RAG](../05-agentic-rag/README.md)

## 下一课

[规划设计模式](../07-planning-design/README.md)