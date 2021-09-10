import random, string, time
from colorama import Fore

print(Fore.GREEN +"""
    
   ___               __           ___                                 _______                      __          
  / _ \___ ____  ___/ /__  __ _  / _ \___ ____ ____    _____  _______/ / ___/__ ___  ___ _______ _/ /____  ____
 / , _/ _ `/ _ \/ _  / _ \/  ' \ / ___/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
/_/|_|\_,_/_//_/\_,_/\___/_/_/_/_/   \_,_/___/___/__,__/\___/_/  \_,_/\___/\__/_//_/\__/_/  \_,_/\__/\___/_/  

                                                                    twitter alii76tt
""")

digits = list(string.digits)
special_characters = list(string.punctuation)
small_letters = list(string.ascii_lowercase)
capital_letters = list(string.ascii_uppercase)

all_characters = list(digits + special_characters + small_letters + capital_letters)

class generateRandomPassword():

    def generatePassword(self, passwordLength):
        self.length = passwordLength
        self.password = list()

        try:

            digitsCount = int(input("\nEnter digits count in password: "))
            specialCharactersCount = int(input("Enter special characters count in password: "))
            smallLettersCount = int(input("Enter small letters count in password: "))
            capitalLettersCount = int(input("Enter capital letters count in password: "))

            totalCharacters = digitsCount + specialCharactersCount + smallLettersCount + capitalLettersCount

            if totalCharacters > passwordLength:
                
                response = input("Characters total count is greater than the password length. Still create password?(Y/N): ")
                
                if response == "Y":
                    
                    for i in range(digitsCount):
                        self.password.append(random.choice(digits))

                    for i in range(specialCharactersCount):
                        self.password.append(random.choice(special_characters))
                    
                    for i in range(smallLettersCount):
                        self.password.append(random.choice(small_letters))

                    for i in range(capitalLettersCount):
                        self.password.append(random.choice(capital_letters))
                    
                    random.shuffle(self.password)               
                    print("Your password is scrambled for your security...")
                    time.sleep(1)
                    
                    newPassword =""
                    newPassword = newPassword.join(self.password)

                    print("Your password:" + newPassword)

                else:
                    print("Could not create password.")
            else:
                self.randomPassword(totalCharacters, digitsCount, specialCharactersCount, smallLettersCount, capitalLettersCount)
        except Exception:
            print("Something went wrong")
        

    def randomPassword(self, totalCharacters, digitsCount, specialCharactersCount, smallLettersCount, capitalLettersCount):
        self.totalCharacters = totalCharacters
        self.digitsCount = digitsCount
        self.specialCharactersCount = specialCharactersCount
        self.smallLettersCount = smallLettersCount
        self.capitalLettersCount = capitalLettersCount

        random.shuffle(all_characters)

        if (passwordLength - totalCharacters) == passwordLength:
            for i in range(passwordLength - totalCharacters):
                self.password.append(random.choice(all_characters))
                            
        elif totalCharacters <= passwordLength:   
            for i in range(digitsCount):
                self.password.append(random.choice(digits))

            for i in range(specialCharactersCount):
                self.password.append(random.choice(special_characters))
                    
            for i in range(smallLettersCount):
                self.password.append(random.choice(small_letters))

            for i in range(capitalLettersCount):
                self.password.append(random.choice(capital_letters))
                
            for i in range(passwordLength - totalCharacters):
                self.password.append(random.choice(all_characters))


        random.shuffle(self.password)        
        print("Your password is scrambled for your security...")
        time.sleep(1)
                                
        newPassword = ""
        newPassword = newPassword.join(self.password)
        print("Your password:" + newPassword)   

generator = generateRandomPassword()
while True:
    
    try:
        passwordLength = int(input("Enter password length(default:8): "))
        if passwordLength < 8 or passwordLength < 0:
            print(f"Please enter minimum 8 character and a positive number! Number of Characters you entered:{passwordLength}")
        else:
            generator.generatePassword(passwordLength)
            break
    except (TypeError, ValueError):
        print("Please enter number!")


    


