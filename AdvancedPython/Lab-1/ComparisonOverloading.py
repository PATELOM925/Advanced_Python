
# __lt__ for less than comparison <
# __le__ for less than or equal to comparison <=
# __gt__ for greater than comparison >
# __ge__ for greater than or equal to comparison >=
# __eq__ for equal to comparison ==
# __ne__ for not equal to comparison !=

class comparison:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return 'Plot perimeter is: {}'.format(self.x)

    def __lt__(self, other):
        return self.x < other.x   
        
    def __gt__(self, other):
        return self.x > other.x 
        
    def __eq__(self,other):
        return self.x == other.x
 
p1 = int(input("Enter perimeter of the plot1: "))
p2 = int(input("Enter perimeter of the plot2: "))
    
cmp1 = comparison(p1)   
cmp2 = comparison(p2)
 
print("Plot 1 < Plot 2",cmp1<cmp2)
print("Plot 1 > Plot 2",cmp1>cmp2)
print("plot 1 = Plot 2",cmp1==cmp2)
