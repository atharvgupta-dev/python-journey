def motivation():
    name = input("enter your name")
    time = input("what time of the day is now : 1. Morning 2. Afternoon 3. Night")
    if time == "1" :
        print (f"good morning {name}, have a nice day")
    elif time == "2" :
        print (f"afternoon it is {name}, dont stop grinding")
    elif time == "3" :
        print (f"sleep well {name}, tomorrow is waiting for you")
motivation()
