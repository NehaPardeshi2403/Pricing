import pandas as pd 

#reading csv files 
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")

#now merging the both files in sku because the data we need present in different files.
#here "on = "sku"" matcing rows usking sku column

data = pd.merge(products, sales, on = "sku", how="left")

#creating empty columns for old and new prices 
data["old_prices"] = 0.0
data["new_prices"] = 0.0

for index, row in data.iterrows(): #each row of our DataFrame
    old_price =row["current_price"]
    cost = row["cost_price"]
    stock = row["stock"]
    sold = row["quantity_sold"]

    new_price = old_price

    # rule 1: if stock is less than 20 and sold is more than 30
    if stock < 20 and sold >30:
        new_price= old_price * 1.15

    # rule 2 : Dead stock 
    elif stock > 200 and sold ==0:
        new_price = old_price * 0.7

    # rule 3 : Overstocked
    elif stock >100 and 20:
        new_price = old_price * 0.9

    #rule 4 : Minimun profit margin
    minimum_price =cost * 1.2
    if new_price < minimum_price:
        new_price = minimum_price

    #data table with new column
    data.at[index, "old_price"] = round(old_price, 2)
    data.at[index, "new_price"] = round(new_price, 2) 

    final = data[["sku", "old_price", "new_price"]] 
    final.to_csv("updated_price.csv", index=False) #csv file

print("updated prices saved in 'updated_prices.csv'")
print(final)