from random import choice
import datetime as date
from datetime import date
import csv 
from tkinter import *

#password_use = input("What site are you generating a password for?: ")


pet_names1 = choice(["Tater","Chester","Georgie","Darbie"])
pet_names2 = choice(["Holmes","Cheeto","Taco","Pietro"])
number = choice(range(1986,2021))
def password_generator(pet_names1,pet_names2,number):
    password = ""
    number = str(number)
    for i in range(len(pet_names2)):
        password = pet_names2[-1] + pet_names1 + "_" + pet_names2[:-1] + number[2:]
    return password

#print("Your randomly generated password for {password_use}:  ".format(password_use=password_use)
   #   +(password_generator(pet_names1,pet_names2,number)))


#bobs burgers password generator
episode_name = ["Sexy_Dance_Fighting","Burger_War","Fingers-Loose","Drumforgiven","Boywatch"]
season_number = ["1","1","11","10","8"]
episode_number = ["4","10","17","11","17"]

Bobs_master_list = list(zip(episode_name,season_number,episode_number))
Bobs_Random_Choice = choice(Bobs_master_list)

def Bobs_burgers_password_generator(episode_list):
    password = "-".join(episode_list)
    print("Randomly generated Bob's burger's password for {password_use} is: ".format(password_use = password_use) + password)
class App(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.pack()
        self.output()

    

    def output(self):
        password_use_label = Label(text = "Password Use:").pack(side=LEFT, padx = 5,pady = 5)
        self.e_site = Entry(root, width = 10)
        self.e_site.pack(side = LEFT, padx =5, pady = 5)
        password_label = Label(text = "Password:").pack(side = LEFT, padx = 5, pady = 10)
        self.e = Entry(root, width = 10)
        self.e.pack(side = LEFT, padx = 5, pady = 8)

        self.b = Button(root, text = "Submit", command = self.save_to_csv)
        self.b.pack(side= RIGHT, padx = 5, pady = 10)
        present = date.today()
        number = choice(range(1986,2021))
        pet_names1 = choice(["Tater","Chester","Georgie","Darbie"])
        pet_names2 = choice(["Holmes","Cheeto","Taco","Pietro"])

    def password_generator(pet_names1,pet_names2,number):
        password = ""
        number = str(number)
        for i in range(len(pet_names2)):
            password = pet_names2[-1] + pet_names1 + "_" + pet_names2[:-1] + number[2:]
        return password
    
    password_generator(pet_names1,pet_names2,number)
    password_generator(pet_names1,pet_names2,number)
    def save_to_csv(self):
        
        with open("password_document.csv",'a') as myfile:
            present = date.today()
            wr = csv.writer(myfile)
            header = ["Website","Password","Date"]
            new_password = self.e.get()[-1] + str(number)
            data = [self.e_site.get(),new_password,present]
            column_names = wr.writerow(header)
            save_info = wr.writerow(data)
        #website.writerows(password_use)
       
        
#save_to_csv(password_use,password_generator(pet_names1,pet_names2,number),present)
if __name__ == "__main__":
    root=Tk()
    root.title("Password Generator")
    root.geometry("1000x100")
    #app_password = ""
    app = App(master=root)
    app.mainloop()
    root.mainloop()
