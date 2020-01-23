print('Welcome to Smart Stay'.center(200))
input('Choose an Option:\n1.Log in\n2.Create an account')
option=int(input('>>'))
if option==1:
    usr_name=input("User Name:")
    try:
        file1=open(usr_name,'r')
        file1.seek(0)
        pwd=file1.readline()
        if input('Password')==pwd[0:len(pwd)-1]:
            pass
        else:
           print('Incorrect Password')
    except:
        print('User Name don\'t exit.' )
if option==2:
    user_name= input('User Name:')
    file = open(user_name, 'w+')
    password = input('Password:')
    name=input('First Name:')
    name1=input('Middle Name:')
    name2=input('Last Name:')

    address=input('Address:')
    phone_number=input('Phone Number')
    email=input('Email address:')
    services=input('Services with charges')
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
    file.writelines(services)
    file.writelines('\n')







