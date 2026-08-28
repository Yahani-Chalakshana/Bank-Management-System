#Initialize Variables
bank_acc_num=0
nic=0
first_name=0
last_name=0
birth_date=0
per_address=0
phone_num=0
bank_balance=0
deposit_amount=0
x=0
cus_count=0
new_acc=[]
cus1=[]
cus2=[]
cus3=[]
cus4=[]
cus5=[]
details=[]

#Add a new customer
def add_new_customer():

    print("                      ABC Bank                       ")
    print("                 Add a new customer                  ")

    while True:
        bank_acc_num=str(input("Bank Account Number : "))
        if len(bank_acc_num)==10 and bank_acc_num.isdigit():
            break
        else:
            print("Invalid bank account number.Please enter 10 digits number.")

    while True:
        nic=str(input("NIC : "))
        if len(nic)==10 and nic.isdigit():
            break
        else:
            print("Invalid NIC.Please enter 10 characters NIC number.")

    while True:
        first_name=str(input("First Name : "))
        if len(first_name)<=10 and len(first_name)>0:
            break
        else:
            print("Invalid first name.Please enter maximum 10 character name.")
                
    while True:
        last_name=str(input("Last Name : "))
        if len(last_name)<=15 and len(last_name)>0:
            break
        else:
            print("Invalid last name.Please enter maximum 15 characters name.")
            
    while True:
        birth_date=str(input("Birth Date(yyyy.mm.dd) : "))
        if len(birth_date)>0:
            break
        else:
            print("Please enter birth date correctly")
            
    while True:
        per_address=str(input("Permanent Address : "))
        if len(per_address)<=15 and len(per_address)>0:
            break
        else:
            print("Invalid permanent address.Please enter maximum 15 characters address")
            
    while True:
        phone_num=str(input("Phone Number : "))
        if len(phone_num)==10 and phone_num.isdigit() and len(phone_num)>0:
            break
        else:
            print("Invalid phone number.Please enter 10 digits number")

    details=[
        bank_acc_num,
        nic,
        first_name,
        last_name,
        birth_date,
        per_address,
        phone_num,
        bank_balance
        ]

    while True:
        save_acc=str(input("Do you want to save the account(yes/no)? ")).lower()
        
        if(save_acc=="yes"):
            
            if len(cus1)==0:
                cus1.extend(details)
                print("Coustomer added successfully")
                break
            elif len(cus2)==0:
                cus2.extend(details)
                print("Coustomer added successfully")
                break
            elif len(cus3)==0:
                cus3.extend(details)
                print("Coustomer added successfully")
                break
            elif len(cus4)==0:
                cus4.extend(details)
                print("Coustomer added successfully")
                break
            elif len(cus5)==0:
                cus5.extend(details)
                print("Coustomer added successfully")
                break
            else:
                print("Five customer lists already completed.")
                break
            
        elif (save_acc=="no"):
            print("Customer not added")
            break
        
        else:
            ("Invalid input.Please enter yes or no.")

#View details of a customer        
def view_customer_details():

    print("                      ABC Bank                          ")
    print("              View details of a customer                ")

    while True:
        bank_acc_num=str(input("Bank Account Number : "))
        if (len(bank_acc_num)==10 and bank_acc_num.isdigit()and len(bank_acc_num)>0):
            break
        else:
            print("Invalid bank account number.Please enter 10 digits number.")

    if len(cus1)>0 and bank_acc_num==cus1[0]:
        print("NIC : ",cus1[1])
        print("Phone Number : ",cus1[6])
        print("First Name : ",cus1[2])
        print("Last Name : ",cus1[3])
        print("Bank Balance : ",cus1[7])
                    
    elif len(cus2)>0 and bank_acc_num==cus2[0]:
        print("NIC : ",cus2[1])
        print("Phone Number : ",cus2[6])
        print("First Name : ",cus2[2])
        print("Last Name : ",cus2[3])
        print("Bank Balance : ",cus2[7])
                    
    elif len(cus3)>0 and bank_acc_num==cus3[0]:
        print("NIC : ",cus3[1])
        print("Phone Number : ",cus3[6])
        print("First Name : ",cus3[2])
        print("Last Name : ",cus3[3])
        print("Bank Balance : ",cus3[7])

    elif len(cus4)>0 and bank_acc_num==cus4[0]:
        print("NIC : ",cus4[1])
        print("Phone Number : ",cus4[6])
        print("First Name : ",cus4[2])
        print("Last Name : ",cus4[3])
        print("Bank Balance : ",cus4[7])

    elif len(cus5)>0 and bank_acc_num==cus5[0]:
        print("NIC : ",cus5[1])
        print("Phone Number : ",cus5[6])
        print("First Name : ",cus5[2])
        print("Last Name : ",cus5[3])
        print("Bank Balance : ",cus5[7])

    else:
        print("Customer not included to the system.")

    while True:
        view=str(input("Do you want to view another account details(yes/no)? ")).lower()
        if (view=="yes"):
            view_customer_details()
            break
        elif (view=="no"):
            break
        else:
            print("Invalid input.Please enter yes or no.")

#View details of all customers                        
def view_all_customers_details():

        print("                                             ABC Bank                                             ")
        print("                                  View details of all customers                                   ")

        print("  NIC           Account No     First Name      Last Name     Bank Balance   ")

        if len(cus1)>0 or len(cus2)>0 or len(cus3)>0 or len(cus4)>0 or len(cus5)>0:

            if len(cus1)>0:
                print(cus1[1],"    ",cus1[0],"    ",cus1[2],"    ",cus1[3],"    ",cus1[7])

            if len(cus2)>0:
                print(cus2[1],"    ",cus2[0],"    ",cus2[2],"    ",cus2[3],"    ",cus2[7])

            if len(cus3)>0:
                print(cus3[1],"    ",cus3[0],"    ",cus3[2],"    ",cus3[3],"    ",cus3[7])

            if len(cus4)>0:
                print(cus4[1],"    ",cus4[0],"    ",cus4[2],"    ",cus4[3],"    ",cus4[7])

            if len(cus5)>0:
                print(cus5[1],"    ",cus5[0],"    ",cus5[2],"    ",cus5[3],"    ",cus5[7])

                while True:
                    update=str(input("Do you want to update the account details(yes/no)? ")).lower()

                    if (update=="yes"):
                        update_customer_details()
                        break
                    elif (update=="no"):
                        break
                    else:
                        print("Invalid input.Please enter yes or no")

        else:
            print("Account details not added")
           
#Deposit money
def deposit_money():

    print("                                       ABC Bank                             ")
    print("                            Deposit Money to a given account                ")

    while True:
        bank_acc_num=str(input("Bank Account Number : "))
        if len(bank_acc_num)==10 and bank_acc_num.isdigit():
            if(len(cus1)>0 and bank_acc_num==cus1[0])or (len(cus2)>0 and bank_acc_num==cus2[0])or(len(cus3)>0 and bank_acc_num==cus3[0])or(len(cus4)>0 and bank_acc_num==cus4[0])or (len(cus5)>0 and bank_acc_num==cus5[0]):
                break
            else:
                print("Customer not in system")
        else:
            print("Invalid input.Please enter 10 digits bank account number.")

    while True:
        deposit_amount_str=input("Deposit amount : ")

        try:
            deposit_amount=float(deposit_amount_str)
            if deposit_amount>0:
                print("Deposit amount accepted")
                break
            else:
                print("Please enter a valid amount")
        except ValueError:
            print("Invalid input.Please enter a valid amount")

    if bank_acc_num==cus1[0]:
        while True:
             save=input("Do you want to save (yes/no)? ").lower()

             if (save=="yes"):
                 cus1[7]=cus1[7]+deposit_amount
                 print("Money deposited successfully")
                 break
             elif(save=="no"):
                 print("Money not deposited")
                 break
             else:
                print("Invalid input.Please input yes or no.")

    elif bank_acc_num==cus2[0]:
         while True:
             save=input("Do you want to save (yes/no)? ").lower()

             if (save=="yes"):
                 cus2[7]=cus2[7]+deposit_amount
                 print("Money deposited successfully")
                 break
             elif (save=="no"):
                 print("Money not deposited")
                 break
             else:
                print("Invalid input.Please input yes or no.")

    elif bank_acc_num==cus3[0]:
        while True:
             save=input("Do you want to save (yes/no)? ").lower()

             if (save=="yes"):
                 cus3[7]=cus3[7]+deposit_amount
                 print("Money deposited successfully")
                 break
             elif (save=="no"):
                 print("Money not deposited")
                 break
             else:
                print("Invalid input.Please input yes or no.")

    elif bank_acc_num==cus4[0]:
        while True:
             save=input("Do you want to save (yes/no)? ").lower()

             if (save=="yes"):
                 cus4[7]=cus4[7]+deposit_amount
                 print("Money deposited successfully")
                 break
             elif (save=="no"):
                 print("Money not deposited")
                 break
             else:
                print("Invalid input.Please input yes or no.")

    elif bank_acc_num==cus5[0]:
        while True:
             save=input("Do you want to save (yes/no)? ").lower()

             if (save=="yes"):
                 cus5[7]=cus5[7]+deposit_amount
                 print("Money deposited successfully")
                 break
             elif (save=="no"):
                 print("Money not deposited")
                 break
             else:
                print("Invalid input.Please input yes or no.")

#Withdraw money
def withdraw_money():

    print("                         ABC Bank                               ")
    print("             Withdraw money from a given account                ")
    
    while True:
        bank_acc_num=str(input("Bank Account Number : "))
        if len(bank_acc_num)==10 and bank_acc_num.isdigit():
            if(len(cus1)>0 and bank_acc_num==cus1[0])or (len(cus2)>0 and bank_acc_num==cus2[0])or(len(cus3)>0 and bank_acc_num==cus3[0])or(len(cus4)>0 and bank_acc_num==cus4[0])or (len(cus5)>0 and bank_acc_num==cus5[0]):
                break
            else:
                print("Customer not found")
        else:
            print("Invalid input.Please enter 10 digits bank account number.")

    
    while True:
        withdraw_amount_str=input("Withdaw amount: ")

        try:
            withdraw_amount=float(withdraw_amount_str)
            if withdraw_amount>0:
                break
            else:
                print("Please enter a valid amount")
        except ValueError:
            print("Invalid input.Please enter a valid amount")

    if len(cus1)>0 and bank_acc_num == cus1[0] and cus1[7]>=withdraw_amount:
        while True:
            save=input("Do you want to save (yes/no)? ").lower()
            if (save=="yes"):
                cus1[7]=cus1[7]-withdraw_amount
                print("Money withdrew successfully")
                break
            elif (save=="no"):
                print("Money not withdrew")
                break
            else:
                print("Invalid input.Please input yes or no.")

    elif len(cus2)>0 and bank_acc_num == cus2[0] and cus2[7]>=withdraw_amount:
        while True:
            save=input("Do you want to save (yes/no)?").lower()
            if (save=="yes"):
                cus2[7]=cus2[7]-withdraw_amount
                print("Money withdrew successfully")
                break
            elif (save=="no"):
                print("Money not withdrew")
                break
            else:
                print("Invalid input.Please input yes or no.")

    elif len(cus3)>0 and  bank_acc_num == cus3[0] and cus3[7]>=withdraw_amount:
        while True:
            save=input("Do you want to save (yes/no)? ").lower()
            if (save=="yes"):
                cus3[7]=cus3[7]-withdraw_amount
                print("Money withdrew successfully")
                break
            elif (save=="no"):
                print("Money not withdrew")
                break
            else:
                print("Invalid input.Please input yes or no.")

    elif len(cus4)>0 and bank_acc_num == cus4[0] and cus4[7]>=withdraw_amount:
        while True:
            save=input("Do you want to save (yes/no)? ").lower()
            if (save=="yes"):
                cus4[7]=cus4[7]-withdraw_amount
                print("Money withdrew successfully")
                break
            elif (save=="no"):
                print("Money not withdrew")
                break
            else:
                print("Invalid input.Please input yes or no.")

    elif len(cus5)>0 and bank_acc_num == cus5[0] and cus5[7]>=withdraw_amount:
        while True:
            save=input("Do you want to save (yes/no)? ").lower()
            if (save=="yes"):
                cus5[7]=cus5[7]-withdraw_amount
                print("Money withdrew successfully")
                break
            elif (save=="no"):
                print("Money not withdrew")
                break
            else:
                print("Invalid input.Please input yes or no.")
    else:
        print("Insufficient balance")

#Update the all customers details 
def update_customer_details():

    print("                            ABC Bank                         ")
    print("                     Update Customer Details                 ")

    while True:
        bank_acc_num=str(input("Bank Account Number : "))
        if len(bank_acc_num)==10 and bank_acc_num.isdigit():
            if(len(cus1)>0 and bank_acc_num==cus1[0])or (len(cus2)>0 and bank_acc_num==cus2[0])or(len(cus3)>0 and bank_acc_num==cus3[0])or(len(cus4)>0 and bank_acc_num==cus4[0])or (len(cus5)>0 and bank_acc_num==cus5[0]):
                break
            else:
                print("Customer not found")
        else:
            print("Invalid input.Please enter 10 digits bank account number.")


    if (bank_acc_num==cus1[0]or bank_acc_num==cus2[0]or bank_acc_num==cus3[0]or bank_acc_num==cus4[0]or bank_acc_num==cus5[0]):

        while True:
            nic=str(input("NIC : "))
            if len(nic)==10:
                break
            else:
                print("Invalid NIC number.Please enter only 10 characters.")

        while True:
            first_name=str(input("First Name : "))
            if len(first_name)<=10 and len(first_name)>0:
                break
            else:
                print("Invalid first name.Please enter maximum 10 character name.")
                
        while True:
           last_name=str(input("Last Name : "))
           if len(last_name)<=15 and len(last_name)>0:
               break
           else:
               print("Invalid last name.Please enter maximum 15 characters name.")
            
        while True:
           birth_date=str(input("Birth Date : "))
           if len(birth_date)>0:
               break
           else:
               print("Please enter birth date correctly")
            
        while True:
           per_address=str(input("Permanent Address : "))
           if len(per_address)<=15 and len(per_address)>0:
               break
           else:
               print("Invalid permanent address.Please enter maximum 15 characters address")
            
        while True:
           phone_num=str(input("Phone Number : "))
           if len(phone_num)==10 and phone_num.isdigit():
               break
           else:
               print("Invalid phone number.Please enter 10 digits number")

    else:
        print("Customer not found")

    while True:
           save=str(input("Do you want to save the account(yes/no)? ")).lower()

           if (save=="yes"):
               if bank_acc_num==cus1[0]:
                   cus1[1]=nic
                   cus1[2]=first_name
                   cus1[3]=last_name
                   cus1[4]=birth_date
                   cus1[5]=per_address
                   cus1[6]=phone_num
                   print("Details updated successfully")
                   break
                
               elif bank_acc_num==cus2[0]:
                   cus2[1]=nic
                   cus2[2]=first_name
                   cus2[3]=last_name
                   cus2[4]=birth_date
                   cus2[5]=per_address
                   cus2[6]=phone_num
                   print("Details updated successfully")
                   break
                
               elif bank_acc_num==cus3[0]:
                   cus3[1]=nic
                   cus3[2]=first_name
                   cus3[3]=last_name
                   cus3[4]=birth_date
                   cus3[5]=per_address
                   cus3[6]=phone_num
                   print("Details updated successfully")
                   break
                
               elif bank_acc_num==cus4[0]:
                  cus4[1]=nic
                  cus4[2]=first_name
                  cus4[3]=last_name
                  cus4[4]=birth_date
                  cus4[5]=per_address
                  cus4[6]=phone_num
                  print("Details updated successfully")
                  break
                
               elif bank_acc_num==cus5[0]:
                  cus5[1]=nic
                  cus5[2]=first_name
                  cus5[3]=last_name
                  cus5[4]=birth_date
                  cus5[5]=per_address
                  cus5[6]=phone_num
                  print("Details updated successfully")
                  break

           elif (save=="no"):
               print("Details not updated")
               break
           else:
               print("Invalid input.Please enter yes or no.")

#Main menu
if __name__ == "__main__":
    
    while True:
        print("                        ABC Bank                 ")
        print("                        Main Menu                ")

        print("""
                1)Add a new customer
                2)View details of a customer including his/her bank balance
                3)View details of all the customers with their bank balances
                4)Deposit money to a given account
                5)Withdraw money from a given account
                6)Update Customer Details
                7)Exit
                """)
        x=int(input("                                                            Your Choice: "))
        
        if x==1:
            add_new_customer()
        elif x==2:
            view_customer_details()
        elif x==3:
            view_all_customers_details()
        elif x==4:
            deposit_money()
        elif x==5:
            withdraw_money()
        elif x==6:
            update_customer_details()
        elif x==7:
            print("Thank you for choosing ABC bank.")
            break
        else:
            print("Invalid choice.Please enter a number from 1 to 7.")
