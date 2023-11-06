# # Danh sách các tuples
# data = [("English", 88), ("Science", 90), ("Math", 97), ("Social sciences", 82)]

# # Sắp xếp danh sách theo giá trị của tuple sử dụng lambda
# sorted_data = sorted(data, key=lambda x: x[1])

# # In danh sách đã sắp xếp
# for item in sorted_data:
#     print(item)

class Employee:
    def __init__(self,name,id,salary,department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
    def assign_department(self,department):
        self.department = department
    def print_detail(self):
        print(self.name,self.id,self.salary,self.department,sep=" ")
    def caculate_salary(self,time):
        if time > 50:
            self.salary = self.salary + int( (time - 50)*(self.salary/50) )

class BankAccount:
    def __init__(self):
        self.acoount_number = str(input())
        self.name = str(input())
        self.balance = int(input())
        self.date_open = str(input())
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        self.balance -= money
    def check_balance(self):
        return self.balance