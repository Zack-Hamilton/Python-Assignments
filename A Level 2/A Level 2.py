MAX = 10;
TopStack = -1

def menu():
    print("1) Push");
    print("2) Pop");
    print("3) Traverse");
    print("4) Search");
    print("5) Quit");

def init(Stack):
    global TopStack;
    for i in range (0,MAX):
        Stack [i] = '';
    TopStack = -1

def push(Stack,new_item):
    global TopStack
    if TopStack == MAX - 1:
        return False;
    else:
        TopStack = TopStack + 1;
        Stack[TopStack] = new_item;
        return True;

def pop(Stack,new_item):
    global TopStack
    if TopStack == - 1:
        return False;
    else:
        Stack[TopStack] = '';
        TopStack = TopStack - 1;
        return True;

def traverse(Stack):
    for i in range (TopStack, -1, -1):
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

def printing(data):
    for i in range (0, MAX):
        print(data[i]);

def main():
    MyStack = [''] * MAX;
    choice = 0;
    new_item = '';
    init(MyStack)
    while (choice != 5):
        menu();
        choice = int(input("Enter your choice:"));
        if (choice == 1):
            new_item = input("Enter item to push:");
            if (push(MyStack,new_item) == True):
                print("Item pushed successfully.");
            else:
                print("Error");
        elif (choice == 2):
            if (pop(MyStack,new_item) == True):
                print("Item popped successfully.");
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