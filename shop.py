#This is a simple Coffeeshop script a bit of a demo #
import pyfiglet
from word2number import w2n
ascii_banner = pyfiglet.figlet_format("Drews Coffee")
print(ascii_banner)

print ("Hi Welcome to Drews Coffee ! ")
name = input ("Can i take your name please \n \n")
menu = " Americano, Latte, Cappucino, "
price = 8

#Adding the coffee shop bouncer, nobody allowed called Ben#

if name == "Ben":
    print (" BANNED .. NOT ALLOWED")
    exit()
else:
    print ( "Hi " + name + " Check out our Menu \n \n" + menu )


selection = input ("\n What can i get you ?")

print ("Great choice! " + selection )

amount = input( "\n How many " + selection + "'s would you like ? ")


total = price * int(amount)


# can do it like this too and reference the absolute - absolutetotal = str(total)


everything = input ( " Brilliant! is that everything ? \n")

if everything == "yes":
    print ( "That will cost you £ " + str(total))
else:
    print (" What else can i get you ?")



