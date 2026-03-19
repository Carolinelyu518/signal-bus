import json
import time
import random
import os

# 确保信号总线文件夹存在
SIGNAL_DIR = "signal_bus"
os.makedirs(SIGNAL_DIR, exist_ok=True)

print("🧠 [Oracle] Dummy Model Started. Analyzing macro trends...")

while True:
    # 模拟神经网络推理，随机生成看涨、看跌或震荡信号
    signal = random.choice(["BULL", "BEAR", "CHOP"])
    confidence = round(random.uniform(0.60, 0.99), 2)
    
    data = {
        "timestamp": time.time(),
        "symbol": "BTC/USDT",
        "direction": signal,
        "confidence": confidence,
        "source": "Oracle_v940"
    }
    
    # 写入信号总线 (V940.json)
    file_path = os.path.join(SIGNAL_DIR, "v940.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
        
    print(f"🧠 [Oracle] Broadcasted: {signal} (Confidence: {confidence})")
    
    # 模拟计算耗时，每 5 秒输出一次大势
    time.sleep(5)
