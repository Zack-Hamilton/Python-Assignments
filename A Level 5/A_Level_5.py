HeadPtr = -1
FreePtr = 0

def menu():
    print("1) Add Item")
    print("2) Remove Item")
    print("3) Traverse")
    print("4) Search")
    print("5) Quit")
    
def init(Arr,NextPt):
    HeadPtr =  -1
    FreePtr =  0

    for i in range(0,9):
        Arr[i] = ""
        NextPt[i] = i + 1

    Arr[9] = ""
    NextPt[9]  = -1

def traverse(Arr,NextPt):
    global HeadPtr
    global FreePtr

    if (HeadPtr == -1):
        print("Linked List is empty")
    else:
        CurrentPtr = HeadPtr
        while (CurrentPtr != -1):
            print(Arr[CurrentPtr])
            CurrentPtr = Next[CurrentPtr]
    return;

def main():
    Data = [""] * 10
    NextPtr = [0] * 10
    choice = 0

    menu();

    choice = int(input("Enter your choice"))
    while choice != 5:
        if (choice == 3):
            traverse(Data,NextPtr);

main();

