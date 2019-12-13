#program to set key and value by the user

#creating empty dictionary
'''dic={}
a='yes'
while a=='yes':
    key=input("Enter your key value")
    value=input("Enter your value for the key")
    if value.isdigit()==True:
        value=int(value)
    else:
        value=value
#inserting entered key and value to the dictionary
    dic[key]=value

    a=input('type yes to add more')
print(dic)'''


#program to verify the email entered by the user
#importing regular expression
import re
import sys
reinput='yes'

email=input("Enter your email")
pattern='^.*@.*$'
var=re.match(pattern,email)
if var:
    print("Email matched")
else:
    sys.exit("INVALID EMAIL")