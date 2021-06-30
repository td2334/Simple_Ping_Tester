#!/usr/bin/env python3
#Trevor DeWall
#Version 2 
#6/30/2021
#Notes: Version 2 now accounts for not getting a default gateway and can now handle the error instead of terminating and breaking the program.
#Version 2 also supresses more error output with stderr and the use of /dev/null 2>&1
#Any issues with the program email me at td2334@rit.edu


import os 
import subprocess 
import netifaces

#clear the screen 
os.system("clear")
#Collects User Input 
userinput = ""

#This while loop controls the program eveytime the user inputs a selection it returns to the menu until they type q. 
while userinput != "q":
    print("**********************************************************")
    print("Welcome to connection tester please select an option below")
    print("**********************************************************")
    print("1- Default Gateway")
    print("2- Test DNS Server")
    print("3- Test Domain Name")
    print("q= Quit Program")
    userinput= input("Select an option: ") 
    #This if tests to see if the user can ping the default gateway. 
    if userinput == "1":
        #command to grab all ip information
        all_gateway= netifaces.gateways()
        #This is a blank variable for default gateway
        default_gateway=" "
        #This is to catch an error if you do not get a default gateway and keep the program going. Previous version did not account for this error.
        try:
            default_gateway= all_gateway["default"][netifaces.AF_INET][0]
        except:
            print("No Gateway")
        #This prints out your default gateway to the user if not gateway it will be blank
        print("Default Gateway is " + default_gateway)
        #This build the command
        command="ping -c 1 >/dev/null 2>&1 " + default_gateway
        #This is iniating the command and getting the result back.
        response_default_gateway= os.system(command)
        os.system("sleep 5")
       # This will check if the result comes back as a 0 and if it does the connection is succesful. 
        if response_default_gateway  == 0:
            print("Connection Succesful")
        else:
            print("No Connection")
        os.system("sleep 3")
	#This elif is being used for testing connection to dns server    
    elif userinput == "2":
        #Subprocess is being used here for the requierments of the instruction to use subprocess once. 
        DNS_Server="129.21.3.17"
        #stdout and stderr are being supressed so the end user does not see them. 
        response_DNS= subprocess.run(["ping", "-c", "1",  DNS_Server], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #This is checking to see if you get a return code of 0 and if it is then the connection is a success. 
        if response_DNS.returncode==0:
            print("Connection Succesful")
        else:
            print("Connection Unsuccesful")
        os.system("sleep 3")
    #This elif tests a ping to the hostname
    elif userinput == "3":
        hostname="www.google.com"
        #Note: send output to /dev/null makes it so the user does not see the output of the ping when the command is executed
        command= "ping -c 1 > /dev/null 2>&1 " + hostname 
        responsehostname= os.system(command)
        #This is checking to see if you get a return code of 0 and if so the connection is succesful. 
        if responsehostname == 0:
            print("Connection Succesful!")
        else:
            print("No Connection")
        os.system("sleep 3")
    elif userinput == "q": 
        break; 
    else: 
        print("not valid option")

print("Program Ended")



