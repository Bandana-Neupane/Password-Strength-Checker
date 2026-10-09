# Password_Strength_Checker
import re
# conditions for strong Password
# min 8 digits, digit, upper case, lower case, special character
def check_password_strength(Password):
    if(len(Password))<8:
        return("Weak password:Need at least 8 charcters")
    if not any(char.isdigit() for char in Password):
        return("Weak Password:Need at least 1 digit")
    if not any(char.isupper() for char in Password):
        return("Weak Password:Need uppercase letters")
    if not any(char.islower()for char in Password):
        return("Weak Password:Need lowercase letters")
    if not re.search(r'["#\$%&\'\(\)\*\+,\./:;<=>\?@\[\\\]\^_`\{\|\}~-]',Password):
        return("Medium Password:Need a special character")
    
    return("Strong Password: Your Password is secured")

def Password_checker():
    while True:
        Password =input("Enter your password (or Type exit to end)")
        if Password.lower()=='exit':
            print("Thankyou for using this tool")
            break
        result= check_password_strength(Password)
        print(result)

# Run the Password_checker first
if __name__=="__main__":
    Password_checker()

        
               


    