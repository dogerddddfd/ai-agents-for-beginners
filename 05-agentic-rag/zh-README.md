[![Agentic RAG](./images/lesson-5-thumbnail.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(点击上方图片观看本课程视频)_

# 智能体增强检索生成 (Agentic RAG)

本课程全面介绍智能体增强检索生成（Agentic RAG），这是一种新兴的AI范式，其中大型语言模型（LLM）在从外部来源获取信息的同时自主规划下一步行动。与静态的"检索后阅读"模式不同，Agentic RAG涉及对LLM的迭代调用，穿插工具或函数调用以及结构化输出。系统会评估结果，优化查询，在需要时调用额外工具，并持续此循环直到获得满意的解决方案。

## 简介

本课程将涵盖

- **理解Agentic RAG**：了解AI中新兴的范式，其中大型语言模型（LLM）在从外部数据源获取信息的同时自主规划下一步行动。
- **掌握迭代"生成-检查"风格**：理解对LLM的迭代调用循环，穿插工具或函数调用以及结构化输出，旨在提高正确性并处理格式错误的查询。
- **探索实际应用**：识别Agentic RAG表现出色的场景，如优先考虑正确性的环境、复杂的数据库交互和扩展工作流。

## 学习目标

完成本课程后，您将了解如何/理解：

- **理解Agentic RAG**：了解AI中新兴的范式，其中大型语言模型（LLM）在从外部数据源获取信息的同时自主规划下一步行动。
- **迭代"生成-检查"风格**：掌握对LLM的迭代调用循环的概念，穿插工具或函数调用以及结构化输出，旨在提高正确性并处理格式错误的查询。
- **自主推理过程**：理解系统能够自主管理其推理过程，在不依赖预定义路径的情况下决定如何处理问题。
- **工作流程**：了解智能体模型如何独立决定检索市场趋势报告、识别竞争对手数据、关联内部销售指标、综合发现并评估策略。
- **迭代循环、工具集成和记忆**：了解系统依赖于循环交互模式，在步骤之间保持状态和记忆，以避免重复循环并做出明智的决策。
- **处理失败模式和自我纠正**：探索系统强大的自我纠正机制，包括迭代和重新查询、使用诊断工具以及依赖人工监督。
- **智能体的边界**：理解Agentic RAG的局限性，关注特定领域的自主性、基础设施依赖性以及对护栏的尊重。
- **实际用例和价值**：识别Agentic RAG表现出色的场景，如优先考虑正确性的环境、复杂的数据库交互和扩展工作流。

## 什么是Agentic RAG？

智能体增强检索生成（Agentic RAG）是一种新兴的AI范式，其中大型语言模型（LLM）在从外部来源获取信息的同时自主规划下一步行动。与静态的"检索后阅读"模式不同，Agentic RAG涉及对LLM的迭代调用，穿插工具或函数调用以及结构化输出。系统会评估结果，优化查询，在需要时调用额外工具，并持续此循环直到获得满意的解决方案。这种迭代的"生成-检查"风格提高了正确性，处理了格式错误的查询，并确保了高质量的结果。

系统积极管理其推理过程，重写失败的查询，选择不同的检索方法，并整合多种工具（如Azure AI Search中的向量搜索、SQL数据库或自定义API），然后才最终确定其答案。使系统具有"智能体"特性的显著品质是其能够自主管理推理过程。传统的RAG实现依赖于预定义的路径，但智能体系统会根据找到的信息质量自主确定步骤顺序。

## 定义智能体增强检索生成（Agentic RAG）

智能体增强检索生成（Agentic RAG）是AI开发中的一种新兴范式，其中LLM不仅从外部数据源获取信息，还自主规划下一步行动。与静态的"检索后阅读"模式或精心编写的提示序列不同，Agentic RAG涉及对LLM的迭代调用循环，穿插工具或函数调用以及结构化输出。在每个回合，系统评估已获得的结果，决定是否优化查询，在需要时调用额外工具，并持续此循环直到获得满意的解决方案。

这种迭代的"生成-检查"操作风格旨在提高正确性，处理对结构化数据库（例如NL2SQL）的格式错误查询，并确保平衡、高质量的结果。系统不是仅仅依赖精心设计的提示链，而是积极管理其推理过程。它可以重写失败的查询，选择不同的检索方法，并整合多种工具（如Azure AI Search中的向量搜索、SQL数据库或自定义API），然后才最终确定其答案。这消除了对过于复杂的编排框架的需求。相反，相对简单的"LLM调用→工具使用→LLM调用→..."循环可以产生复杂且有充分根据的输出。

![Agentic RAG Core Loop](./images/agentic-rag-core-loop.png)

## 自主推理过程

使系统具有"智能体"特性的显著品质是其能够自主管理推理过程。传统的RAG实现通常依赖人类为模型预定义路径：一个思考链，概述何时检索什么。
但当系统真正具有智能体特性时，它会在内部决定如何处理问题。它不仅仅是执行脚本；它会根据找到的信息质量自主确定步骤顺序。
例如，如果要求它创建产品发布策略，它不仅仅依赖于详细说明整个研究和决策工作流程的提示。相反，智能体模型会独立决定：

1. 使用Bing Web Grounding检索当前市场趋势报告
2. 使用Azure AI Search识别相关竞争对手数据
3. 使用Azure SQL Database关联历史内部销售指标
4. 通过Azure OpenAI Service将发现综合成连贯的策略
5. 评估策略中的差距或不一致之处，必要时提示另一轮检索
所有这些步骤——优化查询、选择来源、迭代直到对答案"满意"——都是由模型决定的，而不是由人类预先编写的。

## 迭代循环、工具集成和记忆

![Tool Integration Architecture](./images/tool-integration.png)

智能体系统依赖于循环交互模式：

- **初始调用**：将用户的目标（即用户提示）呈现给LLM
- **工具调用**：如果模型识别到缺失信息或模糊指令，它会选择工具或检索方法——如向量数据库查询（例如Azure AI Search对私有数据的混合搜索）或结构化SQL调用——来收集更多上下文
- **评估与优化**：在审查返回的数据后，模型决定信息是否足够。如果不够，它会优化查询，尝试不同的工具，或调整其方法
- **重复直到满意**：此循环持续进行，直到模型确定它有足够的清晰度和证据来提供最终的、合理的响应
- **记忆与状态**：由于系统在步骤之间保持状态和记忆，它可以回忆以前的尝试及其结果，避免重复循环，并在进行过程中做出更明智的决策

随着时间的推移，这会产生一种不断发展的理解感，使模型能够导航复杂的多步骤任务，而不需要人类不断干预或重塑提示。

## 处理失败模式和自我纠正

Agentic RAG的自主性还涉及强大的自我纠正机制。当系统遇到死胡同时——例如检索不相关文档或遇到格式错误的查询——它可以：

- **迭代和重新查询**：模型不会返回低价值的响应，而是尝试新的搜索策略，重写数据库查询，或查看替代数据集
- **使用诊断工具**：系统可能会调用旨在帮助它调试推理步骤或确认检索数据正确性的附加功能。像Azure AI Tracing这样的工具对于实现强大的可观察性和监控非常重要
- **依赖人工监督**：对于高风险或反复失败的场景，模型可能会标记不确定性并请求人工指导。一旦人类提供纠正性反馈，模型可以在未来纳入该教训

这种迭代和动态的方法使模型能够不断改进，确保它不仅仅是一个一次性系统，而是一个在给定会话中从错误中学习的系统。

![Self Correction Mechanism](./images/self-correction.png)

## 智能体的边界

尽管智能体在任务中具有自主性，但Agentic RAG并不等同于通用人工智能。其"智能体"能力仅限于人类开发人员提供的工具、数据源和政策。它不能发明自己的工具或超出已设置的域边界。相反，它擅长动态编排手头的资源。
与更高级AI形式的关键区别包括：

1. **特定领域的自主性**：Agentic RAG系统专注于在已知领域内实现用户定义的目标，采用查询重写或工具选择等策略来改善结果
2. **依赖基础设施**：系统的能力取决于开发人员集成的工具和数据。没有人工干预，它无法超越这些边界
3. **尊重护栏**：道德准则、合规规则和业务政策仍然非常重要。智能体的自由始终受到安全措施和监督机制的限制（希望如此？）

## 实际用例和价值

Agentic RAG在需要迭代优化和精确性的场景中表现出色：

1. **优先考虑正确性的环境**：在合规检查、监管分析或法律研究中，智能体模型可以反复验证事实，咨询多个来源，并重写查询，直到产生经过彻底审查的答案
2. **复杂的数据库交互**：在处理查询可能经常失败或需要调整的结构化数据时，系统可以使用Azure SQL或Microsoft Fabric OneLake自主优化查询，确保最终检索与用户意图一致
3. **扩展工作流**：随着新信息的出现，长时间运行的会话可能会演变。Agentic RAG可以不断整合新数据，随着对问题空间的了解更多而调整策略

## 治理、透明度和信任

随着这些系统在推理中变得更加自主，治理和透明度至关重要：

- **可解释的推理**：模型可以提供它所做查询、所咨询来源以及达成结论所采取推理步骤的审计跟踪。像Azure AI Content Safety和Azure AI Tracing / GenAIOps这样的工具可以帮助保持透明度并减轻风险
- **偏见控制和平衡检索**：开发人员可以调整检索策略，确保考虑平衡、代表性的数据源，并定期审计输出，以检测使用Azure Machine Learning的高级数据科学组织的自定义模型的偏见或偏差模式
- **人工监督和合规**：对于敏感任务，人工审查仍然必不可少。Agentic RAG不会取代高风险决策中的人工判断——它通过提供更彻底审查的选项来增强人工判断

拥有提供清晰行动记录的工具至关重要。没有这些工具，调试多步骤过程可能非常困难。请参见Literal AI（Chainlit背后的公司）的智能体运行示例：

![AgentRunExample](./images/AgentRunExample.png)

## 结论

Agentic RAG代表了AI系统处理复杂、数据密集型任务的自然演变。通过采用循环交互模式、自主选择工具以及优化查询直到获得高质量结果，系统超越了静态的提示跟随，进入了更具适应性、上下文感知的决策制定。虽然仍然受到人类定义的基础设施和道德准则的限制，但这些智能体能力为企业和最终用户提供了更丰富、更动态、最终更有用的AI交互。

### 对Agentic RAG有更多问题？

加入[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者见面，参加办公时间并获得AI Agents问题的解答。

## 其他资源

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">使用Azure OpenAI Service实现检索增强生成（RAG）：了解如何将自己的数据与Azure OpenAI Service一起使用。这个Microsoft Learn模块提供了实现RAG的综合指南</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">使用Azure AI Foundry评估生成式AI应用程序：本文涵盖了在公开可用数据集上评估和比较模型，包括智能体AI应用程序和RAG架构</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">什么是Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG：基于智能体的检索增强生成完整指南 – 来自生成RAG的新闻</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG：通过查询重构和自查询增强您的RAG！Hugging Face开源AI食谱</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">向RAG添加智能体层</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">知识助手的未来：Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">如何构建Agentic RAG系统</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">使用Azure AI Foundry Agent Service扩展您的AI智能体</a>

### 学术论文

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement with Self-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG</a>

## 上一课

[工具使用设计模式](../04-tool-use/README.md)

## 下一课

[构建可信的AI智能体](../06-building-trustworthy-agents/README.md)