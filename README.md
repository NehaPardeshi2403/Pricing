## Files contains 
1. 'pricing_script.py' = main script.
2. 'products.csv' = Current prices, stock, and cost.
3. 'sales.csv' = Last 30 days of product data.
4. 'updated_price.csv'= Output file with updated pricing.
5. 'README.md' = Project overview.

## Logic Used

1. Low Stock and High Demand:
 - stock <20 and quantity_sold > 30 --> increase price by 15 %
2. Dead stock:
 - stock . 200 and quantity_sold == 0 --> decrease price by 30%
3. Overstocked Inventory:
 - stock > 100 and quantity_sold < 20 --> decrease price by 10%
4. Miniimun Profit Rule(Always Applied):
 - Final price ≥ 120% of cost price.
 - If not, reset to cost_price * 1.2

## How to RunS
1. Install python
2. Place all files in the same folder
3. Run script 
    - python pricing_script.py