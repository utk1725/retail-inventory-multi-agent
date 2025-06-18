
---

```markdown
# 🛒 Retail Inventory Multi-Agent System

A Python-based multi-agent system for **retail inventory management**. This project leverages intelligent agents to automate **demand forecasting**, **inventory replenishment**, and **pricing optimization** to streamline operations in a retail setting.

---

## 🚀 Features

- 🔍 **Demand Forecasting** using machine learning
- 📦 **Replenishment Planning** based on forecasted demand
- 💰 **Dynamic Pricing Optimization** for profitability
- 📊 Streamlit-based interactive dashboard (via `streamlit_app.py`)

---

## 🧠 Agents

| Agent            | Description |
|------------------|-------------|
| `StoreAgent`     | Predicts future product demand using historical data |
| `WarehouseAgent` | Generates optimal replenishment plans for inventory restocking |
| `PricingAgent`   | Recommends optimal product prices using pricing models |

---

## 📁 Project Structure

```

.
├── agents/               # Contains agent implementations (Store, Warehouse, Pricing)

├── data/                 # CSV input files (e.g., demand\_forecasting.csv)

├── models/               # Trained ML models (optional)

├── output/               # Output CSVs (replenishment orders, pricing suggestions)

├── utils/                # Helper functions

├── main.py               # Main entry point script

├── streamlit\_app.py      # Streamlit dashboard for visualization

├── requirements.txt      # Python dependencies

└── README.md             # Project documentation

````

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/utk1725/retail-inventory-multi-agent.git
   cd retail-inventory-multi-agent
````

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Run the main backend logic:

```bash
python main.py
```

### Start the Streamlit dashboard:

```bash
streamlit run streamlit_app.py
```

---

## 📈 Sample Outputs

* `output/replenishment_orders.csv` — Suggested restocking orders per product-store combination.
* `output/optimal_prices.csv` — Optimized product pricing based on predicted demand.

---

## ✅ Requirements

* Python 3.8+
* pandas, scikit-learn, streamlit, numpy (see `requirements.txt` for full list)

---

## 📌 License

This project is licensed for academic and personal use only.

---

## 📬 Contact

**Utkarsh Singh**

📧 Email: [utkarshthakur17022002@gmail.com](mailto:utkarshthakur17022002@gmail.com)

🔗 [LinkedIn](https://www.linkedin.com/in/utkarshsingh1702)


---

 
