import tkinter
from tkinter import messagebox

print('Dogs age faster than human bieng the little animals that they are.\nLet\'s look into how old your dog is. ')

def age_calc():
    try:
        w = eval(input("Enter your dog's weight\n"))
        if w in range(1,20):
            x = 1
        elif w in range(21, 50):
            x = 2
        elif w in range(51, 100):
            x = 3
        elif w >=100:
            x = 4
        print('How old is your dog?\n')
        y = int(input())
        if x == 1:
            small = [15,24,28,32,36,34,40,44,48,52,56,60,64,68,72,76,80]
            res = small[y-1]
        elif x == 2:
            medium = [15,24,28,32,36,42,47,51,56,60,65,69,74,78,83,87]
            res = medium[y-1]
        elif x == 3:
            large = [15,24,28,32,36,45,50,55,61,66,72,77,82,88,93,99]
            res = large[y-1]
        elif x == 4:
            giant = [12,22,31,38,45,49,56,64,71,79,86,93,100,107,114,121]
            res = giant[y-1]
    except ValueError or EOFError:
        print('Give a valid input')
        age_calc()
    messagebox.askquestion("Results", 'You dog is {} years old in human years.'.format(res))
age_calc()

root = tkinter.Tk()
root.withdraw()


