from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 4

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            emp = Employee()
            
            emp.emp_id = int(input("Employee Id: "))
            emp.name = input("Name: ")
            emp.basic = float(input("Basic: "))
            emp.hra = float(input("HRA: "))
            emp.allowance_percentage = float(input("Allowance Percentage: "))
            

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            emp.role  = int(input("Role: "))
            
            employees[i] = emp


        report_date = input("Enter the date of the report (dd/mm/yyyy) : ")

        report = EmployeeReport()
        
        report.report_date = report_date
        print()
        
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main([])
