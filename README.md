# signal-bus
A production-grade, multi-process quantitative trading framework featuring a decoupled signal bus and tripartite risk control.
# Signal-Bus: A Decoupled Quant Trading Infrastructure 🚀

A production-grade, multi-process quantitative trading framework featuring a decoupled signal bus and tripartite risk control. 

## 📖 Overview

Most open-source trading bots are highly coupled, monolithic scripts where a single API timeout or data lag can crash the entire system. **Signal-Bus** is different. It is a robust, production-ready trading infrastructure built strictly on the philosophy of **Separation of Concerns** and **Signal Bus Decoupling**.

Designed to survive in harsh live-trading environments, this framework splits the trading logic into completely isolated processes. This ensures that heavy computational tasks (like neural network inferences) never block real-time order book monitoring or micro-second execution.

## 🏛️ System Architecture


<img width="1248" height="934" alt="bc51f51af4f1c1a9b26d24e98ee4cb74" src="https://github.com/user-attachments/assets/06741eed-7d0c-42be-bc82-ee6726a98b8c" />

### Core Highlights

* **The Tripartite System (三权分立)**
  * 🧠 **Oracle (The Brain):** Focuses solely on macro-trend prediction (BULL/BEAR/CHOP). It analyzes historical features (e.g., minute-level K-lines, LSTM inferences) but remains oblivious to immediate entry timing.
  * 🛡️ **Sentinel/Radar (The Shield):** Provides real-time monitoring of order book depth, CVD, and Open Interest. It doesn't predict direction; it only calculates statistical anomalies and holds the absolute power to *veto* unsafe actions.
  * 🎯 **Sniper (The Trigger):** Focuses exclusively on micro-market fluctuations to pinpoint the mathematically optimal entry point.

* **Asynchronous Signal Bus (信号总线解耦)**
  Modules do not call each other directly. Instead, they communicate asynchronously via a file-based JSON signal bus (`signal_bus/`). If the Oracle crashes, the Sentinel and Executor continue to function safely. Hot-swapping a strategy is as simple as replacing a JSON writer.

* **Defense-in-Depth Execution (防御性执行器)**
  The Executor operates on a "Zero Trust" model. It enforces multi-layered gatekeeping, requiring consensus from the Oracle, Sentinel, and Sniper before firing any order. Built-in dual-track validation allows seamless parallel running of Paper Trading (V960) and Live Execution (V950).

## 🗂️ Directory Structure

This repository provides the core infrastructure. Users can plug their own trading logic into the respective modules.

```text
signal-bus/
│
├── signal_bus/               # The core communication hub (JSON files)
│   ├── v940.json             # Oracle signals
│   ├── sentinel.json         # Risk veto signals
│   └── swing_hunter.json     # Sniper entry signals
│
├── oracle/                   # Strategy & Prediction Models
│   └── dummy_model.py        # Example model (Replace with your own logic)
│
├── sentinel/                 # Risk & Orderbook Monitoring
│   └── health_checker.py     # System health and veto logic
│
├── executor/                 # Trade Execution
│   ├── v950_live.py          # Live trading engine
│   └── v960_paper.py         # Paper trading engine
│
└── requirements.txt          # Python dependencies
🚀 Quick Start
Clone the repository:

Bash
git clone [https://github.com/your-username/signal-bus.git](https://github.com/your-username/signal-bus.git)
cd signal-bus
Install dependencies:

Bash
pip install -r requirements.txt
Run the Dummy Infrastructure:
Start the signal bus and paper trading executor to see the multi-process communication in action:

Bash
python executor/v960_paper.py
