[![Multi-Agent Design](./images/lesson-9-thumbnail.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(点击上方图片观看本课程视频)_  
# AI 代理中的元认知

## 介绍

欢迎学习 AI 代理中的元认知课程！本章专为对 AI 代理如何思考自身思考过程感兴趣的初学者设计。完成本课程后，您将理解关键概念，并掌握在 AI 代理设计中应用元认知的实用示例。

## 学习目标

完成本课程后，您将能够：

1. 理解代理定义中推理循环的含义。
2. 使用规划和评估技术帮助自我纠正的代理。
3. 创建能够通过操作代码完成任务的代理。

## 元认知介绍

元认知指的是涉及思考自身思考过程的高阶认知过程。对于 AI 代理来说，这意味着能够基于自我意识和过去经验来评估和调整其行为。元认知，或"思考思考"，是开发智能体 AI 系统的重要概念。它涉及 AI 系统意识到自己的内部过程，并能够监控、调节和适当地调整其行为。就像我们在观察环境或看待问题时所做的那样。这种自我意识可以帮助 AI 系统做出更好的决策，识别错误，并随着时间的推移提高其性能 - 这又回到了图灵测试以及关于 AI 是否会接管的辩论。

在智能体 AI 系统的背景下，元认知可以帮助解决几个挑战，例如：
- 透明度：确保 AI 系统能够解释其推理和决策过程。
- 推理：增强 AI 系统综合信息并做出合理决策的能力。
- 适应：允许 AI 系统适应新环境和变化的条件。
- 感知：提高 AI 系统识别和解释来自环境的数据的准确性。

### 什么是元认知？

元认知，或"思考思考"，是一种涉及自我意识和自我调节认知过程的高阶认知过程。在 AI 领域，元认知使代理能够评估和调整其策略和行为，从而提高问题解决和决策能力。通过理解元认知，您可以设计不仅更智能，而且更具适应性和效率的 AI 代理。在真正的元认知中，您会看到 AI 明确地对自己的推理进行推理。

示例："我优先考虑更便宜的航班，因为...我可能错过了直飞航班，让我重新检查一下。"。
跟踪它如何或为什么选择特定路线。
- 注意到它犯了错误，因为它过度依赖上次的用户偏好，所以它修改了决策策略，而不仅仅是最终推荐。
- 诊断模式，例如："每当我看到用户提到'太拥挤'时，我不仅应该移除某些景点，还应该反映出如果我总是按受欢迎程度排名，我的'顶级景点'选择方法是有缺陷的。"

### AI 代理中元认知的重要性

元认知在 AI 代理设计中发挥着关键作用，原因如下：

![元认知的重要性](./images/importance-of-metacognition.png)

- 自我反思：代理可以评估自己的性能并识别需要改进的领域。
- 适应性：代理可以根据过去的经验和变化的环境修改其策略。
- 错误纠正：代理可以自主检测和纠正错误，从而获得更准确的结果。
- 资源管理：代理可以通过规划和评估其行为来优化资源使用，例如时间和计算能力。

## AI 代理的组成部分

在深入探讨元认知过程之前，了解 AI 代理的基本组成部分至关重要。AI 代理通常包括：

- 角色：代理的个性和特征，定义了它如何与用户交互。
- 工具：代理可以执行的功能和能力。
- 技能：代理拥有的知识和专业知识。

这些组件共同创建了一个可以执行特定任务的"专业单元"。

**示例**：
考虑一个旅行代理，该代理服务不仅计划您的假期，还根据实时数据和过去的客户旅程经验调整其路径。

### 示例：旅行代理服务中的元认知

想象您正在设计一个由 AI 驱动的旅行代理服务。这个名为"旅行代理"的代理帮助用户规划他们的假期。为了融入元认知，旅行代理需要基于自我意识和过去经验来评估和调整其行为。以下是元认知如何发挥作用的方式：

#### 当前任务

当前任务是帮助用户规划巴黎之旅。

#### 完成任务的步骤

1. **收集用户偏好**：询问用户关于他们的旅行日期、预算、兴趣（例如博物馆、美食、购物）和任何特定要求。
2. **检索信息**：搜索符合用户偏好的航班选项、住宿、景点和餐厅。
3. **生成推荐**：提供包含航班详情、酒店预订和建议活动的个性化行程。
4. **根据反馈调整**：向用户询问对推荐的反馈并进行必要的调整。

#### 所需资源

- 访问航班和酒店预订数据库。
- 关于巴黎景点和餐厅的信息。
- 来自之前互动的用户反馈数据。

#### 经验和自我反思

旅行代理使用元认知来评估其性能并从过去的经验中学习。例如：

1. **分析用户反馈**：旅行代理审查用户反馈，以确定哪些推荐受到好评，哪些不受好评。它相应地调整未来的建议。
2. **适应性**：如果用户之前提到不喜欢拥挤的地方，旅行代理将来会避免在高峰时段推荐热门旅游景点。
3. **错误纠正**：如果旅行代理在过去的预订中犯了错误，例如推荐了已订满的酒店，它会学会在推荐前更严格地检查可用性。

#### 开发者实用示例

以下是旅行代理代码在融入元认知时的简化示例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 根据偏好搜索航班、酒店和景点
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # 分析反馈并调整未来的推荐
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 示例用法
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Top Museums in Paris:", museums)
```

**工具示例：**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### 评估相关性

评估相关性是 AI 代理性能的关键方面。它确保代理检索和生成的信息对用户来说是适当、准确和有用的。让我们探讨如何评估 AI 代理中的相关性，包括实用示例和技术。

#### 评估相关性的关键概念

1. **上下文感知**：
   - 代理必须理解用户查询的上下文，以检索和生成相关信息。
   - 示例：如果用户询问"巴黎最好的餐厅"，代理应考虑用户的偏好，如菜系类型和预算。

2. **准确性**：
   - 代理提供的信息应该是事实正确且最新的。
   - 示例：推荐当前营业且评价良好的餐厅，而不是过时或已关闭的选项。

3. **用户意图**：
   - 代理应推断用户查询背后的意图，以提供最相关的信息。
   - 示例：如果用户询问"经济型酒店"，代理应优先考虑价格实惠的选项。

4. **反馈循环**：
   - 持续收集和分析用户反馈有助于代理完善其相关性评估过程。
   - 示例：将用户对先前推荐的评分和反馈纳入，以改进未来的响应。

#### 评估相关性的实用技术

1. **相关性评分**：
   - 根据项目与用户查询和偏好的匹配程度，为每个检索项目分配相关性评分。
   - 示例：

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **过滤和排序**：
   - 过滤掉不相关的项目，并根据它们的相关性评分对剩余项目进行排序。
   - 示例：

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 返回前 10 个相关项目
     ```

3. **自然语言处理（NLP）**：
   - 使用 NLP 技术理解和解释用户提供的自然语言查询。这包括实体识别、情感分析和查询解析等任务。
   - 示例：

     ```python
     def process_query(query):
         # 使用 NLP 从用户查询中提取关键信息
         processed_query = nlp(query)
         return processed_query
     ```

4. **用户反馈集成**：
   - 收集用户对推荐的反馈，并使用它来改进未来的相关性评估。
   - 示例：

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### 示例：旅行代理中的相关性评估

以下是旅行代理如何评估旅行推荐相关性的实用示例：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # 返回前 10 个相关项目

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# 示例用法
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### 带有意图的搜索

带有意图的搜索涉及理解和解释用户查询背后的目的或目标，以检索和生成最相关和有用的信息。这种方法超越了简单的关键词匹配，专注于理解用户的实际需求和上下文。

#### 带有意图的搜索的关键概念

1. **理解用户意图**：
   - 用户意图可以分为三种主要类型：信息性、导航性和交易性。
     - **信息性意图**：用户寻求有关某个主题的信息（例如，"巴黎最好的博物馆是什么？"）。
     - **导航性意图**：用户想要导航到特定网站或页面（例如，"卢浮宫博物馆官方网站"）。
     - **交易性意图**：用户旨在执行交易，例如预订航班或进行购买（例如，"预订前往巴黎的航班"）。

2. **上下文感知**：
   - 分析用户查询的上下文有助于准确识别他们的意图。这包括考虑以前的互动、用户偏好和当前查询的具体细节。

3. **自然语言处理（NLP）**：
   - NLP 技术用于理解和解释用户提供的自然语言查询。这包括实体识别、情感分析和查询解析等任务。

4. **个性化**：
   - 基于用户的历史、偏好和反馈个性化搜索结果，增强检索信息的相关性。

#### 实用示例：旅行代理中的带有意图的搜索

让我们以旅行代理为例，看看如何实现带有意图的搜索。

1. **收集用户偏好**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **理解用户意图**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **上下文感知**

   ```python
   def analyze_context(query, user_history):
       # 结合当前查询和用户历史来理解上下文
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **搜索和个性化结果**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # 信息性意图的示例搜索逻辑
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # 导航性意图的示例搜索逻辑
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # 交易性意图的示例搜索逻辑
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # 示例个性化逻辑
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # 返回前 10 个个性化结果
   ```

5. **示例用法**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. 将代码生成为工具

代码生成代理使用 AI 模型编写和执行代码，解决复杂问题并自动化任务。

### 代码生成代理

代码生成代理使用生成式 AI 模型编写和执行代码。这些代理可以通过在各种编程语言中生成和运行代码来解决复杂问题、自动化任务并提供有价值的见解。

#### 实际应用

1. **自动代码生成**：为特定任务生成代码片段，例如数据分析、网页抓取或机器学习。
2. **作为 RAG 的 SQL**：使用 SQL 查询从数据库中检索和操作数据。
3. **问题解决**：创建和执行代码来解决特定问题，例如优化算法或分析数据。

#### 示例：数据分析的代码生成代理

想象你正在设计一个代码生成代理。它可能如下工作：

1. **任务**：分析数据集以识别趋势和模式。
2. **步骤**：
   - 将数据集加载到数据分析工具中。
   - 生成 SQL 查询以过滤和聚合数据。
   - 执行查询并检索结果。
   - 使用结果生成可视化和见解。
3. **所需资源**：访问数据集、数据分析工具和 SQL 功能。
4. **经验**：使用过去的分析结果来提高未来分析的准确性和相关性。

### 示例：旅行代理的代码生成代理

在这个示例中，我们将设计一个代码生成代理，即旅行代理，通过生成和执行代码来帮助用户规划旅行。这个代理可以处理诸如获取旅行选项、过滤结果和使用生成式 AI 编译行程等任务。

#### 代码生成代理概述

1. **收集用户偏好**：收集用户输入，如目的地、旅行日期、预算和兴趣。
2. **生成代码以获取数据**：生成代码片段以检索有关航班、酒店和景点的数据。
3. **执行生成的代码**：运行生成的代码以获取实时信息。
4. **生成行程**：将获取的数据编译成个性化旅行计划。
5. **根据反馈调整**：接收用户反馈并在必要时重新生成代码以优化结果。

#### 分步实现

1. **收集用户偏好**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **生成代码以获取数据**

   ```python
   def generate_code_to_fetch_data(preferences):
       # 示例：生成代码以根据用户偏好搜索航班
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 示例：生成代码以搜索酒店
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **执行生成的代码**

   ```python
   def execute_code(code):
       # 使用 exec 执行生成的代码
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **生成行程**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **根据反馈调整**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # 根据用户反馈调整偏好
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # 使用更新后的偏好重新生成并执行代码
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### 利用环境感知和推理

基于表的模式确实可以通过利用环境感知和推理来增强查询生成过程。

以下是如何实现这一点的示例：

1. **理解模式**：系统将理解表的模式，并使用此信息来指导查询生成。
2. **根据反馈调整**：系统将根据反馈调整用户偏好，并推理出模式中的哪些字段需要更新。
3. **生成和执行查询**：系统将生成并执行查询，以根据新偏好获取更新的航班和酒店数据。

以下是包含这些概念的更新后的 Python 代码示例：

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # 根据用户反馈调整偏好
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # 基于模式推理以调整其他相关偏好
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # 根据模式和反馈调整偏好的自定义逻辑
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 基于更新的偏好生成获取航班数据的代码
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 基于更新的偏好生成获取酒店数据的代码
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # 模拟代码执行并返回模拟数据
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # 基于航班、酒店和景点生成行程
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 示例模式
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 示例用法
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 使用更新后的偏好重新生成并执行代码
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 解释 - 基于反馈的预订

1. **模式感知**：`schema` 字典定义了如何根据反馈调整偏好。它包括 `favorites` 和 `avoid` 等字段，以及相应的调整。
2. **调整偏好（`adjust_based_on_feedback` 方法）**：此方法根据用户反馈和模式调整偏好。
3. **基于环境的调整（`adjust_based_on_environment` 方法）**：此方法根据模式和反馈自定义调整。
4. **生成和执行查询**：系统生成代码以根据调整后的偏好获取更新的航班和酒店数据，并模拟执行这些查询。
5. **生成行程**：系统根据新的航班、酒店和景点数据创建更新的行程。

通过使系统具有环境感知能力并基于模式进行推理，它可以生成更准确和相关的查询，从而获得更好的旅行推荐和更个性化的用户体验。

### 将 SQL 用作检索增强生成（RAG）技术

SQL（结构化查询语言）是与数据库交互的强大工具。当作为检索增强生成（RAG）方法的一部分使用时，SQL 可以从数据库中检索相关数据，以告知和生成 AI 代理中的响应或操作。让我们探讨如何在旅行代理的上下文中将 SQL 用作 RAG 技术。

#### 关键概念

1. **数据库交互**：
   - SQL 用于查询数据库、检索相关信息和操作数据。
   - 示例：从旅行数据库中获取航班详情、酒店信息和景点。

2. **与 RAG 集成**：
   - SQL 查询基于用户输入和偏好生成。
   - 检索到的数据随后用于生成个性化推荐或操作。

3. **动态查询生成**：
   - AI 代理根据上下文和用户需求生成动态 SQL 查询。
   - 示例：自定义 SQL 查询以根据预算、日期和兴趣过滤结果。

#### 应用

- **自动代码生成**：为特定任务生成代码片段。
- **作为 RAG 的 SQL**：使用 SQL 查询操作数据。
- **问题解决**：创建和执行代码来解决问题。

**示例**：
数据分析代理：

1. **任务**：分析数据集以发现趋势。
2. **步骤**：
   - 加载数据集。
   - 生成 SQL 查询以过滤数据。
   - 执行查询并检索结果。
   - 生成可视化和见解。
3. **资源**：数据集访问、SQL 功能。
4. **经验**：使用过去的结果改进未来的分析。

#### 实用示例：在旅行代理中使用 SQL

1. **收集用户偏好**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **生成 SQL 查询**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **执行 SQL 查询**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **生成推荐**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### 示例 SQL 查询

1. **航班查询**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **酒店查询**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **景点查询**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

通过将 SQL 作为检索增强生成（RAG）技术的一部分，像旅行代理这样的 AI 代理可以动态检索和利用相关数据，以提供准确和个性化的推荐。

### 元认知示例

为了演示元认知的实现，让我们创建一个简单的代理，在解决问题时*反思其决策过程*。对于这个示例，我们将构建一个系统，其中代理尝试优化酒店的选择，但随后评估自己的推理并在犯错误或做出次优选择时调整策略。

我们将使用一个基本示例来模拟这一点，其中代理根据价格和质量的组合选择酒店，但它会"反思"自己的决策并相应地调整。

#### 这如何说明元认知：

1. **初始决策**：代理将选择最便宜的酒店，而不了解质量影响。
2. **反思和评估**：在初始选择后，代理将检查酒店是否是使用用户反馈的"坏"选择。如果它发现酒店质量太低，它会反思自己的推理。
3. **调整策略**：代理根据其反思调整策略，从"最便宜"切换到"最高质量"，从而在未来的迭代中改进其决策过程。

以下是一个示例：

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 存储以前选择的酒店
        self.corrected_choices = []  # 存储更正的选择
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # 可用策略

    def recommend_hotel(self, hotels, strategy):
        """
        根据选择的策略推荐酒店。
        策略可以是'cheapest'或'highest_quality'。
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        反思最后做出的选择，并决定代理是否应该调整其策略。
        代理考虑先前的选择是否导致了不良结果。
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # 假设我们有一些用户反馈，告诉我们最后一个选择是好是坏
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 如果先前的选择不令人满意，则调整策略
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        根据酒店属性模拟用户反馈。
        为简单起见，假设如果酒店太便宜，反馈是"bad"。
        如果酒店质量低于7，反馈是"bad"。
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# 模拟酒店列表（价格和质量）
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# 创建代理
agent = HotelRecommendationAgent()

# 步骤1：代理使用"cheapest"策略推荐酒店
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 步骤2：代理反思选择并在必要时调整策略
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 步骤3：代理再次推荐，这次使用调整后的策略
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### 代理的元认知能力

这里的关键是代理的能力：
- 评估其先前的选择和决策过程。
- 基于该反思调整其策略，即行动中的元认知。

这是一种简单的元认知形式，其中系统能够基于内部反馈调整其推理过程。

### 结论

元认知是一种强大的工具，可以显著增强 AI 代理的能力。通过纳入元认知过程，您可以设计更智能、适应性更强、更高效的代理。使用其他资源进一步探索 AI 代理中元认知的迷人世界。

### 对元认知设计模式还有更多问题？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) 与其他学习者见面，参加办公时间并获得您的 AI 代理问题的答案。

## 上一课

[多代理设计模式](../08-multi-agent/README.md)

## 下一课

[生产中的 AI 代理](../10-ai-agents-production/README.md)