# phonebook


# base
users = {   "user_1" : "80984567123",
            "user_2" : "80984567124",
            "user_3" : "80984567125",
            "user_4" : "80984567126",
            "user_5" : "80984567127",
            "user_6" : "80984567128",
            "user_7" : "80984567129",
            "user_8" : "80984567130",
            "user_9" : "80984567131",
            "user_10" : "80984567132"
}



# add new phones to base
new_user = str(input("write down new_user_name:"))
user = new_user.capitalize()


new_phone = input("write down new_user_phone:")
phone = new_phone.replace("", "-")


users.update({user : phone})

for key in users:
    print(key, " - ", users[key])
