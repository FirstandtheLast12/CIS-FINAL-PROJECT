import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Walmart_Sales.csv')
df = df.dropna()

print(df.describe().round(2))
print('Average Weekly Sales: ', df['Weekly_Sales'].mean().round(2))

plt.boxplot(df['Weekly_Sales'])
plt.title('Weekly_Sales')
plt.ylabel('Weekly_sales')
plt.show()