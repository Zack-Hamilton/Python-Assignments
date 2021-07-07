HeadPtr = -1;
FreePtr = 0;

def menu():
    print("1) Add Item");
    print("2) Remove Item");
    print("3) Traverse");
    print("4) Search");
    print("5) Quit");
    
def init(Arr,NextPt):
    HeadPtr =  -1;
    FreePtr =  0;

    for i in range(0,9):
        Arr[i] = "";
        NextPt[i] = i + 1;

    Arr[9] = "";
    NextPt[9]  = -1;

def add(Arr,Next,NewItem):
    global HeadPtr;
    global FreePtr;
    
    if (FreePtr == -1):
        print("No node free.");
        print("");
    else:
        NewPtr = FreePtr;
        FreePtr = Next[FreePtr];
        Arr[NewPtr] = NewItem;
        CurrentPtr = HeadPtr;
        
        while (Arr[CurrentPtr] < NewItem) and (CurrentPtr != -1):
            PreviousPtr = CurrentPtr;
            CurrentPtr = Next[CurrentPtr];

        if (CurrentPtr == HeadPtr):
            Next[NewPtr] = HeadPtr;
            HeadPtr = NewPtr;
        else:
            Next[PreviousPtr] = NewPtr;
            Next[NewPtr] = CurrentPtr;

def remove(Arr,Next,RemItem):
    global HeadPtr;
    global FreePtr;
    
    if (HeadPtr == -1):
        print("Linked List is empty");
    else:
        CurrentPtr = HeadPtr;

        while (Arr[CurrentPtr] != RemItem):
            PreviousPtr = CurrentPtr;
            CurrentPtr = Next[CurrentPtr];

        if (CurrentPtr == HeadPtr):
            HeadPtr = Next[CurrentPtr];
        else:
            Next[PreviousPtr] = Next[CurrentPtr];    

        Arr[CurrentPtr] = 0;
        Next[CurrentPtr] = FreePtr;
        FreePtr = CurrentPtr;

def traverse(Arr,Next):
    global HeadPtr;
    global FreePtr;
    
    if (HeadPtr == -1):
        print("Linked List is empty");
        print("");
    else:
        CurrentPtr = HeadPtr;
        while (CurrentPtr != -1):
            print(Arr[CurrentPtr]);
            CurrentPtr = Next[CurrentPtr];

def search(Arr,Next):
    global HeadPtr;

    CurrentPtr = 0;

    if (HeadPtr == -1):
        print("Linked List is empty");
        print("");

        return;
    else:
        CurrentPtr = HeadPtr;
        Found = False;

        SearchItem = int(input("Enter an item to search:"));
        print("");

        while (CurrentPtr != -1):
            if (Arr[CurrentPtr] == SearchItem):
                Found = True;
                return Found;
            else:
                CurrentPtr = Next[CurrentPtr];
        
    return Found;

def main():
    Data = [0] * 10;
    NextPtr = [0] * 10;

    for i in range(0,10):
        NextPtr[i] = i + 1;
    NextPtr[9] = -1;
    
    choice = 0;

    while choice != 5:
        menu();
        choice = int(input("Enter your choice:"));
        print("");
        
        if (choice == 1):
            ItemAdd = int(input("Enter a new item:"));
            print("");

            add(Data,NextPtr,ItemAdd);

        if (choice == 2):
            ItemRemove = int(input("Enter item to remove:"));
            print("");

            remove(Data,NextPtr,ItemRemove);

        elif (choice == 3):
            traverse(Data,NextPtr);
        elif (choice == 4):
            if (search(Data,NextPtr) == True):
                print("Item found!");
                print("");
            else:
                print("Item not found.");
                print("");

main();

