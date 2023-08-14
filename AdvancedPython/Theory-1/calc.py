class Obj_dist:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

def calculate_total_distance(distances):
    total_feet = sum(d.feet for d in distances)
    total_inches = sum(d.inches for d in distances)

    extra_feet = total_inches // 12 #converting in to ft >12
    total_feet += extra_feet
    total_inches %= 12

    return total_feet, total_inches


distances = []
total_inputs = int(input("Enter the total number of distance: ")) #user input

for i in range(total_inputs):
    feet = int(input(f"Enter feet for distance {i + 1}: "))
    inches = int(input(f"Enter inches for distance {i + 1}: "))
    distances.append(Obj_dist(feet, inches))

f, i = calculate_total_distance(distances)

print("Total distance is", f, "feet and", i, "inches")
