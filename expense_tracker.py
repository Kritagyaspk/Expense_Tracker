import csv 

def save_expenses():
    date = input("Enter the date of expense(MM/DD):")
    description = input("Enter where you spend:")
    amount = input("Enter how much you spend")

    with open("expense.csv", 'a', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, description, amount])

    return() 

def view_expense(date):
    try:
        with open("expense.csv", 'r', newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)

            if not data:
                print("No expense recorded yet..")

            else:
                found = False

                for row in data:
                    if row[0] == date:
                        print(row)
                        found = True

                if not found:         
                    print("No expense recorded on this day.")

    except FileNotFoundError:
        print("No expense file found.")

def main():
    while True:
        num = input(
             "1. Record new expense\n"
             "2. See my expense\n"
             "3. Exit\n"
             "Select your choice:"
                
        )
        if num == '1':
            save_expenses()

        elif num == '2':
            date = input("Enter the date of expenditure:")
            view_expense(date)

        elif num == '3':
            print("Exiting the expense tracker....")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()




        



