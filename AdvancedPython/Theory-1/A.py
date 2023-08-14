a = 6

for i in range(a):
    for j in range(2*a + 1):
         if (i == 0 and j % 2 == 0) or (i == a // 2 and j % 2 == 0) or (j == 0 and i != 0) or (j ==  a*2 and i != 0):
                print("*", end="")
         else:
                print(" ", end="")
    print()