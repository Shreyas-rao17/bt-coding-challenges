from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.emp_id = "E101"
        emp.name = "Shreyas"
        emp.gender = "Male"
        
        addr = Address() # Address Object Creation
        addr.address1 = "4, Rm Street"
        addr.address2 = "Near Dental Clinic"
        addr.city = "Bengaluru" 
        addr.pincode = 560016
        emp.address = addr

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : ", emp.emp_id)
        print("Employee Name : ", emp.name)
        print("Employee Gender : ", emp.gender)

        print("Employee Address : --------------")
        print("Address 1 : ", emp.address.address1)
        print("Address 2 : ", emp.address.address2)
        print("City : ", emp.address.city)
        print("PinCode : ", emp.address.pincode)
        print("----------------------------------")
        


if __name__ == "__main__":
    Program.main([])
