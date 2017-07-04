import random
import string
import getpass
def encryption():
    inputpassword1 = getpass.getpass("Password: ")
    password1 = ("")
    if password1 == inputpassword1:
        encrypt = input("Type something for encryption: ")
        def add_str(lst):
            _letters = ("1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","!","#","$","%","&","/","(",")","=","?","*","+","_","-",";"," ")
            return [''.join(random.sample(set(_letters), 2)) + letter + ''.join(random.sample(set(_letters), 2))for letter in lst]

        print(''.join(add_str(encrypt)))
        input("")
    else:
        print("Wrong password")
        input("")
def generate():
    passwdinput2 = getpass.getpass("Password: ")
    passwd2 = ("")
    if passwdinput2 == passwd2:
        karakteri=("1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","!","#","$","%","&","/","(",")","=","?","*","+","_","-",";")
        user_input=input("How many characters do you want?(6-15): ")
        if user_input == "6":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "7":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "8":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "9":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "10":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "11":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "12":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "13":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "14":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "15":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        else:
            print("Error,make sure its 6-15 characters")
            input("")
    else:
        print("Wrong password")
        input("")
def decryption():
    passwdinput = getpass.getpass("Password: ")
    passwd = ("")
    if passwd == passwdinput:
        s = input("Type something for decryption: ")
        print(s[2::5])
        input("")
print("Welcome!")
choice = input("Choose:Encrypt(e),Decrypt(d),Generate password(p): ")
if choice == ("e"):
    encryption()
elif choice == ("d"):
    decryption()
elif choice == ("p"):
    generate()
    input("")
else:
    print("Error,choose e,d or p.")
    input("")



        


        
        
                      
    




