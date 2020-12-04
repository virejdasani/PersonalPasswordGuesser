print("""\033[31m
MADE BY: _ _          _   _____                        _ 
 \ \    / (_)        (_) |  __ \                      (_)
  \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _ 
   \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
    \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
     \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
                    _/ |                                 
                   |__/      github.com/virejdasani                            
""")

# Get names and append to names list
fName = input("Enter target's first name:\n")
lName = input("Enter target's last name:\n")
mName = input("Enter target's middle/nickname:\n")
names = [fName, lName, mName]

done = False

# Keep getting names unitl done
while done == False:
    oName = input("Enter any other string like Date of birth and press enter/return. Leave empty when done: \n")
    if oName != "":
        names.append(oName)
    else:
        done = True

save = input("Enter 's' to show the passwords or complete path to append them to an existing file: ")

if save == "s":
    # TODO add first letter caps functionality
    for i in range(len(names)):
        print(names[i] + "12")
        print(names[i] + "123")
        print(names[i] + "1234")
        print(names[i] + "12345")
        print(names[i] + "123456")
        print(names[i] + "@12")
        print(names[i] + "@123")
        print(names[i] + "@1234")
        print(names[i] + "@12345")
        print(names[i] + "@123456")
        print(fName + lName)
        print(lName + fName)
        print(lName + " " +fName)
        print(lName + "_" +fName)

else:
    with open(save, 'a') as outF:

        # Using list comprehension 
        listToStr = '\n'.join([str(elem) for elem in names]) 
        outF.write(listToStr)

