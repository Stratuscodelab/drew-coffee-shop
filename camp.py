'''
:'######:::::'###::::'##::::'##:'########::'####:'##::: ##::'######:::
'##... ##:::'## ##::: ###::'###: ##.... ##:. ##:: ###:: ##:'##... ##::
 ##:::..:::'##:. ##:: ####'####: ##:::: ##:: ##:: ####: ##: ##:::..:::
 ##:::::::'##:::. ##: ## ### ##: ########::: ##:: ## ## ##: ##::'####:
 ##::::::: #########: ##. #: ##: ##.....:::: ##:: ##. ####: ##::: ##::
 ##::: ##: ##.... ##: ##:.:: ##: ##::::::::: ##:: ##:. ###: ##::: ##::
. ######:: ##:::: ##: ##:::: ##: ##::::::::'####: ##::. ##:. ######:::
:......:::..:::::..::..:::::..::..:::::::::....::..::::..:::......::::
                    stratuslabs@outlook.com
'''

import pyfiglet
  
result = pyfiglet.figlet_format("Camping", font = "banner3-D" )
print(result)

#Variable list of all camping stuff to take 

#camping_stuff = "Tent, knife, Rapberry PI, Hexi Cooker, Bag, Mobile, Portable Charger, Food, Flask, Water, Sleeping Bag"
#The list is indexed and will stay the same number so you can reference it at a later date.
#if you want to reference backwards use [-1] neat little hack
camping_list = ["Tent", "knife", "Hexi Cooker", "Bag", "Mobile", "Portable Charger", "Food", "Flask", "Water", "Sleeping Bag"]

#Print the data Class 
#print(type(camping_list))

#This list shows a String, Float, Integer and a Boolean 
camp_site = [ "Crystal Lake", 23.3, 404, True ]

me = camping_list[2]
print (me)