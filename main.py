# main.py

import pandas as pd
from agents.store_agent import StoreAgent
from agents.warehouse_agent import WarehouseAgent
from agents.pricing_agent import PricingAgent
import os

def load_demand_data(path):
    print("🔍 Loading demand data...")
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df

def main():
    # --- Demand Forecasting ---
    df = load_demand_data("data/demand_forecasting.csv")

    store_agent = StoreAgent()
    store_agent.train(df)

    df['Predicted Demand'] = store_agent.predict(df)
    demand_preds = df[['Store ID', 'Product ID', 'Predicted Demand']]

    warehouse_agent = WarehouseAgent()
    orders = warehouse_agent.replenish(demand_preds)

    print("📦 Suggested Replenishment Orders:")
    print(orders.head())

    os.makedirs("output", exist_ok=True)
    orders.to_csv("output/replenishment_orders.csv", index=False)

    print(f"✅ Total orders generated: {len(orders)}")

    # --- Pricing Optimization ---
    print("\n💰 Starting Pricing Optimization...")
    pricing_agent = PricingAgent()
    pricing_agent.train()

    suggestions = pricing_agent.suggest_optimal_prices()
    print("🧠 Optimal Pricing Suggestions:")
    print(suggestions.head())

    suggestions.to_csv("output/optimal_prices.csv", index=False)
    print(f"✅ Pricing optimization completed for {len(suggestions)} products.")

if __name__ == "__main__":
    main()
