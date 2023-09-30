#There are 3 clients named as sonu , monu & tonu
# create total 6 files - write a function that takes client name  as input when executed (3 files to lock food & 3 for locking exercise)
# ask for whom among 3 you want to choose (press -  1 for sonu , 2 for monu , 3 for tonu)


name = input("Enter Your Name: ")

def getDate():
    import datetime
    return datetime.datetime.now()

value = int(input("Type 1 to Add and 2 To Retrieve: "))

def healthManager(values):
    choose = int(input("Type 1 for Food and 2 for Exercise: "))
    if values == 1:
        if choose == 1:
            food = input("Write your diet use comma to separate: ")
            # I had created this exercise file in a exercise folder so i used ".." to get
            #      to my files folder in which i stored all file.txt
            with open("file" + name + "food.txt", "a") as writeFood:
                writeFood.write("[ " + str(getDate()) + " ]" + ": " + food + "\n")
            print("Added Successfully")
        else:
            exercise = input("Write your Exercise use comma to separate: ")
            with open("file" + name + "exec.txt", "a") as writeExer:
                writeExer.write("[ " + str(getDate()) + " ]" + ": " + exercise + "\n")
            print("Added Successfully")
    else:
        if choose == 1:
            with open("file" + name + "food.txt") as getFood:
                for foods in getFood:
                    print(foods, end="")
        else:
            with open("file" + name + "exec.txt") as getExer:
                for exercises in getExer:
                    print(exercises, end="")


healthManager(value)