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
names = ["\n", fName, lName, mName]

done = False

# Keep getting names unitl done
while done == False:
    oName = input("Enter any other name. Leave empty when done: \n")
    if oName != "":
        names.append(oName)
    else:
        done = True

save = input("Enter 's' to show the passwords or complete path to append them to an existing file: ")

if save == "s":
    for i in range(len(names)):
        print(names[i] + "1234")
else:
    with open(save, 'a') as outF:
        # outF.write(names)

        # for line in names:
        #     # write line to output file
        #     outF.write(line)
        #     outF.write("\n")
        #     outF.close()

        # Python program to convert a list 
# to string using list comprehension 

        # using list comprehension 
        listToStr = '\n'.join([str(elem) for elem in names]) 
        # print(listToStr) 
        outF.write(listToStr)

