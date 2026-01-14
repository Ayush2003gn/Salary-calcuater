def database():
    employees = (#(id, name, basic salary)
        (1, "John Doe", 50000),
        (2, "Jane Smith", 60000),
        (3, "Bob Johnson", 55000),
        (4, "Alice Williams", 70000),
        (5, "Charlie Brown", 65000)
    )
    return employees    
def salary(x):
    # HRA = 15% of basic salary
    # DA = 10% of basic salary
    # TA = 20.2% of basic salary
    hra = 0.15 * x
    da = 0.10 * x
    ta = 0.202 * x
    gross_salary = x + hra + da + ta
    print(f"\n hra: {hra} \n da: {da} \n ta: {ta}")
    print("______________________________")
    print(f"Gross Salary: {gross_salary}")

    
user = input("Enter employee ID: ")
for emp in database(): #This loop accesses each employee record from the database one by one.
    if emp[0] == int(user):
        print(f"Employee Name: {emp[1]}, Basic Salary: {emp[2]}")
        print("-------------------------------")
        salary(emp[2])
        print("-------------------------------")
        break

if int(user) > 5 :
    print("ID not found")
elif user == None:
    print("No Input")
