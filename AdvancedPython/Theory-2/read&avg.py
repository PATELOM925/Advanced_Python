import csv

def read_csv(filename):
    data = []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                data.append(float(value))
    return data

def calculate_avg(data):
    if data:
        total = sum(data)
        average = total / len(data)
        return average
    else:
        return None

def main():
    filename = "onlygrades.csv"  # Entering the data file name
    data = read_csv(filename)
    average = calculate_avg(data)

    if average is not None:
        print(f"The average of the values in the file is: {average:.2f}")
    else:
        print("No data found in the file.")

# Call the main function to run the program
main()
