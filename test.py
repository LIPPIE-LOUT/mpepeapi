import os
from datetime import datetime
import random
from msvcrt import putch

from getpass4 import getpass


def clear():
    os.system("clear")


def get_pin(my_pin):
    # pin = getpass('Enter pin: ')
    pin = input("Enter Pin")
    if pin == my_pin:
        return True
    else:
        return False


def get_timestamp():
    current_timestamp = datetime.now()
    return current_timestamp


def random_messages():
    prom_msgs = ["Dear customer you are now legible to okoa jahazi dial *254# Safaricom moving with u",
                 "Get 15 GB for as low as ksh 1000, valid for 30 days!!Dial *544*71# and subscribe to watch ur fav show",
                 "Talk more with the new safaricom (OFA MOTO) get upto a whole 90 mins of talking time with ur fam for as low as ksh30"]
    promo = random.choice(prom_msgs)
    return promo


def code_generator():
    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    code = "SI"
    for i in range(8):
        character = random.choice(chars)
        code += character
    return code


print("Safaricom SIM Toolkit")

balance = 20000
airtime = 0
my_pin = "7777"
mshwari_bal = 0
loan_limit = 1000
mshwari_loan_amount = 0

for transaction in range(3):

    main_option = input("Choose an option:\n 1. Safaricom,\n 2. M-PESA : ")

    if main_option == "1":

        safaricom_option = input("Choose an option: 1. MyAccount, 2. M-banking services : ")

        if safaricom_option == "1":
            account_option = input("Choose an option: 1. Balance inquiry, 2. Top-up, 3. Selfcare, 4. Customer-care : ")
            if account_option == "1":
                print(f"Your airtime balance is {airtime}")
            elif account_option == "2":
                print("b. Top-up")
            elif account_option == "3":
                print("c. Selfcare")
            elif account_option == "4":
                print("d. Customer-care")

        elif safaricom_option == "2":

            mbanking_option = input(
                "Choose an option: 1. Barclays bank, 2. Coop bank, 3. Dtb, 4. Ecobank, 5. Equity, 6. Family, 7. I&M : ")
            if mbanking_option == "1":
                print("Barclays bank")
            elif mbanking_option == "2":
                print("Coop bank")
            elif mbanking_option == "3":
                print("Dtb")
            elif mbanking_option == "4":
                print("Ecobank")
            elif mbanking_option == "5":
                print("Equity")
            elif mbanking_option == "6":
                print("Family")
            elif mbanking_option == "7":
                print("I&M")

    elif main_option == "2":

        mpesa_option = input(
            "Choose an option: 1. Send money, 2. Withdraw cash, 3. Buy airtime, 4. Loans and savings, 5. Lipa na Mpesa,  6. My account : ")

        if mpesa_option == "1":
            phone_number = input("Enter Phone number: ")
            amount = int(input("Enter amount: "))
            pin = get_pin(my_pin)
            mpesa_balance = balance - amount
            transaction_code = code_generator()
            promotional_msg = random_messages()

            print(
                f"{transaction_code} Confirmed you have sent amount {amount} to John Ndue {phone_number} at {get_timestamp()} Your new Mpesa balance is {mpesa_balance}\n"
                f" {promotional_msg}")


        elif mpesa_option == "2":

            withdraw_option = input("Choose an option: 1. From agent, 2. From ATM : ")

            if withdraw_option == "1":
                agent_number = input("Enter agent number: ")
                store_number = input("Enter store number: ")
                amount = int(input("Enter amount: "))
                pin = get_pin(my_pin)
                balance -= amount
                transaction_code = code_generator()
                promotional_msg = random_messages()

                print(
                    f"{transaction_code} Confirmed you have withdrawn amount {amount} from John Ndue {phone_number} at {get_timestamp()} Your new Mpesa balance is {balance}\n"
                    f"{promotional_msg}")

            elif withdraw_option == "2":
                agent_number = input("Enter agent number: ")
                amount = int(input("Enter amount: "))
                pin = get_pin(my_pin)
                balance -= amount
                transaction_code = code_generator()
                promotional_msg = random_messages()

                print(
                    f"{transaction_code} Confirmed you have sent amount {amount} to John Ndue {phone_number} at {get_timestamp()} Your new Mpesa balance is {balance}\n"
                    f"{promotional_msg}")
        elif mpesa_option == "3":

            airtime_option = input("Choose an option: 1. My phone, 2. Other phone : ")

            if airtime_option == "1":
                amount = int(input("Enter amount: "))
                pin = get_pin(my_pin)
                balance -= amount
                transaction_code = code_generator()
                promotional_msg = random_messages()
                airtime += amount
                print(
                    f"{transaction_code} Confirmed you have boughtairtime {amount}  for  at {get_timestamp()} Your new Mpesa balance is {balance} new airtime balance {airtime}\n"
                    f"{promotional_msg}")

            elif airtime_option == "2":
                phone_number = input("Enter phone number: ")
                amount = int(input("Enter amount: "))
                pin = get_pin(my_pin)
                balance -= amount
                transaction_code = code_generator()
                promotional_msg = random_messages()
                print(
                    f"{transaction_code} Confirmed you have bought airtime of {amount} to John Ndue {phone_number} at {get_timestamp()} Your new Mpesa balance is {balance}\n"
                    f"{promotional_msg}")

        elif mpesa_option == "4":

            loans_option = input("Choose an option: 1. Mshwari, 2. KCB M-Pesa : ")

            if loans_option == "1":

                mshwari_option = input(
                    "Choose an option: 1. Send to Mshwari, 2. Withdraw to M-Pesa, 3. Lock savings account, 4. Loan @ 9% for 30 days, 5. Fixed savings account, 6. Check balance : ")

                if mshwari_option == "1":
                    amount = int(input("Enter amount: "))
                    pin = get_pin(my_pin)
                    if pin:
                        transaction_code = code_generator()
                        balance -= amount
                        promotional_msg = random_messages()
                        mshwari_bal += amount
                        timestamp = get_timestamp()
                        print(
                            f"You have deposited Ksh{amount} from your Mpesa account at {timestamp},your new M-shwari balance is {mshwari_bal} Mpesa balance is {balance}\n"

                            f"{promotional_msg}")
                    else:
                        print("Entered wrong pin")
                elif mshwari_option == "2":
                    amount = int(input("Enter amount: "))
                    pin = get_pin(my_pin)
                    if pin:
                        transaction_code = code_generator()
                        balance += amount
                        promotional_msg = random_messages()
                        mshwari_bal -= amount
                        print(
                            f"You have withdrawn Ksh{amount} from your M-shwari account at {timestamp},your new M-shwari balance is {mshwari_bal} Mpesa balance is {balance}\n"

                            f"{promotional_msg}")
                    else:
                        print("Entered wrong pin")
                elif mshwari_option == "3":
                    print("Lock savings account")
                elif mshwari_option == "4":
                    mshwari_loan_options = input("Enter an option \n1. Request Loan\n2. Pay Loan\n3.Check loan limit\n4. Loan Balance")
                    if mshwari_loan_options == "1":
                        loan_amount = int(input("Enter amount : "))
                        if get_pin(my_pin):
                            if loan_amount <= loan_limit:
                                mshwari_bal += loan_amount
                                loan_limit -= loan_amount
                                timestamp = get_timestamp()
                                transaction_code = code_generator()
                                promotional_msg = random_messages()
                                print(f"{transaction_code}.Comfirmed {loan_amount} has been debited to your mshwari account at {timestamp} new M-shwari balance {mshwari_bal}\n"
                                      f"{promotional_msg}")
                            else:
                                print("You have entered a wrong pin ")
                        else:
                            print("You are illegible for a loan at this moment")
                    elif mshwari_loan_options == "2" :
                        pay_mshwari_loan_options = input("Choose one way \n1. Pay via Mpesa\n2. Pay via M-shwari")
                        if pay_mshwari_loan_options == "1":
                            mshwari_payment = int(input("Enter the amount you are willing to pay."))
                            if get_pin(my_pin):
                                balance -= mshwari_payment
                                loan_limit += mshwari_payment
                                timestamp = get_timestamp()
                                transaction_code = code_generator()
                                promotional_msg = random_messages()
                                print(f"{transaction_code}Confirmed. You have paid {mshwari_payment} at {timestamp} from Mpesa your new M-shwari loan limit is {loan_limit} "
                                      f"while your Mpesa balance is {balance}\n {promotional_msg}")



                    elif mshwari_loan_options == "3":
                        print(f"Your Mshwari loan limit is {loan_limit}")

                elif mshwari_option == "5":
                    print("Fixed savings account")
                elif mshwari_option == "6":
                    promotional_msg = random_messages()
                    print(f"Your M-shwari balance is {mshwari_bal}\n"
                          f"{promotional_msg}")

            elif loans_option == "2":

                kcb_option = input(
                    "Choose option: 1.deposit from mpesa, 2. withdraw from mpesa, 3.loan @ 8.93% for 30 days, 4.fixed savings account, 5.my account : ")

                if kcb_option == "1":
                    print("Deposit from M-pesa")
                elif kcb_option == "2":
                    print("Withdraw to M-Pesa")
                elif kcb_option == "3":
                    print("Lock savings account")
                elif kcb_option == "4":
                    print("Loan @ 8.93% for 30 days")
                elif kcb_option == "5":
                    print("Fixed savings account")
                elif kcb_option == "6":
                    print("My account")

        elif mpesa_option == "5":

            lipa_option = input("Choose option: 1. Paybill, 2. Buy goods and services, 3. Pochi la biashara : ")

            if lipa_option == "1":
                print("Paybill")
            elif lipa_option == "2":
                print("Buy goods and services")
            elif lipa_option == "3":
                print("Pochi la biashara")

        elif mpesa_option == "6":

            myaccount_option = (input(
                "Choose option: 1. Mini statement, 2. Mpesa pin manager, 3. Change language, 4. Update customer, 5. Check balance "))

            if myaccount_option == "1":
                print("1. Mini statement")
            elif myaccount_option == "2":
                print("2. Mpesa pin manager")
                old_pin = (int(input("Enter the old pin")))
                if old_pin == my_pin:
                    new_pin = (int(input("Enter the New Pin")))
                    new_pin_confirmation = (int(input("Enter the New Pin again")))
                    if new_pin == new_pin_confirmation:
                        my_pin = new_pin
                        print("You have successfully changed your pin")
                    else:
                        print("The two Pins do not match")
                else:
                    print("You entered and invalid pin")

            elif myaccount_option == "3":
                print("3. Change language")
            elif myaccount_option == "4":
                print("4. Update customer")
            elif myaccount_option == "5":
                print(mpesa_balance)
