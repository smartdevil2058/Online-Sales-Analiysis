import pandas as pd
df = pd.read_csv('E-commerce data analysis\Online_Sales_Data.csv')


# data understandeing

print(df.head(3))
print(df.tail(3))
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)


#data cleaning 

print(df.isnull().sum())


#each region' transection and their payment method
df.groupby(['Region', 'Payment Method']).size()

#highest unit price
max_unit_price = df.loc[df['Unit Price'].idxmax()]
print(max_unit_price)

#highest unit sold
max_unit_sold = df.loc[df['Units Sold'].idxmax()]
print(max_unit_sold)

# highest unit sold
max_Total_Revenue = df.loc[df['Total Revenue'].idxmax()]
print(max_Total_Revenue)

#Average unit price
avg_price = df['Unit Price'].mean()
print(avg_price.mean())

#profit column
df['Profit'] = df['Total Revenue'] - df['Unit Price'] * df['Units Sold']


##Most sold Category 
filterd_category = df['Product Category'].value_counts()
print(filterd_category)


#Top 10  Product in total Revenue
top10 = df.nlargest(10, 'Total Revenue') 
print(top10)

#Region wise top revenue
region_wise = df.groupby('Region')['Total Revenue'].sum().sort_values(ascending=False)
print(region_wise)


#Cate gory and region wise 
category_wise = df.groupby(['Product Category', 'Region'])['Total Revenue'].sum().sort_values(ascending=False)
print(category_wise)

#profit according to the product name
products_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)
print(products_profit)

#profit according to the Product Category
df.groupby('Product Category')['Profit'].sum().sort_values(ascending=False)

#Month analysis
df['Date'] = pd.to_datetime(df['Date'])
df.groupby(df['Date'].dt.month)['Total Revenue'].sum().sort_values(ascending=False)


#total revenue and profit
Total_revenue = df['Total Revenue'].sum()
print(Total_revenue)
Total_profit = df['Profit'].sum()
print(Total_profit)

df.to_csv('final_online_sales_data.csv', index=False)