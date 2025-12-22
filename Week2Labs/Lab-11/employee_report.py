from role_builder import RoleBuilder

class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self, report_date=""):
        self.report_date = report_date

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()
        print("EMP_ID\tNAME\tROLE\t\tBASIC\t\tHRA\tALLOW\tSALARY")
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        for emp in employees:
            role_desc = emp.get_role_description()
            allow = emp.get_allowance()
            salary = emp.get_salary()

            print(f"{emp.emp_id}\t{emp.name}\t{role_desc}\t{emp.basic:.2f}\t{emp.hra:.2f}\t{allow:.2f}\t{salary:.2f}")

        # Placeholder for employee information printing
        # Original C# code does not include the loop for displaying details

        self.display_footer(len(employees))
