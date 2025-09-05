contact_item = {
    "lydia": "0967387834",
    "sem" : "0928049750",
    "desta" : "0911234789",
    "kidane" : "091211515",

}

print("1.Add contact")
print("2.show contact")
print("3.Delet contact")
print("4. search ")
print("5. exit") 


choose = input("input your choice (1-5)")


if choose == "1":
    contact_name = input("Enter the name:")
    Contact_phone = input("Enter the phone number:")
    print(contact_name + "added!")

elif choose == "2":
    print("Here is yours contact")
    for name, phone in contact_item.items() :
        print(name , ":", phone)

elif choose == "3":
    name = input("Enter the contact to delet")   
    if name in contact_item:
        del contact_item[name]
        print(name + "deleted!") 
    else:
        print("  SORRY Not in list")  

elif choose == "4":
    name = input("Enter ythe name to search:")
    phone = contact_item.get(name)
    contact_item.get(name)
    if phone :
        print(name ,":" , phone)
    else:
        print("not found")   
         
elif choose =="5":
    print("okay!")
else:
    print("no valid intake")  


          

  


 