import dataset
from datetime import datetime

#setting current date and time
now = datetime.now() 

#setting up database                                     
data_base = dataset.connect('sqlite:///database.db')   
acc_info = data_base['accinfo']

#setting up username and password
user_name = "admin"   
pass_word = "admin"   

print("")
print("# Welcome to Zinderbot E-Bank v1.0 ! (Dev Mode) #")
print("-------------------------------------------------")
print("")
print("[~] Enter database username and password - ")
print("")

def main_program():

	#requests username and password from user
    enter_username = input("[~] Enter username : ")     
    enter_password = input("[~] Enter password : ")     
    print("")
    print("-----------------")

    if enter_username == user_name and enter_password == pass_word:   #checking username and password

        #if credentials correct, enjoy !
        print("")
        print("[+] Login successful !") 
        print("----------------------")
        print("")

        def enter_user_details():

            while True:

                try:

                	#setting up user account
                    acc_no = int(input("[~] Enter account no. : "))   
                    user_case = input("[~] Enter full name : ")        
                    age = int(input("[~] Enter age : "))
                    gender_case = input("[~] Enter gender : ")

                    #to minimize errors, changing case
                    name = user_case.lower()
                    gender = gender_case.lower()

                    #inserting data into database
                    acc_info.insert(dict(Account_No=acc_no, Name=name, Age=age, Gender=gender, Balance=0, Time=now))

                    print("")
                    print("[+] Saved to database !")
                    print("-----------------------")
                    print("")


                except ValueError:  #if any errors, pass it
                        pass
                        print ("")
                        print ("[-] Oops! An error occured... Please try again...")
                        print ("")
                        enter_user_details()

        enter_user_details()

    else:   #if incorrect username or password, re-request it from user

            print("")
            print("[-] Incorrect username or password !")
            print("------------------------------------")
            print("")
            main_program()


main_program()
