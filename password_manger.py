import csv
from csv import DictWriter

admin_pass_ask = input('Enter Password : ')
if admin_pass_ask == 'hello':
    print('Hello\nNice to help\nWhat do you want to do :-')
    while True:
        print('\n1.)All Passwords\n2.)Store Password\n3.)Get New Password')
        what_to_do = input('Enter (1/2/3) : ')
        if what_to_do == '1' or what_to_do == 'All Passwords' or what_to_do == 'all passwords':
            with open ('Games Accounts.csv','r') as file:
                csvreader = csv.reader( file )
                fields = next( csvreader )
                for row in file:
                    print(row.replace(",","\n"))
        elif what_to_do == '2' or what_to_do == 'Store Password' or what_to_do == 'store password':
            ask_service = input('Which Service : ')
            ask_email = input("Which Email : ")
            ask_password = input('Which Password : ')
            with open ("Games Accounts.csv","a") as f:
                dict_writer = DictWriter(f, fieldnames=["service","email","password"])
                dict_writer.writerow({
                    'service':"service - "+ask_service,
                    'email':"email - "+ask_email,
                    "password":"password - "+ask_password
                })
            print('Done !')
        elif what_to_do == '3' or what_to_do == 'Get New Password' or what_to_do == 'get new password':
            import random
            passlen = int(input('Length of Password : '))
            print('What Type Of Password Combination :\n'
                  '1.)abc+123+ABC+(#$&)\n'
                  '2.)abc+123+(#$&)\n'
                  '3.)abc+(#$&)')
            type_pass = input('Enter (1/2/3/4): ')
            if type_pass == '1':
                s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
                p = "".join( random.sample( s, passlen ) )
                print(p)
            elif type_pass == '2':
                abc = 'abcdefghijklmnopqrstuvwxyz'
                numbers = '0123456789'
                hashs = '!@#$%^&*'
                s = abc+numbers+hashs
                p = "".join( random.sample( s, passlen ) )
                print( p )
            elif type_pass == '3':
                abc = 'abcdefghijklmnopqrstuvwxyz'
                hashs = '!@#$%^&*'
                s = abc + hashs
                p = "".join( random.sample( s, passlen ) )
                print( p )
        else:
            print('Invalid Input')

