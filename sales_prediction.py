# given the following data on the amount of advertising and the sales for the past 10 years can u use linear reggression to predict the sales for the next year?
# year - 2013 - 2014 - 2015 - 2016 - 2017  (2018)
# adversting x - 100000 -120000 - 140000 - 160000 - 220000
# sales y - 100000 - 120000 - 140000 - 160000 - 220000

from statistics import mean
import matplotlib.pyplot as plt

year = [2013, 2014, 2015, 2016, 2017]
adv = [100000, 120000, 140000, 160000, 220000]
sales = [100000, 120000, 140000, 160000, 220000]

years_mean = mean(year)
advertising_mean = mean(adv)
sales_mean = mean(sales)

years_dev = []
sales_dev = []
product_dev = []
square_dev_years = []
square_dev_sales = []

for i in range(len(adv)):
    years_dev.append(year[i] - years_mean)
    sales_dev.append(adv[i] - sales_mean)  # Corrected variable name
    product_dev.append(years_dev[i] * sales_dev[i])
    square_dev_years.append(years_dev[i] ** 2)
    square_dev_sales.append(sales_dev[i] ** 2)

sum_square_dev_years = sum(square_dev_years)
sum_square_dev_sales = sum(square_dev_sales)
sum_product_dev = sum(product_dev)

m = sum_product_dev / sum_square_dev_years
b = sales_mean - (m * years_mean)

X = int(input("Enter the year: "))
Y = m * X + b
print(f'Predicted sales in {X} is {Y}')

plt.scatter(year, adv, label='Actual Sales')  # Corrected variable name
plt.plot(year, [m * x + b for x in year], color='red', label='Linear Regression')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Linear Regression Example')
plt.legend()
plt.show()

