#scenario , working for a retail company d i have to analye quaterly sales data
#for different categoriees 
#you have 2 matrices , one containing sales data(quaterly) for each ca
# 
# category and another containinf price infor
#create matries (simulating real world data)
import numpy as np
#create 2d array (price per unit)
sales_data = np.array([[500,600,750,900],[300,350,400,450],[100,150,200,250]])

#1d array
price_per_unit = np.array([10,15,20,25])

quaterly_revenue = np.dot(sales_data,price_per_unit)
print(quaterly_revenue)

print("quaterly revenue for ach category: ")

for i,revenue in enumerate(quaterly_revenue):
    print(f"Category {i+1}: ${revenue:.2f}")