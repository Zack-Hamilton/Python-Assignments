import random;
num = [0] * 10;

def fill():
    row = 0;
    while (row < 10):
        num[row] = random.randint(10,99);
        row = row + 1;

def printing():
    row = 0;
    while (row < 10):
        print(num[row]);
        row = row + 1;    

choice = 0;

while (choice != 7):
    choice = int(input("Enter your choice:"));
    print("");

    if (choice == 1):
        fill();
    elif (choice == 2):
        printing();