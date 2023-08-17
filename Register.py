import time as t

print(f'''
    Welcome To Python Group 2 Admin Project System
        press 1 to create an account now!
''')


#  Function for Creating and Login into the Account
def register():
    max_creating = 5
    attempt = 0
    while attempt < max_creating:
        reg_username = input("Enter your Username: ")
        password1 = input("Enter your Password: ")
        password2 = input("Confirm Password: ")

        attempt += 1

        if password1 == password2:
            t.sleep(3)
            print(f'''
                            Account Created,  🎉 You Can Now Login
                            ''')

            max_attempt = 3
            attempt = 0
            while attempt < max_attempt:
                username = input("Enter your Username: ")
                password = input("Enter your Password: ")
                attempt += 1
                if password == password1 and username == reg_username:
                    t.sleep(3)
                    print(f'''
                                    Login Succesfully 🎉 as {username}
                                    ''')
                    break
                else:
                    print("Login Unsuccessful, Username or Password NOT correct.")

                if (attempt == max_attempt):
                    print("You've Exceeded the Number of Attempts...Try again Later")

            break

        else:
            print("Password Must Correspond to Continue.")



first_step = input("To Create an Accout press '1': ")
if (first_step == '1'):

    register()

    t.sleep(3)
    print(f'''
    Welcome To Admin Dashboard,  🎉 Have a Nice Day!!''')

    add = int(input("press '1' to Store and Retrieve employee Information. "))
    if add == 1:
        t.sleep(1)

        # Employee empty dict.
        employee = {}

        for i in range(5):
            name = input("Enter employee's name: ")
            age = int(input(f'''Enter {name}'s age: '''))

            if name not in employee:
                employee[name] = age

        # print(employee)

        showage = int(input("Enter '1' to retrieve employee below 25 years: "))
        if showage == 1:
            t.sleep(2)
            c = dict((key, value) for (key, value) in employee.items() if value < 25)
            print('List Of employee less than 25 and their actual age.')

            # loop to retrieve key and values of employuee dict..
            for x, y in c.items():
                print(f'{x} is {y} years old')

        else:
            print("Please try again and follow instructions.")
    else:
        print("Please try again and follow instructions.")



else:
    print("Please Try Again and follow Instructions")


