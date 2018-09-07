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







































# file = open("C:\\Users\\MAKS\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data","r")
# print(file.read())
# file.close()

# import pyttsx
# e = pyttsx.init()
# e.say("Hello world")
# e.runAndWait()


# import warnings as pd
# x=dir(pd)
# for i in x:
#     print(i)

# import matplotlib.pyplot as plt
# fig=plt.figure("Histrogram")
# ax = fig.add_subplot(1,1,1)
# ax.hist([45,87,12,34,123,512,21,541,541],bins=7,facecolor="r",normed=True)
# plt.title("Distription")
# plt.xlabel("Range")
# plt.ylabel("Amount")
# plt.show()

# x=dir(plt)
# for i in x:
#     print(i)



# import getpass# a=getpass.getpass("Enter ")
# u = getpass.getuser()

# print(a)
# print(u)

# l = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda a: a%2 == 0 ,l)))

# l = ["moin", "akmal", "khan", "sharwani"]
# print(max(l, key = lambda item: len(item)))

# import webbrowser
# # a = dir(webbrowser)
# # for i in a:
# #     print(i)
# print(webbrowser.__doc__)

# a = {1,2,3,4,5,6,7,8,9,10}
# b= {1,2,3,4,6,7,8,9}
# print(a^b)#intersection
# print(a|b)#union
# print(a-b)#difference

# import sys
# fonct = dir(sys)
# print(sys.path)
# # for i in fonct:
# #     print(i)


# def name(a):
#     if type(a) != type("a"):
#         assert a == 3, (f"{a} = 3")
#         assert a>3, (f"{a} > 3")
#         assert a<3, (f"{a} < 3")

#     else:
#         print(f"Your string is {a.title()}")
# try:
#     name(3)
# except ValueError as e:
#     print(e)
# except AssertionError as e:
#     print(e)


# li=[]
# l = 0
# while "stop" not in li or "no" not in li:
#     if "stop" in li or "no" in li:
#         li.pop()
#         break
#     else:
#         print("\nNote :: Type no or stop to stop this")
#         l = input("Enter a item of list : ")
#         li.append(l)
# for i in range(0,len(li)):
#     rev = li[i][::-1]
#     print(rev)

# l = []
# for i in range(1,11):
#     l.append(i)
# print(l) 
# l = [i*i for i in range(1,11)]
# print(l)
