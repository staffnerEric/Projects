import random
import string

if __name__ == '__main__':
    while True:
        v=input("Save password, make password or quit? (1,2,3?) ")
        if v.lower()=="2":
            h=input("Nummber of letters? ")
            x=""
            for i in range(int(h)):
                x += random.choice(string.ascii_letters+string.digits)
            print(x)
        elif v.lower()=="1":
            d=input("look at password or save new password? (1,2?) ")
            if d.lower()=="2":
                o=input("Passwort to save: ")
                f=open("save", "a")
                f.write("\n"+o)
            elif d.lower()=="1":
                g=open("save", "r")
                print(g.read())
        elif v.lower()=="3":
            break
        else:
            print("Falsche Eingabe")