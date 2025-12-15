import random

def autoroll():

    def rolling_dice(n):
        l=[]
        for i in range(n):
            rolled=random.randint(1,6)
            l.append(rolled)
        return l
    
    print("The avaialable Auto Roll options are: ")
    print("1. 10")
    print("2. 50")
    print("3. 100")
    print("4. 500")
    print("5. Custom")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
         return rolling_dice(10)
    elif choice==2:
        return rolling_dice(50)
    elif choice==3:
        return rolling_dice(100)
    elif choice==4:
        return rolling_dice(500)
    elif choice==5:
        return rolling_dice(int(input("Enter the number of times: ")))
    else:
        print("Invalid Choice")
