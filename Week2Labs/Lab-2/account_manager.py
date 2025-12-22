class AccountManager:
    """
    Method to store account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc.acc_no = input("Enter the Account Number:")
        acc.name = input("Enter the Account Holder Name:")
        acc.balance = float(input("Enter the Account Balance:"))

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print()
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
