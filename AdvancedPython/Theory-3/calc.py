import csv

def cal_from_col(reader, col_name):
    col = []
    
    # Check if column exists or not
    if col_name not in reader.fieldnames:
        print(f"Column '{col_name}' does not exist in the CSV file.")
        return None
            
    for row in reader:
        value = row[col_name].strip()
        if value.isdigit():
            col.append(int(value))
        else:
            print(f"Column '{col_name}' does not contain numeric values.")
    ans = sum(col)
    avg = ans/len(col)
    print(f"The sum of values in column '{col_name}' is: {ans}, and Avferage is {avg}")
    return ans

def main():
    col_name = "Number"
    file = "calc.csv"

    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        cal_from_col(reader, col_name)

main()
