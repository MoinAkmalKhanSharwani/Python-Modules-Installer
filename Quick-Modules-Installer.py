import os
import getpass
import sys
user = getpass.getuser()
def platform1():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]
try:
    if platform1()== "Windows":
        pass
    else:
        print("This software is only for Windows sorry")
        sys.exit()
    def lable():
        print("""
        ##############################
        #           Python           #
        #   Quick Modules Installer  #
        ##############################
    """)
    lable()
    while True :
        mod = input("Enter the Name of Python Module to install : ")
        if mod:
            if mod.lower() == "exit":
                print("\nReload this program to install new Modules of Python.")
                sys.exit()
            else:
                veri = os.listdir("C:\\Users\\{}\\AppData\\Local\\Programs\\Python".format(user))
                if len(veri) ==2:
                    pyveri1,pyveri2 = veri[0],veri[1]
                    print("You have two folder in your python file or you install two versions of python.")
                    print("(1)",pyveri1)
                    print("(2)",pyveri2)
                    print("Please select your python folder")
                    while True:
                        try:
                            ans1 = input("Type 1 to select {} or Type 2 to select {} : ".format(pyveri1,pyveri2))
                            if ans1:
                                if ans1 == "1":
                                    veri =pyveri1
                                    break
                                elif ans1 == "2":
                                    veri =pyveri2
                                    break
                                elif  ans1.lower()[0:6] == pyveri1.lower()[0:6] or ans1.lower()[0:6] == pyveri2.lower()[0:6]:
                                    print("Please Type the number of python folder. But you name of python folder.  ")
                                    continue
                                else:
                                    print("Error : {} not found".format(ans1))
                                    continue
                            else:
                                print("Error : Please select the number of your python folder")
                                continue
                        except ValueError:
                            print("ValueError: {} not found The Number of folder must be a number".format(ans1))
                            continue
                    os.system("cd C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\{}\\Scripts && pip.exe install {}".format(user,veri,mod))
                    more = input("Do You want to install more ? [Yes/No] : ")
                    if more.lower()=="yes" or  more.lower()=="y":
                        lable()
                        continue
                    else:
                        break
                        sys.exit()
                elif len(veri)>2:
                    def versioninfo():
                        print("You have many versions of python. Please Select your python folder.")
                        for i in range(0,len(veri)):
                            pyveri = veri[i]
                            print("({})".format(i), pyveri)
                        print("You have many versions of python. Please Select your python folder.")
                        while True:
                            try:
                                foldernum=int(input("Type the Number of your python folder which show in display : "))
                                if foldernum:
                                    if foldernum > i:
                                        print("Error: {} not found. \nThe number you type is too high and not found in the list of folders.".format(foldernum))
                                        continue
                                    else:
                                        break
                            except ValueError:
                                print("ValueError: The Folder Number must be a number. Please type a number.")  
                                continue                      
                        gen = veri[foldernum]
                        return gen
                    veri = versioninfo()
                    os.system("cd C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\{}\\Scripts && pip.exe install {}".format(user,veri,mod))
                    more = input("Do You want to install more ? [Yes/No] : ")
                    if more.lower()=="yes" or  more.lower()=="y":
                        lable()
                    else:
                        print("{} ThanksYou for using.......".format(user))
                        sys.exit()
                else:
                    x = str(*veri)
                    os.system("cd C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\{}\\Scripts && pip.exe install {}".format(user,x,mod))
                    more = input("Do You want to install more ? [Yes/No] : ")
                    if more.lower()=="yes" or  more.lower()=="y":
                        lable()
                    else:
                        print("{} ThanksYou for using .......".format(user))
                        sys.exit()
        else:
            print("Please Type Module Name or type Exit to exit.")
            continue
except Exception as e:
    print("Error : ",e,"\nPlease Try again")
