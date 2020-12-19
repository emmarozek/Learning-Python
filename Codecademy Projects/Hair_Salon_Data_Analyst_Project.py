# The name of each hairstyle offered:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
# The price of each hairstyle in hairstyles:
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# The number of each hairstyle in hairstyles that was purchased last week:
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
  
average_price = total_price/len(prices)
print("Average Haircut Price: " +str(average_price))

new_prices = [price - 5 for price in prices]
print("New Prices: " +str(new_prices))

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: " +str(total_revenue))

average_daily_revenue = total_revenue/7
print("Average Daily Revenue: " +str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices) - 1) if new_prices[i] < 30]
print("Cuts Under $30: " +str(cuts_under_30))
