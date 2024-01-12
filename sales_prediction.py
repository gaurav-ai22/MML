# given the following data on the amount of advertising and the sales for the past 10 years can u use linear reggression to predict the sales for the next year?
# year - 2013 - 2014 - 2015 - 2016 - 2017  (2018)
# adversting x - 100000 -120000 - 140000 - 160000 - 220000
# sales y - 100000 - 120000 - 140000 - 160000 - 220000

import matplotlib.pyplot as plt 

ads = [100000,120000,140000,160000,220000]
sales = [100000,120000,140000,160000,220000]

mean_ads_x = sum(ads)//len(ads)
mean_sales_y = sum(sales)//len(sales)

devi_x = []
devi_y = []


for x in ads:
    devi_x.append((x - mean_ads_x))
for y in sales:
    devi_y.append((y - mean_sales_y))

print(f"Deviation of X:\n{devi_x}")
print(f"Deviation of Y:\n{devi_y}")

product = []
for i in range(len(devi_x)):
    # produc = d[x] * d[y]
    product.append((devi_x[i] * devi_y[i]))

sqr_of_devi_of_x = []
for x in devi_x:
    sqr_of_devi_of_x.append((x**2))

sum_of_product_of_devi = sum(product)
sum_of_sqr_of_devi_of_x = sum(sqr_of_devi_of_x)

m = sum_of_product_of_devi/sum_of_sqr_of_devi_of_x
print(m)
b = mean_sales_y - (m*mean_ads_x)
print(b)

last=devi_y[len(devi_y)-1]
slast=devi_y[len(devi_y)-2]
resTemp=sales[len(sales)-1]+(last-slast)
print(resTemp)

#  Y = m X + b
# plotting
# 2013,2014,2015,2016,2017,2018

xplot = [100000,120000,140000,160000,220000,resTemp]
yplot = [100000,120000,140000,160000,220000,resTemp]
# data = [2,5,4]
plt.plot(yplot,xplot,marker='*')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2018 SALES PRIDICTION")
plt.show()
