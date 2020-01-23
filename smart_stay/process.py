def costumer():
    print('Home Stays:')
    homestay = open('homestay', 'r')
    for i, line in enumerate(homestay):
        print(i + '.' + line)
    print('Choose an option:\n1.Search with address\n2.Select\n3.Quit')
    option = int(input())
    if option == 1:
        address = input('Where are you going?')
        file1 = open(address, 'r')
        print('Home Stays:')
        for i, line in enumerate(file1):
            print(i + '.' + line)
        choice = input('Enter the homestay you wish to stay')
        file2 = open(choice, 'r')
        details = file2.readline()
        print('Name:', choice)
        print('Location:', details[3])
        print('No. of rooms aviable:', details[6])
        print('Services:', details[5])
        print('Charge for a room:', details[7])
        print('Contact no.', details[4])
        print('Do you want to book?')
        choice1 = input('Yes or No:').lower()
        if choice1 == 'yes':
            num_of_rooms = int(input('Number of rooms'))
        else:
            print('Thanks for using our app.')
def host():
    pass












