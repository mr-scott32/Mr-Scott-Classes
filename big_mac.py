import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('big_mac.csv')
df = pd.DataFrame(data)
print(data.dtypes)

print("Initial Data:")
print(data.head())


average_usd = data['dollar_price'].mean()
print("\nAverage US dollar price of a Big Mac since 2000: ", average_usd)



country_group = data.groupby('name')['dollar_price'].mean() * 1.53
print("\nAverage US dollar by country")
print(country_group)

plt.bar(country_group.index, country_group.values)
plt.xlabel('Country')
plt.ylabel('Average Price (AUD)')
plt.title('Average Big Mac Price Since 2000')
plt.show()


