import json
import time
import random
import os

SIGNAL_DIR = "signal_bus"
os.makedirs(SIGNAL_DIR, exist_ok=True)

print("🛡️ [Sentinel] Health Checker Started. Monitoring orderbook anomalies...")

while True:
    # 模拟盘口监控：80% 概率安全，20% 概率检测到异常并一票否决
    is_safe = random.random() > 0.2
    reason = "Normal Condition" if is_safe else "High CVD / Spread Anomaly Detected!"
    
    data = {
        "timestamp": time.time(),
        "symbol": "BTC/USDT",
        "safe_to_trade": is_safe,
        "reason": reason
    }
    
    # 写入哨兵风控信号
    file_path = os.path.join(SIGNAL_DIR, "sentinel.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
        
    status_icon = "✅" if is_safe else "⛔ VETO"
    print(f"🛡️ [Sentinel] Status: {status_icon} | {reason}")
    
    # 雷达需要高频监控，每 2 秒更新一次状态
    time.sleep(2)
