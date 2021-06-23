SIZE = 10;
Tail = -1;
Head = -1;

def menu():
    print("1) Add");
    print("2) Remove");
    print("3) Traverse");
    print("4) Search");
    print("5) Quit");

def init(Stack):
    global Tail;
    global Head;
    for i in range (0, SIZE):
        Stack [i] = '';
    Tail = -1;
    Head = -1;

def add(Stack,new_item):
    global Tail;
    if (Tail == SIZE - 1):
        Tail = -1;
    if (Stack[Tail + 1] == ""):
        Tail = Tail + 1;
        Stack[Tail] = new_item;
        return True;

def remove(Stack,new_item):
    global Head;
    if Head == SIZE - 1:
        Head = -1;
    if not(Stack[Head + 1] == ""):
        Head = Head + 1;
        Stack[Head] = "";
        return True;

def traverse(Stack):
    for i in range (0, SIZE):
        print(Stack[i]);

def search(data,search_item):
    found = False;
    i = 0;
    while (i < MAX) and not(found):
        if (data[i] == search_item):
            found= True;
            return i;
        else:
            i = i + 1;
    if not(found):
        return -1;

def main():
    MyStack = [''] * SIZE;
    choice = 0;
    new_item = '';
    init(MyStack)
    while (choice != 5):
        menu();
        choice = int(input("Enter your choice:"));
        if (choice == 1):
            new_item = input("Enter item to add:");
            if (add(MyStack,new_item) == True):
                print("Item added successfully.");
            else:
                print("Error");
        elif (choice == 2):
            if (remove(MyStack,new_item) == True):
                print("Item removed successfully.");
            else:
                print("Error");
        elif (choice == 3):
            traverse(MyStack);
        elif (choice == 4):
            item_to_search = (input("Enter what you are looking for:"));
            print("");
            index = search(MyStack, item_to_search);
            if (index !=  -1):
                print("Item found at index:", index);
                print("");
            else:
                print("Item not found:", index);
                print("");

main();
