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
# if new_user == True:
#     users.apdate([new_user])

new_phone = int(input("write down new_user_phone:"))
# if new_phone == True:
#     users.apdate([new_phone])



users.update({new_user : new_phone})

for key in users:
    print(key, " - ", users[key])
