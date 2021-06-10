import random;
MAX = 10;

def menu():
    print("1) Fill");
    print("2) Print");
    print("3) Linear Search");
    print("4) Binary Search");
    print("5) Bubble sort (Inefficent)");
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

def binary_search(data,search_item):
    Low = 0;
    High = MAX - 1;
    while (Low <= High):
        Mid = (Low + High) // 2
        if (data[Mid] == search_item):
            return Mid;
        elif (search_item > data[Mid]):
            Low = Mid + 1;
        else:
            High = Mid - 1;
    return -1;

def bubble_sort(data):
    i = 9
    swapped = True;
    while not(swapped):
        j = 0;
        while (j < i):
            if 

def main():
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
        elif (choice == 4):
            item_to_search = int(input("Enter what you are looking for:"));
            print("");
            if (binary_search(arr, item_to_search) ==  True):
                print("Item found");
                print("");
            else:
                print("Item not found");
                print("");

main();