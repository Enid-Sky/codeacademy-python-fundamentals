
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
# PRICE

#Find the average price of a haircut
total_price = 0
for price in prices:
  total_price += price
num_of_prices = len(prices)
average_price = round(total_price / num_of_prices)
print(f"Average Haircut Price: {average_price}")

# use list comprehension to slash price by $5
new_prices = [price - 5 for price in prices]
print(new_prices)

# REVENUE

# Find how much revenue was brought in last week

total_revenue = 0
# set the length
for i in range(len(last_week)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: {total_revenue}")

#Find average daily revenue
average_daily_revenue = total_revenue / len(last_week)
print(average_daily_revenue)

# use list comprehension to create a list that displays all haircuts under 30. 

cuts_under_30 = [
  hairstyles[i] 
  for i in range(len(hairstyles)) 
  if new_prices[i] < 30
  ]

print(cuts_under_30)

