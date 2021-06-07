import random;
MAX = 10;

def menu():
    print("1) Fill");
    print("2) Print");
    print("3) Linear Search");
    print("7) Quit");

def fill(data):
    for i in range (0, MAX):
        data[i] = random.randint(10,99);

def printing(data):
    for i in range (0, MAX):
        print(data[i]);

def linear_search(data,search_item):
    found = False;
    i = 0;
    while (i < MAX) and not(found):
        if (data[i] == search_item):
            found= True;
        else:
            i = i + 1;
    return found;

arr = [0] * MAX;
item_to_search = 0;
choice = 0;

while (choice != 7):
    menu();
    choice = int(input("Enter your choice:"));
    print("");

    if (choice == 1):
        fill(arr);
    elif (choice == 2):
        printing(arr);
    elif (choice == 3):
        item_to_search = int(input("Enter what you are looking for:"));
        print("");
        if (linear_search(arr, item_to_search) ==  True):
            print("Item found");
            print("");
        else:
            print("Item not found");
            print("");