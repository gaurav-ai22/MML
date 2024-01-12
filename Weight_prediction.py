# implement python program to performk limnar reggresion on a dataset of heights and weights, predict the weight based on  heights ? calaculate y=[weight] x=[height]

import matplotlib.pyplot as plt

height = [1.47, 1.5, 1.52, 1.55, 1.57, 1.6, 1.63, 1.65, 1.68, 1.7, 1.73, 1.75, 1.78, 1.8, 1.83]
weight = [52.21, 53.12, 54.48, 55.84, 57.2, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.1, 69.92, 71.19, 74.46]

mean_height = sum(height) / len(height)
mean_weight = sum(weight) / len(weight)

numerator = sum([(height[i] - mean_height) * (weight[i] - mean_weight) for i in range(len(height))])
denominator = sum([(height[i] - mean_height) ** 2 for i in range(len(height))])

slope = numerator / denominator
intercept = mean_weight - slope * mean_height

new_height = float(input("Enter the new height to predict weight: "))

predicted_weight = slope * new_height + intercept

print(f'Predicted Weight for the new height : {predicted_weight:.2f}')

xplot=[1.47, 1.5, 1.52, 1.55, 1.57, 1.6, 1.63, 1.65, 1.68, 1.7, 1.73, 1.75, 1.78, 1.8, 1.83]

yplot=[52.21, 53.12, 54.48, 55.84, 57.2, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.1, 69.92, 71.19, 74.46]

plt.plot(xplot,yplot,marker="o",c="black")
plt.xlabel("HEIGHT")
plt.ylabel("WEIGHT")
plt.title("WEIGHT PREDICTION")
plt.show()







