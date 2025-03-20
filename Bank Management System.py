import json
import random
import os
import datetime
import pywhatkit
import time

data = {}
class BankAccount:
    def __init__(self, user_name,data, password="Krsbank[65]"):
        self.data = data
        self.__account_number = str(random.randint(100000000, 999999999999999999))
        self.user_name = user_name
        self.__password = str(password)

    def save_data(self):        
        with open("account.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def load_data(self):
        with open("account.json", "r") as file:
            self.data = json.load(file)

    def sign_up(self): 
        if (self.user_name not in self.data):
            self.new_user = {
                self.user_name:{"account_number": self.__account_number ,
                                "password": self.__password,
                                "balance":0,
                                "transaction":{}
                                }
                            }
            self.data.update(self.new_user)
            self.save_data()   
            print(f"Sign up Successfully! Welcom {self.user_name}.")  
            self.features()
            
        elif (self.user_name  in self.data):
            print("user already exists!")

    def login(self):
        if (self.user_name in self.data) and (self.__password != self.data[self.user_name]["password"]):
            print("Incorrect password!")  

        elif (self.user_name in self.data) and (self.__password == self.data[self.user_name]["password"]):
            print(f'Login Successfully! Welcom Back {self.user_name}.')
            self.save_data()
            self.features()
        else:
            print("User not exits!")

    def account_detail(self):
        print(f'Accoun Holder: {self.user_name}\nAccount Number: {self.data[self.user_name]["account_number"]}')

    def reset_password(self,account_holder):
        try:
            if account_holder not in self.data:
                print("User not exits!")
        
            elif account_holder in self.data:
                self._phone_number = f"+91{input("Enter phone number: ")}"
                self.__message = random.randint(1001, 9999)
                random.seed()                
                pywhatkit.sendwhatmsg_instantly(self._phone_number, f"Your varification code: {self.__message}", wait_time=8, tab_close=True)
                time.sleep(2)
                os.remove("PyWhatKit_DB.txt")
                
                while True:
                    self.__varification_code = int(input("Enter varification code: ").strip())

                    if self.__varification_code != self.__message:
                        print("\nWrong varification Code.")
                    else:
                        while True:
                            self.__new_password = input("\nNew password: ").strip()
                            self.__confirm_password = input("confirm Password: ").strip()
                            if self.__new_password != self.__confirm_password :
                                print("Password not Match!")
                            elif len(self.__new_password) < 8:
                                print("Password must be 8 digits!")
                            elif self.__new_password == self.data[account_holder]["password"]:
                                print("Same old Paaword!")
                            else:
                                self.data[account_holder]["password"] = self.__new_password 
                                print('Password upadate successfully.')
                                self.save_data()
                                return
        except ValueError:
            print("Wrong varification code!")

    def check_balance(self):
        print(f'Your Balance is: {self.data[self.user_name]["balance"]}')

    def deposite(self, amount):
        try:
            if amount < 0:
                print("We don't allow negative Transaction!")
                return
            elif amount == 0:
                print("Nothing deposite to Your account. Invalid Amount!")
                return
            if f"transaction_on_{datetime.datetime.now().strftime('%d/%b/%y')}" not in self.data[self.user_name]["transaction"]:
                self.data[self.user_name]["transaction"][f"transaction_on_{datetime.datetime.now().strftime('%d/%b/%y')}"] = {}
            if f"transaction_time_{datetime.datetime.now().strftime("%H.%M.%S")}_{datetime.datetime.now().microsecond}" not in self.data[self.user_name]["transaction"][f"transaction_on_{datetime.datetime.now().strftime("%d/%b/%y")}"]:
                self.data[self.user_name]["transaction"][f"transaction_on_{datetime.datetime.now().strftime("%d/%b/%y")}"][f"transaction_time_{datetime.datetime.now().strftime("%H.%M.%S")}_{datetime.datetime.now().microsecond}"] = {"deposite":amount}
                self.data[self.user_name]["balance"] += amount
                self.save_data()
                print(f"{amount} Amount deposite to your account successfully.")
            else:
                print("Fail to desposite amount.")

        except ValueError:
            print(f"\nAmount should in numbers.")
    
    def withdraw(self, amount):
        try:
            if amount < 0:
                print("We don't allow negative Transaction!")
                return
            elif amount == 0:
                print("Nothing withdraw from Your account. Invalid Amount!")
                return
            elif amount > self.data[self.user_name]["balance"]:
                print("Not enough amount in your balance!")
                return
            if f"transaction_on_{datetime.datetime.now().strftime('%d/%b/%y')}" not in self.data[self.user_name]["transaction"]:
                self.data[self.user_name]["transaction"][f"transaction_on_{datetime.datetime.now().strftime('%d/%b/%y')}"] = {}
            if f"transaction_time_{datetime.datetime.now().strftime("%H.%M.%S")}_{datetime.datetime.now().microsecond}" not in self.data[self.user_name]["transaction"][f"transaction_on_{datetime.datetime.now().strftime("%d/%b/%y")}"]:
                self.data[self.user_name]["transaction"][f"transaction_on_{datetime.datetime.now().strftime("%d/%b/%y")}"][f"transaction_time_{datetime.datetime.now().strftime("%H.%M.%S")}_{datetime.datetime.now().microsecond}"] = {"withdraw_amount":amount}
                self.data[self.user_name]["balance"] -= amount
                self.save_data()
                print(f"{amount} Amount withdraw from your account successfully.")
            else:
                print("Fail to desposite amount.")
        except ValueError:
            print(f"\nAmount should in numbers.")
    def transaction_history(self):
        try:
            self.history = self.data[self.user_name]["transaction"]
            self.user_date = input("Date in this format 15/Mar/25: ").title()
            self.transaction_time = self.history[f"transaction_on_{self.user_date}"]        
        
            with open("transaction_history.txt", "w") as history:
                data_history = " "
                for i in self.transaction_time:
                    self.data = self.history[f"transaction_on_{self.user_date}"][i]
                    data_history += f"\n{i} = {self.data}"
                history.writelines(f"Transaction_date_{self.user_date}:\n{data_history}")
                print("Transaction History save to transaction_history.txt file.")
        except KeyError:
            print("No Transaction on this date.")
            

    def features(self):
        while True:
            try:
                self.load_data()
                print(f'''\n
------------------------
     K.RS Bank
------------------------
1. Account detail
2. Deposite Amount
3. Withdraw Amount
4. Check Balance
5. Transaction history
6. Log Out / Exit
------------------------
              ''')
                obj = self
                self.user_want = input("What you want to do: ").strip()
                if self.user_want == "1":
                    obj.account_detail()
                elif self.user_want == "2":
                    self.deposite_amount = int(input("How much amount you to want to deposite: ").strip())
                    obj.deposite(self.deposite_amount)
                elif self.user_want == "3":
                    self.withdraw_amount = int(input("How amount you want to withdraw: ").strip())
                    obj.withdraw(int(self.withdraw_amount))
                elif self.user_want == "4":
                    obj.check_balance()
                elif self.user_want == "5":
                    obj.transaction_history()
                elif self.user_want == "6":
                    break
                else:
                    print("Error: You NOT choose.")
            except ValueError:
                print("Amount should we in numbers!")
def main():
    while True:
        if os.path.exists("account.json"):
            with open("account.json", "r") as file:
                memory = file.read().strip()

            print(f'''\n
--------------------
     K.RS Bank
--------------------
1. Sign up Account
2. Login Account
3. Reset Password
4. Quit
--------------------
              ''')
        
            user_entry = input("\nSign up or Login 1/2: ").strip()
        
            if user_entry == "1":
                name = input("\nUser name: ").strip()
                password = input("User password: ").strip()
                user = BankAccount(name,data, password)

                confirm_password = input("Confirm password: ")
                if  len(password) < 8:
                    print("Password must be 8 digits or greater!") 
                elif password == confirm_password:
                    if not memory:
                        user.sign_up()
                    else:
                        user.load_data()
                        user.sign_up() 
                else:
                    print("Passowrd not match!")
            elif user_entry == "2":
                name = input("\nUser name: ").strip()
                password = input("User password: ").strip()
                user = BankAccount(name,data, password)
                if not memory:
                    print("User not exits!")
                else:
                    user.load_data()
                    user.login()
            elif user_entry == "3":
                name = input("\nUser name: ").strip()
                user = BankAccount(name, data)
                if not memory:
                    print("User not exits!")
                else:
                    user.load_data()
                    user.reset_password(name)
            elif user_entry == "4":
                break        
            else:
                print("Error: You NOT choose.")
        else:
            with open("account.json", 'w') as f:
                pass

if __name__ == "__main__":
    main()