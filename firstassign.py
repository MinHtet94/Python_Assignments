#for first assignment

class MiniBank:

    main_userInfo:dict={}
    def firstOption(self):
        option: int= int(input("Press 1 to login : \nPress 2 to Register : \nPress 3 to quit : "))
        if option == 1:
            self.login()
        elif option ==2:
            self.register()
        elif option == 3:
            return True
        else:
            return False
            

    def returnId(self,transfer_username):
        usercount: int= len(self.main_userInfo)
        for i in range(1,usercount+1):
            if self.main_userInfo[i]["r_username"]==transfer_username:
                return i
        return None
            

    def menu(self,loginId):
        while True:
            menu_input=int(input(" Enter 1 to transfer : \n Enter 2 to widthdarw : \n Enter 3 to update : \n Enter 4 to quit"))
            if menu_input == 1:
                transfer_username = input("Enter the username want to transfer : ")
                transfer_id :int = self.returnId(transfer_username)
                print("Transfer username id is ",transfer_id," and my id is ",loginId)
                print(self.main_userInfo[transfer_id]["r_username"])
                amount :int = int(input("Enter the transfer amount {0} : ".format(self.main_userInfo[transfer_id]["r_username"])))
                print (amount)
                if amount > self.main_userInfo[loginId]["r_useramount"]:
                    print ("You can't transfer")
                else:
                    self.main_userInfo[loginId]["r_useramount"]-=amount
                    self.main_userInfo[transfer_id]["r_useramount"]+=amount
                    print ("Your balance is ", self.main_userInfo[loginId]["r_useramount"])
                print (self.main_userInfo)

            elif menu_input == 2:
                amount = int(input("Enter withdraw amount: "))
                if amount > self.main_userInfo[loginId]["r_useramount"]:
                    print(" Not enough balance!")
                else:
                    self.main_userInfo[loginId]["r_useramount"] -= amount
                    print(" Withdraw successful!")
                    print("Your balance is", self.main_userInfo[loginId]["r_useramount"])
                print (self.main_userInfo)

            elif menu_input == 3:
                new_name = input("Enter new username: ")
                new_pass = int(input("Enter new passcode: "))
                self.main_userInfo[loginId].update({
                    "r_username": new_name,
                    "r_userpasscode": new_pass
                })
                print(" Update successful!")
                print("Updated info:", self.main_userInfo[loginId])

            elif menu_input == 4:
                print("Exiting menu is 1 transfer and 2 withdraw and 3 update")
                break  # stop the loop

            else:
                print("Invalid option, try again.")


    def login(self):
        print ("\n____________This is from Login____________\n")
        l_username: str= input("Enter your username : ")
        l_userpasscode :int=int(input("Enter your passcode : "))
        exitUser=self.exitUser(l_username,l_userpasscode)
        if (exitUser):
            print("Username is exist, you can enter ")
            print("\n\n____Welcome____",l_username,"\n\n")
            loginId=self.returnId(l_username)
            self.menu(loginId)
        else:
            print("User cannot enter ")
        

    def exitUser(self,l_username,l_userpasscode):
        user_count=len(self.main_userInfo)
        for i in range(1,user_count+1):
            if self.main_userInfo[i]["r_username"] == l_username and self.main_userInfo[i]["r_userpasscode"] == l_userpasscode:
                return True
            else:
                return False

    def register(self):
        print ("\n____________This is from Register____________\n")
        r_username:str = input("Enter your username : ")
        r_userpasscode :int=int(input("Enter your passcode : "))
        r_userpasscode2 :int=int(input("Enter your passcode again : "))
        r_useramount :int =int(input("Enter your money amount : "))

        if r_userpasscode2 == r_userpasscode:
            id:int = self.checkingUserCount()
            userInfo_form:dict={id:{"r_username":r_username,"r_userpasscode":r_userpasscode,"r_useramount":r_useramount}}
            self.main_userInfo.update(userInfo_form)
            print("### Sucessful Registered ###")
            print(self.main_userInfo)


    def checkingUserCount(self):
        count = len(self.main_userInfo)
        return count+1


if __name__=="__main__":
    minbank: MiniBank = MiniBank()
    while True:
        exit_program=minbank.firstOption()
        if exit_program:
            print ("_____Bye Bye______")
            break
        
