def numask():
    num=[]
    for i in range(5):
        num.append(int(input("enter a number: ")))
    highest = max(num)
    lowest = min(num)
    average = sum(num)/len(num)
    print(f"highest:{highest}")
    print(f"lowest:{lowest}")
    print(f"average:{average}")
numask()
