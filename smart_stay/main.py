import os

print('Welcome to Smart Stay'.center(150))
print('''Choose an option:
1.Host
2.Customer''')
option = input('>>')
if option == '2':
    print('Choose an Option:\n1.Log in\n2.Create an account\n3.Use as Guest')
    option = int(input('>>'))
    if option == 1:
        try:
            usr_name = input("User Name:")
            file1 = open(usr_name, 'r')
            file1.seek(0)
            pwd = file1.readline()
            if input('Password') == pwd[0:len(pwd) - 1]:
                print('Home Stays:')
                homestay = open('homestay', 'r')
                for i, line in enumerate(homestay):
                    print(i ,'.' + line,sep='')
                print('Choose an option:\n1.Search with address\n2.Select\n3.Quit')
                option = int(input())
                if option == 1:
                    address = input('Where are you going?')
                    file1 = open(address, 'r')
                    print('Home Stays:')
                    for i, line in enumerate(file1):
                        print(i , '.' + line,sep='')
                    choice = input('Enter the homestay you wish to stay')
                    file2 = open(choice[0,len(choice)-1], 'r')
                    details = file2.readlines()
                    print('Name:', choice)
                    print('Location:', details[3])
                    print('No. of rooms aviable:', details[6])
                    print('Services:', details[5])
                    print('Charge for a room:', details[7])
                    print('Contact no.', details[4])
                    print('Do you want to book?')
                    choice1 = input('Yes or No:').lower()
                    if choice1 == 'yes':
                        num_of_rooms = input('Number of rooms')
                        booking = open('booking_' + choice1, 'w+')
                        booking.writelines(usr_name)
                        booking.writelines('\n')
                        booking.writelines(num_of_rooms)
                        booking.writelines('\n')
                        booking.writelines(input('Write services you want:'))
                        booking.writelines('\n')
                    else:
                        print('Thanks for using our app.')
            else:
                print('Incorrect Password')
        except:
            print('User Name don\'t exit.')
    if option == 2:
        user_name = input('User Name:')
        if os.path.exists(user_name) == True:
            print('User name already exist')
            user_name = input()
        else:
            file = open(user_name, 'w+')
        password = input('Password:')
        name = input('First Name:')
        name1 = input('Middle Name:')
        name2 = input('Last Name:')
        address = input('Address:')
        phone_number = input('Phone Number')
        id = input('Identification Number')
        email = input('Email address:')
        file.seek(1)
        email1 = file.readline()
        if email1[0:len(email1) - 1] != email:
            file.writelines(password)
            file.writelines('\n')
            file.writelines(email)
            file.writelines('\n')
            file.writelines(name + ' ' + name1 + ' ' + name2)
            file.writelines('\n')
            file.writelines(address)
            file.writelines('\n')
            file.writelines(phone_number)
            file.writelines('\n')
            file.writelines(id)
            file.writelines('\n')

    if option == 3:
        name = input('First Name')
        name1 = input('Middle Name')
        name2 = input('Last Name')
        country = input('Country')
        usr_name = "guest_" + name + '_' + country
        file2 = open(usr_name, 'w+')
        contact = input('Contact Information')
        file2.writelines(name + ' ' + name1 + ' ' + name2)
        file2.writelines("\n")
        file2.writelines(country)
        file2.writelines('\n')
        file2.writelines(contact)
        print('Home Stays:')
        homestay = open('homestay', 'r')
        for i, line in enumerate(homestay):
            print(i ,'.' + line,sep='')
        print('Choose an option:\n1.Search with address\n2.Select\n3.Quit')
        option = int(input())
        if option == 1:
            address = input('Where are you going?')
            file1 = open(address, 'r')
            print('Home Stays:')
            for i, line in enumerate(file1):
                print(i , '.' + line,sep='')
            choice = input('Enter the homestay you wish to stay')
            file2 = open(choice, 'r')
            details = file2.readlines()
            print('Name:', choice)
            print('Location:', details[3])
            print('No. of rooms aviable:', details[6])
            print('Services:', details[5])
            print('Charge for a room:', details[7])
            print('Contact no.', details[4])
            print('Do you want to book?')
            choice1 = input('Yes or No:').lower()
            if choice1 == 'yes':
                num_of_rooms = input('Number of rooms')
                booking = open('booking_' + choice1, 'w+')
                booking.writelines(usr_name)
                booking.writelines('\n')
                booking.writelines(num_of_rooms)
                booking.writelines('\n')
                booking.writelines(input('Write services you want:'))
                booking.writelines('\n')
            else:
                print('Thanks for using our app.')



elif option == '1':
    print('Choose an option:\n1.Log in\n2.Create an account')
    option = int(input('>>'))
    if option == 1:
        try:
            usr_name = input("User Name:")
            file1 = open(usr_name, 'r')
            file1.seek(0)
            pwd = file1.readline()
            if input('Password') == pwd[0:len(pwd)]:
                print('Booking')
                booking = open('booking_' + usr_name, 'r')
                for i, line in enumerate(booking):
                    print(i ,'.' + line,sep='')
                print('Whose details you want to see?')
                option = (input('Enter the user name'))
                file4 = open(option, 'r+')
                detail = booking.readlines()
                details = file4.readlines()
                print('Name:', details[2])
                print('Address:', details[3])
                print('No. of rooms booked:', detail[1])
                print('Services:', details[2])
                print('Contact no.', details[4])
            else:
                print('Incorrect Password')
        except:
            print('User Name don\'t exit.')
    if option == 2:
        user_name = input('User Name:')
        if os.path.exists(user_name) == True:
            print('User name already exist')
            user_name = input()
        else:
            file4 = open(user_name, 'w+')
        password = input('Password:')
        file4.writelines(password)
        file4.writelines('\n')
        name = input('Home Stay name:')
        file=open(name,'w+')
        file3 = open('homestay', 'w+')
        file3.writelines(name)
        address = input('Where are you located:')
        file2 = open(address, 'w+')
        file2.writelines(name)
        phone_number = input('Phone Number:')
        email = input('Email address:')
        room = input('No.of rooms')
        services = input('Input the services you provide:')
        charge = input('Charge per room:')
        file.writelines(password)
        file.writelines('\n')
        file.writelines(email)
        file.writelines('\n')
        file.writelines(name)
        file.writelines('\n')
        file.writelines(address)
        file.writelines('\n')
        file.writelines(phone_number)
        file.writelines('\n')
        file.writelines(services)
        file.writelines('\n')
        file.writelines(room)
        file.writelines('\n')
        file.writelines(charge)
        file.writelines('\n')
