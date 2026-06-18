import pandas as pd
import numpy as np
from datetime import datetime

# Load the dataset
print("Loading DataCo Supply Chain Dataset...")
df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding='latin-1')

print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Data Cleaning
print("\nCleaning data...")
df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'], errors='coerce')
df['shipping date (DateOrders)'] = pd.to_datetime(df['shipping date (DateOrders)'], errors='coerce')

# Calculate Key Metrics
print("\nCalculating supply chain KPIs...")

# 1. On-Time Delivery Rate
df['is_on_time'] = df['Days for shipping (real)'] <= df['Days for shipment (scheduled)']
on_time_rate = (df['is_on_time'].sum() / len(df)) * 100

# 2. Late Delivery Risk
late_delivery_count = df['Late_delivery_risk'].sum()
late_delivery_pct = (late_delivery_count / len(df)) * 100

# 3. Shipping Mode Analysis
shipping_mode_summary = df.groupby('Shipping Mode').agg({
    'Sales': ['sum', 'mean'],
    'Order Item Quantity': 'sum',
    'Days for shipping (real)': 'mean',
    'Order Item Profit Ratio': 'mean'
}).round(2)

# 4. Delivery Status Summary
delivery_status_summary = df['Delivery Status'].value_counts()

# 5. Product Category Performance
category_performance = df.groupby('Category Name').agg({
    'Sales': 'sum',
    'Order Item Profit Ratio': 'mean',
    'Days for shipping (real)': 'mean',
    'Late_delivery_risk': 'sum'
}).round(2)

# 6. Customer Segment Analysis
segment_analysis = df.groupby('Customer Segment').agg({
    'Sales': 'sum',
    'Benefit per order': 'mean',
    'Days for shipping (real)': 'mean',
    'Late_delivery_risk': 'sum'
}).round(2)

# 7. Market Performance
market_performance = df.groupby('Market').agg({
    'Sales': 'sum',
    'Order Id': 'count',
    'Days for shipping (real)': 'mean',
    'Late_delivery_risk': 'sum'
}).rename(columns={'Order Id': 'Total_Orders'})

# Create Summary Report
summary_metrics = {
    'Total Orders': [len(df)],
    'On-Time Delivery Rate (%)': [on_time_rate],
    'Late Delivery Risk (%)': [late_delivery_pct],
    'Total Sales': [df['Sales'].sum()],
    'Average Order Value': [df['Sales'].mean()],
    'Average Profit Ratio': [df['Order Item Profit Ratio'].mean()],
    'Average Shipping Days': [df['Days for shipping (real)'].mean()],
    'Total Profit': [df['Order Profit Per Order'].sum()]
}

summary_df = pd.DataFrame(summary_metrics)

# Print Summary to Console
print("\n" + "="*60)
print("SUPPLY CHAIN ANALYTICS SUMMARY")
print("="*60)
print(summary_df.to_string(index=False))
print("\nOn-Time Delivery Rate: {:.2f}%".format(on_time_rate))
print("Late Delivery Risk: {:.2f}%".format(late_delivery_pct))
print("="*60)

# Export to Excel with Multiple Sheets
output_file = 'output/supply_chain_analysis.xlsx'
print(f"\nExporting results to {output_file}...")

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    summary_df.to_excel(writer, sheet_name='Summary Metrics', index=False)
    shipping_mode_summary.to_excel(writer, sheet_name='Shipping Mode Analysis')
    delivery_status_summary.to_excel(writer, sheet_name='Delivery Status')
    category_performance.to_excel(writer, sheet_name='Category Performance')
    segment_analysis.to_excel(writer, sheet_name='Customer Segment Analysis')
    market_performance.to_excel(writer, sheet_name='Market Performance')

print(f"✓ Analysis complete! File saved to: {output_file}")
print("You can now import this Excel file into Power BI for visualization.")