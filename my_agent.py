import random

# 1. 模拟 AI 预测：明天能卖出多少件货？
def forecast_sales():
    prediction = random.randint(50, 150) # 随机生成一个50到150之间的数
    return prediction

# 2. 模拟 AI 决策：根据预测，我们要干什么？
def ai_decision_agent():
    predicted_demand = forecast_sales()
    current_inventory = 100 # 假设现在仓库有100件货
    
    print(f"📊 预测报告：明天预计需求 {predicted_demand} 件")
    print(f"📦 库存现状：当前仓库剩余 {current_inventory} 件")
    
    if predicted_demand > current_inventory:
        print("💡 AI 决策：【需要补货！】预测需求大于库存。")
    else:
        print("💡 AI 决策：【暂不补货】库存还够用。")

# 运行 AI
if __name__ == "__main__":
    ai_decision_agent()
