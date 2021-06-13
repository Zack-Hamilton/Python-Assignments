import random;
MAX = 10;

def menu():
    print("1) Fill");
    print("2) Print");
    print("3) Linear Search");
    print("4) Binary Search");
    print("5) Bubble sort (Inefficent)");
    print("6) Bubble sort (Efficent)");
    print("7) Insertion sort");
    print("8) Quit");

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
            return True;
        elif (search_item > data[Mid]):
            Low = Mid + 1;
        else:
            High = Mid - 1;
    return -1;

def bubble_sort_in(data):
    i = 9;
    for m in range (1, MAX):
        j = 0;
        while (j < i):
            if (data[j] > data[j + 1]):
                Temp = data[j];
                data[j] = data[j + 1];
                data [j + 1] = Temp;
            j = j + 1
        i = i - 1;
      
def bubble_sort_ef(data):
    i = 9;
    swapped = False;
    for m in range (1, MAX):
        swapped = True;
        j = 0;
        while (j < i):
            if (data[j] > data[j + 1]):
                Temp = data[j];
                data[j] = data[j + 1];
                data [j + 1] = Temp;
                swapped = False;
            j = j + 1
        i = i - 1;
        if swapped:
            return;

def insert_sort(data):
    i = 1;
    for i in range(1, MAX):
        Temp = data[i];
        Pos = i - 1;
        while (data[Pos] > Temp) and Pos > -1:
            data[Pos + 1] = data[Pos];
            Pos = Pos - 1;
        data[Pos + 1] = Temp;
        i = i + 1;

def main():
    arr = [0] * MAX;
    item_to_search = 0;
    choice = 0;

    while (choice != 8):
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
        elif (choice == 5):
            bubble_sort_in(arr);
        elif (choice == 6):
            bubble_sort_ef(arr);
        elif (choice == 7):
            insert_sort(arr);

main();
