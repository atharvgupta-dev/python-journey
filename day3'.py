def contactbook():
    contacts={}
    while True:
        choice = int(input("1.Add , 2.Search ,3.View All , 4.Exit"))
        if choice == 1 :
            name = input("enter the name:")
            number = int(input("enter the number:"))
            contacts[name]=number
        elif choice == 2:
            searchedname = input("enter the name to be searched:")
            if searchedname in contacts :
                print(f"{searchedname}'s number is {contacts[searchedname]}")
            else :
                print("name not found")
        elif choice == 3:
            for key,value in contacts.items() :
                print(f"{key}:{value}")
        elif choice == 4:
            break
contactbook()
 

            
