from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = []

        # Accept employee information from the user
        print("Enter employee information")
        
        # FIRST EMPLOYEE: using empty constructor
        print("\nEmployee No : 1")
        emp = Employee()

        emp.emp_id = input("Id : ")
        emp.name = input("Name : ")
        emp.basic = float(input("Basic : "))
        emp.hra = float(input("HRA : "))
        emp.allowance_percentage = float(input("Percentage of Allowance : "))
        print("Enter Role Id : ")
        for r in Roles:
            print(f"{r.value}. {RoleBuilder.get_role_description(r.value)}")

        emp.role = int(input("Role : "))
        employees.append(emp)

        for i in range(3):
            print("Employee No : " + str(i+2))
            
            emp_id = int(input("Employee Id: "))
            name = input("Name: ")
            basic = float(input("Basic: "))
            hra = float(input("HRA: "))
            allowance_percentage = float(input("Allowance Percentage: "))
            

            print("Enter Role Id : ")
            for r in Roles:
                print(f"{r.value}. {RoleBuilder.get_role_description(r.value)}")
            role  = int(input("Role: "))
            
            emp = Employee(emp_id, name, basic, hra, allowance_percentage, role)
            
            employees.append(emp)


        report_date = input("Enter the date of the report (dd/mm/yyyy) : ")

        report = EmployeeReport(report_date)
        
        report.report_date = report_date
        print()
        
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main([])
