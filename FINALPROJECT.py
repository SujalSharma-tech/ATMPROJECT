import time


RED = '\033[31m'
WHITE = '\033[m'

GREEN = '\033[32m'


t = 3
print("                Welcome to Z-Axis Bank                  ")
print('========================================================')
Card = 123456789
PIN = 8880
Chances = 4
Balance = 15000
CardNo = int(input("                Swipe your Card: "))
print('========================================================')
if CardNo == Card:
    print("                  WELC0ME USER")
    print('========================================================')
    while Chances > 0:

        PININ = int(input("             Enter your Card Pin: "))
        if PININ == PIN:
            button = 0
            while button == 0:

                print('========================================================\n')

                print('''What action you want to perform ?
                1. Withdraw Money
                2. Deposit Money
                3. Check Balance
                4. Change Pin
                5. exit\n''')
                print('========================================================\n')

                Act = int(input("Enter Option: "))
                if Act == 5:
                    print('========================================================\n')
                    print("Thank you for using Z-Axis ATM..Have a Good Day :)\n")
                    print('========================================================\n')
                    exit()
                if Act > 5:
                    print('========================================================\n')
                    # print()
                    print(RED, "Invalid Option Please try again\n", WHITE)
                    print('========================================================\n')
                    # print()
                    continue
                while Act != 5:
                    if Act == 1:
                        Withdraw = (
                            input("Enter Amount of Money you want to Withdraw or press N to see all options: "))
                        if Withdraw == "N" or Withdraw == "n":

                            break
                        Withdraw = int(Withdraw)

                        if int(Withdraw) > Balance:
                            print(
                                '========================================================')
                            print(RED, "Insufficient Balance...Try again", WHITE)
                            print(" Current Balance: {}".format(Balance))
                            print(
                                '========================================================\n')
                            continue

                        else:
                            print(
                                "Please wait while Transaction is being processed...")
                            time.sleep(t)
                            print(
                                '========================================================\n')
                            print(GREEN, "Withdrawal Succesfull\n", WHITE)
                            Balance -= Withdraw
                            print("Remaining Balance: {}\n".format(Balance))
                            print(
                                '========================================================\n')

                    elif Act == 2:

                        Deposit = (
                            input("Enter amount of money you want to deposit or Press N for all options: "))
                        if Deposit == "N" or Deposit == "n":

                            break
                        Deposit = int(Deposit)

                        print("Please wait while Transaction is being processed...")
                        time.sleep(t)
                        Balance += Deposit
                        print(
                            '========================================================\n')
                        print(GREEN, "Deposit Succesfull\n", WHITE)
                        print('Your new Balance is: {}\n'.format(Balance))
                        print(
                            '========================================================\n')

                    elif Act == 3:
                        print(
                            "Please wait while We are fetching your account balance...")
                        time.sleep(t)
                        print(
                            '========================================================\n')
                        print("Your Current Balance is: {}\n".format(Balance))
                        print(
                            '========================================================\n')
                        break

                    elif Act == 4:
                        print(
                            '========================================================\n')
                        PIN = input("Enter a four digit pin: ")
                        print()
                        print(GREEN, "Pin changed succesfully\n", WHITE)
                        print(
                            '========================================================\n')
                        break

                else:
                    print("Thank you for using Z-Axis Bank")
                # break
        else:
            Chances -= 1
            print(RED, "    Wrong Pin !, Try again ({} Chances left)".format(
                Chances), WHITE)
            if Chances == 0:
                print('========================================================')
                print(RED, "                Card Blocked !!!", WHITE)
                print('========================================================\n')
                exit()
else:
    print('========================================================')
    print(RED, "           Card number is Incorrect!", WHITE)
    print('========================================================\n')
