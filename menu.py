# import all modules
import os
import getpass


#welcome part start
os.system("tput setaf 5")
print("\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#os.system("espeak-ng Welcome: I am penuuu")

os.system("tput setaf 7")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || A Python Tool : PYMENUUU ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
os.system("tput setaf 5")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\n\n")
os.system("tput setaf 3")


#authentication part start
password = getpass.getpass("Enter Password : ")
if password != "123":
    print("Incorrect Password..Try again!!")
    exit()
else:
    print("\n\t\t\t\t\tWelcome,Now You can use all our services...\n\n")


#select option locally or remote
print("\t\t\tWhere you want to use the service : locally or remotly")
print("\t\t\tFor Local  : Press l\n\t\t\tFor Remote : Press r\n")
while True:
    option=input()
    if (option!= "l" and option!= "r"):
        print("Nor Supported Option... Again Press(l or r)!! ")
        continue;
    else:

        while True:
            os.system("clear")
            os.system("tput setaf 5")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            os.system("tput setaf 7")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || A Python Tool : PYMENUUU ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            os.system("tput setaf 5")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("\n\n\n")
            os.system("tput setaf 5")

            print('''
            \t\t\t\t\t\tPress 1 : To Perform tasks on Linux
            \t\t\t\t\t\tPress 2 : To Use Hadoop Services
            \t\t\t\t\t\tPress 3 : To Use Docker Services
            \t\t\t\t\t\tPress 4 : To Use Cloud Services
            \t\t\t\t\t\tPress 5 : Exit'''
             )
            os.system("tput setaf 3")

            ch=input("Enter Your choice : ")
            if option == "l":
                if int(ch) == 1:
                    # linux part
    
                    while True:

                        os.system("clear")
                        os.system("tput setaf 6")
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        os.system("tput setaf 7")  
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || PYMENUUU : Use Linux OS ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
                        os.system("tput setaf 6")
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
                        print("\n\n\n")
                        os.system("tput setaf 6")
    

                 # write linux main  code from here
                        print('''
                        \t\t\t\tPress 1 : To set web server
                        \t\t\t\tPress 2 : To create Partition
                        \t\t\t\tPress 3 : To LVM creation
                        \t\t\t\tPress 4 : To perform basic tasks ..
                        \t\t\t\tPress 5 : Exit From Linux Service''')

                        os.system("tput setaf 3")
                        lch=input("Enter Your choice : ")
                #if-condition for linux part

                        if int(lch) == 1:
                            print("web server set up")
                        elif int(lch) == 5:
                            break;
                        else:
                            print("option not supported")
                        input("\nPlease, Enter To Continue...")


        

                

                elif int(ch) == 2:
            #hadoop code here.
                    print("hadoop code here")

                elif int(ch) == 3:
            #docker code 
                    print("docker task")

                elif int(ch) == 4:
            #cloud 
                    print("cloud task")

                elif int(ch) == 5:
            #exit
                    exit()
        
                else:
                    print("Choose again..Option Not supported!!")
                input("Press Enter To Continue...")


            else:
                if int(ch) == 1:
            # linux code
                    print("remote perform linux task")

                elif int(ch) == 2:
            #hadoop code here.
                    print("remote hadoop code here")

                elif int(ch) == 3:
            #docker code 
                    print("remote docker task")

                elif int(ch) == 4:
            #cloud 
                    print("remote cloud task")

                elif int(ch) == 5:
            #exit
                    exit();
        
                else:
                    print("Choose again..Option Not supported!!")


                input("\nPlease,Enter To Continue....")






    


