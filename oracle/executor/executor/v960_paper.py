import json
import time
import os

SIGNAL_DIR = "signal_bus"

def read_json_signal(filename):
    """安全读取信号总线中的 JSON 文件"""
    filepath = os.path.join(SIGNAL_DIR, filename)
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

print("⚙️ [Executor] V960 Paper Trading Engine Started.")
print("⚙️ [Executor] Waiting for multi-process signals to align...\n")

while True:
    oracle_data = read_json_signal("v940.json")
    sentinel_data = read_json_signal("sentinel.json")
    
    if not oracle_data or not sentinel_data:
        time.sleep(1)
        continue

    print("-" * 50)
    # 第一道门禁：检查 Sentinel 哨兵是否亮红灯 (一票否决)
    if not sentinel_data.get("safe_to_trade"):
        print(f"❌ [ACTION REJECTED] Sentinel Veto: {sentinel_data.get('reason')}")
    else:
        # 第二道门禁：读取 Oracle 宏观方向
        direction = oracle_data.get("direction")
        symbol = oracle_data.get("symbol")
        
        if direction in ["BULL", "BEAR"]:
            print(f"🚀 [PAPER TRADE EXECUTED] Opening {direction} position on {symbol}!")
            print(f"    └─ Backed by Oracle Confidence: {oracle_data.get('confidence')}")
        else:
            print(f"⏸️ [HOLD] Market is choppy. Oracle says: {direction}")

    # 执行器独立运转，每 3 秒评估一次全局状态
    time.sleep(3)
