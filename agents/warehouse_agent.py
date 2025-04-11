# agents/warehouse_agent.py

import pandas as pd

class WarehouseAgent:
    def __init__(self, inventory_path="data/inventory_monitoring.csv"):
        self.inventory_df = pd.read_csv(inventory_path)
        self.inventory_df.columns = self.inventory_df.columns.str.strip()

        # Fill missing warehouse IDs with a default based on Store ID
        if 'Warehouse ID' not in self.inventory_df.columns:
            self.inventory_df['Warehouse ID'] = self.inventory_df['Store ID'].apply(
                lambda x: f"W{int(x) % 5 + 1}"
            )
        else:
            self.inventory_df['Warehouse ID'] = self.inventory_df['Warehouse ID'].fillna(
                self.inventory_df['Store ID'].apply(lambda x: f"W{int(x) % 5 + 1}")
            )

    def replenish(self, predicted_demand_df):
        orders = []

        for _, row in predicted_demand_df.iterrows():
            store_id = row['Store ID']
            product_id = row['Product ID']
            predicted_demand = row['Predicted Demand']

            inv = self.inventory_df[
                (self.inventory_df['Store ID'] == store_id) &
                (self.inventory_df['Product ID'] == product_id)
            ]

            if inv.empty:
                continue

            current_stock = inv.iloc[0].get('Stock Levels', 0)
            safety_stock = inv.iloc[0].get('Reorder Point', 0)

            reorder_qty = max(0, predicted_demand + safety_stock - current_stock)

            if reorder_qty > 0:
                orders.append({
                    "Warehouse ID": inv.iloc[0]['Warehouse ID'],
                    "Store ID": store_id,
                    "Product ID": product_id,
                    "Reorder Quantity": int(reorder_qty)
                })

        return pd.DataFrame(orders)
