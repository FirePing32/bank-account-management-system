import dataset
from datetime import datetime

#setting current date and time
now = datetime.now() 

#setting up database                                     
data_base = dataset.connect('sqlite:///database.db')   
acc_info = data_base['accinfo']

print("")
print("# Welcome to Zinderbot E-Bank v1.0 ! #")
print("--------------------------------------")
print("")

def main_program():

	while True:
		
		try:

			#asking what the user wants to do
			print("Choose any one of the following by entering option no. --")
			print("")
			main_input = int(input("[1] Deposit money [2] Withdraw money [3] Know your account info"))
			print("")

			#if user wants to deposit
			if main_input == 1:

                                #request user account no, money to deposit, and update to database
                                print("")       
                                money_input = int(input("Enter ammount to be deposited : "))
                                acc_no_input = int(input("[~] account no. : "))
                                acc_info.update(dict(Account_No=acc_no_input, Balance=money_input), ['Balance'])
                                print("")
                                print("Updated to database !")
                                print("")

                        #if user wants to withdraw
			elif main_input == 2:

                                #request user account no, money to withdraw, and update to database
                                print("")
                                money_output = int(input("Enter ammount to be withdrawed : "))
                                acc_no_output = int(input("[~] account no. : "))
                                acc_info.update(dict(Account_No=acc_no_output, Balance=money_output), ['Balance'])
                                print("")
                                print("Updated to database !")
                                print("")

                        #if user wants to know account info
			elif main_input == 3:

                                #requesting method of info retrieval
                                print("")
                                print("Choose any one of the following by entering option no. -")
                                print("")
                                acc_no_input_find = int(input("[1] Find by account no. [2] Find by account name [3] Find by age [4] Find by gender"))

                                if acc_no_input_find == 1:
                                        #by account no
                                        print("")
                                        acc_no_input_find_no = int(input("Enter account no. : "))
                                        if_1 = acc_info.find_one(Account_No=acc_no_input_find_no)
                                        print(if_1)
                                        print("")

                                elif acc_no_input_find == 2:
                                        #by name
                                        print("")
                                        acc_no_input_find_name = input("Enter account name : ")
                                        if_2 = acc_info.find_one(Name=acc_no_input_find_name)
                                        print(if_2)
                                        print("")

                                elif acc_no_input_find == 3:
                                        #by age
                                        print("")
                                        acc_no_input_find_age = int(input("Enter age : "))
                                        if_3 = acc_info.find_one(Age=acc_no_input_find_age)
                                        print(if_3)
                                        print("")

                                elif acc_no_input_find == 4:
                                        #by gender
                                        print("")
                                        acc_no_input_find_gender = input("Enter gender : ")
                                        if_4 = table.find_one(Gender=acc_no_input_find_gender)
                                        print(if_4)
                                        print("")

                                else:
                                        print("Oops ! Something went wrong... Try again...") #null or incorrect input
                                        print("")
                                        main_program()

                        else:
                                print("Oops ! Something went wrong... Try again...") #null or incorrect input
                                print("")
                                main_program()
		
		except ValueError:

			pass
			print("Oops ! Something went wrong... Try again...") #null or incorrect input
			print("")
			main_program()

main_program()
