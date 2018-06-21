class UI:
    def input(self):
        q=payroll()

        n=int(input("Enter number of employees : "))
        for i in range(n):
            name=input("Enter name : ")
            h_wage=float(input("Enter hourly wages : "))
            emp = employee(name,h_wage)
            q.add_employees(emp)
            
        m=int(input("Enter number of time cards : "))
        for i in range(m):
            name_tc=input("Enter name : ")
            mins_worked=int(input("Enter minutes worked : "))
            emp_tc = emp_time_card(name_tc,mins_worked)

            e=find_employee(name)
            e.add_time_card(emp_tc)

        return q            

class employee:
    def __init__(self,name,hourly_wages):
        self.name=name
        self.hourly_wages=hourly_wages
        self.time_cards=[]

    def add_time_card(self,time_card):
        self.time_cards.append(time_card)



class emp_time_card:
    def __init__(self,name,mins_worked):
        self.name=name
        self.mins_worked=mins_worked
        

class payroll:
    def __init__(self):
        self.employees=[]

    def add_employees(self,emp):
        self.employees.append(emp)

    def find_employee(self,name):
        for i in self.employees:
            if i.name == name:
                return i


    def print_payroll(self):
        pass
    

   
        
            



a=UI()
b=a.input()
print(b)
