def numguess():
    import random
    i = random.randint(1,100)
    count = 0
    while True:
        guess = int(input("guess the number between 1 and 100:"))
        count+=1
        if guess > i :
            print("too high")
        elif guess < i:
            print("too low")
        elif guess == i:
            print(f"you got it right in {count} times")
            break
numguess()
                
            
            
