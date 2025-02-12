#3) Simple Login System

#Write a Python program that asks the user for a username and password.

#    If the username is "admin" and the password is "1234", print "Access granted".
#    Otherwise, print "Access denied".

#Example:
#Enter username: admin 
#Enter password: 1234 
#Access granted

#Enter username: user 
#Enter password: pass 
#Access denied

#Solution:

#Adding the username and password to variables
adminuser = "admin"
adminpass = 1234

#Ask the user to enter their username and password
def login_system(adminuser, adminpass):
    username = input("Enter username: ")
    if username == adminuser:
        password = int(input("Enter password: "))
        if password == adminpass:
            access_granted()
        else:
            access_denied()
    else:
        access_denied()
    
def access_granted():
    return "access granted"

def access_denied():
    return "access denied"   

results = login_system(adminuser, adminpass)
print(results)