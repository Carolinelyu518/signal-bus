# signal-bus
A production-grade, multi-process quantitative trading framework featuring a decoupled signal bus and tripartite risk control.
<img width="1248" height="934" alt="bc51f51af4f1c1a9b26d24e98ee4cb74" src="https://github.com/user-attachments/assets/e2854d1b-bb90-456d-842f-0211b32692bd" />
A Decoupled, Multi-Process Quant Trading Infrastructure

Overview
Most open-source trading bots are highly coupled, monolithic scripts where a single API timeout can crash the entire system. Signal Bus is different. It is a robust, production-ready trading infrastructure built strictly on the philosophy of Separation of Concerns and Signal Bus Decoupling.

Designed to survive in harsh live-trading environments, this framework splits the trading logic into completely isolated processes. This ensures that heavy computational tasks (like neural network inferences) never block real-time order book monitoring or micro-second execution.

Core Architecture Highlights

🏛️ The Tripartite System 

🧠 Oracle (The Brain): Focuses solely on macro-trend prediction (BULL/BEAR/CHOP). It analyzes historical features but remains oblivious to immediate entry timing.

🛡️ Sentinel/Radar (The Shield): Provides real-time monitoring of order book depth, CVD, and Open Interest. It doesn't predict direction; it only calculates statistical anomalies and holds the absolute power to veto unsafe actions.

🎯 Sniper (The Trigger): Focuses exclusively on micro-market fluctuations to pinpoint the mathematically optimal entry point.

🔌 Asynchronous Signal Bus 
Modules do not call each other directly. Instead, they communicate asynchronously via a file-based JSON signal bus (signal_bus/). If the Oracle crashes, the Sentinel and Executor continue to function safely. Hot-swapping a strategy is as simple as replacing a JSON writer.

🏰 Defense-in-Depth Execution 
The Executor operates on a "Zero Trust" model. It enforces multi-layered gatekeeping, requiring consensus from the Oracle, Sentinel, and Sniper before firing any order. Built-in dual-track validation allows seamless parallel running of Paper Trading (xxxname) and Live Execution (xxxname).
