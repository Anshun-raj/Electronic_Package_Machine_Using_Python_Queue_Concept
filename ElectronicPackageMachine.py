class Machine:
    Queue = []
    count=0
    def appendPackage(self):
        ele=int(input("Enter the data:-"))
        Machine.Queue.append(ele)

    def removePackage(self):
        if not Machine.Queue:
            print("Queue is empty")
        else:
            Machine.Queue.pop(0)

    def totalPackage(self):
        for i in range(len(Machine.Queue)):
            Machine.count+=1
            print("Total product inside the machine are",Machine.count)

    def showPackage(self):
        print("The product which is inside the machine are",Machine.Queue)

obj=Machine()

while(True):
    print("There is a machine which collect package")
    print("\nPackage has been completely shielded using the machine")
    print("\nthere are some functionality inside the machine for which some number is assign to each product")
    print("\nPress 1. to add package to the machine")
    print("\nPress 2. to remove package from the machine")
    print("\nPress 3. to count the no. package in the machine")
    print("\nPress 4. to print package which is inside the machine")
    choice=int(input("Enter your choice:-"))
    if(choice==1):
        obj.appendPackage()
    elif(choice==2):
        obj.removePackage()
    elif(choice==3):
        obj.totalPackage()
    elif(choice==4):
        obj.showPackage()
    else:
        exit()


