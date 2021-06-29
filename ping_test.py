#!/usr/bin/env python3
#Trevor DeWall


import os 
import subprocess 
import netifaces


#clear the screen 
os.system("clear")
#Collects User Input 
userinput = ""

#This while loop controls the program eveytime the user inputs a selection it returns to the menu until they type q. 
while userinput != "q":
    print("1- Default Gateway")
    print("2- Test DNS Server")
    print("3- Test Domain Name")
    print("q= Quit Program")
    userinput= input("Select an option: ") 
    #This if tests to see if the user can ping the default gateway. 
    if userinput == "1":
        #command to grab all ip information
        all_gateway= netifaces.gateways()
        #this is greping for the default_gateway
        #It is currently unable to handle not getting a default gateway this will be updated in a later version of the script. 
        default_gateway= all_gateway["default"][netifaces.AF_INET][0]
        #this is to iniate the ping command 
        command="ping -c 1 >/dev/null " + default_gateway
        response_default_gateway= os.system(command)
        os.system("sleep 5")
        #This will check if the result comes back as a 0 and if it does the connection is succesful. 
        if response_default_gateway  == 0:
             print("Connection Succesful")
        else:
             print("No Connection")
        os.system("sleep 3")
	#This elif is being used for testing connection to dns server    
    elif userinput == "2":
        #Subprocess is being used here for the requierments of the instruction to use subprocess once. 
        DNS_Server="129.21.3.17"
        response_DNS= subprocess.run(["ping", "-c", "1",  DNS_Server], stdout=subprocess.DEVNULL)
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
        command= "ping -c 1 > /dev/null " + hostname 
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

print("Out of loop")





#this is for remote ip testing 
#remote_ip=" 8.8.8.8"
#remote_ip_response= os.system("ping -c >/dev/null " + remote_ip)


#If block for testing hostname 
#if responsehostname == 0:
#    print("Connection")
#else:
#    print("No connection")


