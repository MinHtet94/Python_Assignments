import json
import os

class MiniBank:
    def __init__(self, filename="users.json"):
        self.filename = filename
        # load user data from file or create new empty file
        self.main_userInfo = self.load_data()

    # ------------------ File Handling ------------------
    def load_data(self):
        """Load user data from JSON file."""
        if os.path.exists(self.filename): #checks whether the JSON file (e.g., users.json) exists in folder.
            with open(self.filename, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}
    # ----------------- save data ---------------- #

    def save_data(self):
        
        with open(self.filename, 'w') as f:
            json.dump(self.main_userInfo, f) #covert python object into json text and write into file

    # ------------------ Menu Options ------------------
    def firstOption(self):
        option: int= int(input("Press 1 to login : \nPress 2 to Register : \nPress 3 to quit : "))
        if option == 1:
            self.login()
        elif option == 2:
            self.register()
        elif option == 3:
            return True
        else:
            return False
            

    def returnId(self, transfer_username):
        for user_id, user_data in self.main_userInfo.items():
            if user_data["r_username"] == transfer_username:
                return user_id
        return None
            

    def menu(self, loginId):
        while True:
            menu_input=int(input(" Enter 1 to transfer : \n Enter 2 to withdraw : \n Enter 3 to update : \n Enter 4 to quit : "))
            if menu_input == 1:
                transfer_username = input("Enter the username want to transfer : ")
                transfer_id = self.returnId(transfer_username)
                if not transfer_id:
                    print("User not found!")
                    continue
                amount = int(input(f"Enter the transfer amount to {self.main_userInfo[transfer_id]['r_username']} : "))
                if amount > self.main_userInfo[loginId]["r_useramount"]:
                    print ("You can't transfer, not enough balance.")
                else:
                    self.main_userInfo[loginId]["r_useramount"] -= amount
                    self.main_userInfo[transfer_id]["r_useramount"] += amount
                    print ("Your balance is ", self.main_userInfo[loginId]["r_useramount"])
                    self.save_data()   # save after transfer

            elif menu_input == 2:
                amount = int(input("Enter withdraw amount: "))
                if amount > self.main_userInfo[loginId]["r_useramount"]:
                    print(" Not enough balance!")
                else:
                    self.main_userInfo[loginId]["r_useramount"] -= amount
                    print(" Withdraw successful!")
                    print("Your balance is", self.main_userInfo[loginId]["r_useramount"])
                    self.save_data()   # save after withdraw

            elif menu_input == 3:
                new_name = input("Enter new username: ")
                new_pass = int(input("Enter new passcode: "))
                new_amount= int(input ("Enter new amount: "))
                self.main_userInfo[loginId].update({
                    "r_username": new_name,
                    "r_userpasscode": new_pass,
                    "r_useramount": new_amount
                })
                print(" Update successful!")
                print("Updated info:", self.main_userInfo[loginId])
                self.save_data()   # save after update

            elif menu_input == 4:
                print("Exiting menu (1 transfer, 2 withdraw, 3 update).")
                break  

            else:
                print("Invalid option, try again.")


    def login(self):
        print ("\n____________This is from Login____________\n")
        l_username= input("Enter your username : ")
        l_userpasscode = int(input("Enter your passcode : "))
        loginId=self.exitUser(l_username, l_userpasscode)
        if loginId:
            print("Username exists, you can enter ")
            print("\n\n____Welcome____",l_username,"\n\n")
            self.menu(loginId)
        else:
            print("User cannot enter (wrong credentials)")
        

    def exitUser(self, l_username, l_userpasscode):
        for user_id, user_data in self.main_userInfo.items():
            if user_data["r_username"] == l_username and user_data["r_userpasscode"] == l_userpasscode:
                return user_id
        return None

    def register(self):
        print ("\n____________This is from Register____________\n")
        r_username = input("Enter your username : ")
        r_userpasscode = int(input("Enter your passcode : "))
        r_userpasscode2 = int(input("Enter your passcode again : "))
        r_useramount = int(input("Enter your money amount : "))

        if r_userpasscode2 == r_userpasscode:
            new_id = str(self.checkingUserCount())   # use string keys for JSON
            self.main_userInfo[new_id] = {
                "r_username": r_username,
                "r_userpasscode": r_userpasscode,
                "r_useramount": r_useramount
            }
            self.save_data()
            print("### Successful Registered ###")
            print(self.main_userInfo)
        else:
            print("Passcodes do not match!")

    def checkingUserCount(self):
        return len(self.main_userInfo) + 1


if __name__=="__main__":
    minbank = MiniBank()
    while True:
        exit_program = minbank.firstOption()
        if exit_program:
            print ("_____Bye Bye______")
            break
