x = 5
y = 10
print(x+y)

a = "Hello"
b = "World"
print(a+b)


# class over loading
class Plot:
   def __init__(self,x):
       self.x = x
   
   def __add__(self,other):
       return Plot(self.x + other.x)
       
   def __str__ (self):
       return "perimeter is : {}".format(self.x)

     
l = int(input("Enter Length of the plot: "))
b = int(input("Enter breadth of the plot: "))

length =Plot(l)
breadth = Plot(b)
perimeter = length + breadth
print(perimeter)