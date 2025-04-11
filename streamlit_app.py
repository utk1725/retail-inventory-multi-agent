import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Retail Inventory Optimization Dashboard", layout="wide")
st.title("📊 Multi-Agent Retail Optimization Dashboard")
st.markdown("Welcome to the hackathon project dashboard!")

# Load files
def load_file(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

# Load data
st.sidebar.header("📁 Data Files")
demand_df = load_file("output/optimal_prices.csv")  # or the correct name if this is demand
orders_df = load_file("output/replenishment_orders.csv")
pricing_df = load_file("output/optimal_prices.csv")  # <- assuming this is used for pricing suggestions


# Tabs
Tabs = st.tabs(["Predicted Demand", "Replenishment Orders", "Pricing Suggestions", "📈 Metrics"])

# Predicted Demand
with Tabs[0]:
    st.subheader("📦 Predicted Demand")
    if not demand_df.empty:
        st.dataframe(demand_df, use_container_width=True)
    else:
        st.warning("Predicted demand file not found.")

# Warehouse Orders
with Tabs[1]:
    st.subheader("🏬 Replenishment Orders")
    if not orders_df.empty:
        st.dataframe(orders_df, use_container_width=True)
    else:
        st.warning("Replenishment orders file not found.")

# Pricing Suggestions
with Tabs[2]:
    st.subheader("💰 Pricing Optimization Suggestions")
    if not pricing_df.empty:
        st.dataframe(pricing_df, use_container_width=True)
    else:
        st.warning("Pricing suggestions file not found.")

# Metrics Tab
with Tabs[3]:
    st.subheader("📈 Evaluation Metrics")
    if not pricing_df.empty:
        total_expected_revenue = pricing_df['Expected Revenue'].sum()
        total_current_revenue = (pricing_df['Current Price'] * pricing_df['Expected Revenue'] / pricing_df['Optimal Price']).sum()
        uplift = total_expected_revenue - total_current_revenue

        st.metric("Total Expected Revenue", f"₹ {total_expected_revenue:,.2f}")
        st.metric("Total Current Revenue (Est.)", f"₹ {total_current_revenue:,.2f}")
        st.metric("💹 Revenue Uplift", f"₹ {uplift:,.2f}")
    else:
        st.warning("No pricing data to evaluate uplift.")
