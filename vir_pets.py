# This is a virtual pet game that I created to increase the user engagement of the project.
# This game is both entertaining and educative of how to take care of a new born puppy by displaying warnings and restrictions.
# If you are a beginner in Python, then this will be an easy code for you to understand 
# as it is mostly conditional statements and loops.


import time
import datetime
import random
from PIL import Image, ImageFont, ImageDraw


class Pet:
    def __init__(self, name, hungry, weight, age, sex, happy_score, sick, life):
        self.name = name
        self.hungry = hungry
        self.weight = weight
        self.age = age
        self.sex = sex
        self.happy_score = happy_score
        self.sick = sick
        self.life = life

Pet.age = 1


def show_status():

    print('Name of The Sweetheart :', Pet.name)
    print('Age :', Pet.age)
    print('Gender :', Pet.sex)
    print('Weight :', Pet.weight)
    print('Hungry :', Pet.hungry)
    print('Happy Score :', Pet.happy_score)
    print('Is your pet sick?', Pet.sick)
    print('Alive :', Pet.life)
    menu_in()

def initiate():

    print('Welcome to FloofPlus!\nThis is a virtual pet that you take care of.\nAs your pet grows, so do you!\nYou will learn more about how to take care of a labrador puppy!\nLETS GET STARTED!!!')
    Pet.life = True
    Pet.name = input('What would you like to name your puppy?\n')
    Pet.weight = 1
    Pet.happy_score = 0
    Pet.sick = False
    Pet.sex = input('Is your {} a boy or a girl?\n(Select one: M or F)\n'.format(Pet.name))
    
    print('Great! Now lets get started.')
    str1 = 'Congratualations!\n{} is now all yours :D'.format(Pet.name)
    if Pet.sex == 'M':
        image = Image.open('doug2.jpg')
        width, height = image.size 
        font1 = ImageFont.truetype('Arial Bold.ttf', 100) 
        draw = ImageDraw.Draw(image)
        draw.text(xy=(100,100), text = str1, fill = (75,66,245), font = font1)
        image.show()
    else:
        image = Image.open('doug3.jpg')
        width, height = image.size 
        font1 = ImageFont.truetype('Arial Bold.ttf', 20) 
        draw = ImageDraw.Draw(image)
        draw.text(xy=(70,290), text = str1, fill = (75,66,245), font = font1)
        image.show()
    menu_in()
    set_hungry()


def bathe():
    
    if Pet.happy_score <=10:
        Pet.happy_score += 1
    else:
        print('Your pet is already satisfied with how they feel.')
    menu_in()

def reverse_w():
    
    list1 = ['doggo', 'catto', 'mailman', 'treat', 'ball', 'play', 'daycare']
    m = random.choice(list1)
    l1 = m.split()
    print('Reverse the folloing string:') 
    x = input(m+'\n')
    j=''
    for i in m[::-1]:
        j += str(i)
    if x == j:
        print('Wow you must be smart because you did it perfectly :)\n')
        time.sleep(5)
        Pet.happy_score += 2
        menu_in()
    else:
        print('Aww it\'s okay, better luck next time.\n' )
        menu_in()

def feed():
    
    if Pet.age in range(1, 9):

        if Pet.weight in range(1,3):
            Pet.hungry = False
            Pet.weight += 1
            print('Your pet loved his healthy homemade meal. :)\n')
        elif Pet.age >= 3:
            print('You have to stop feeding it or it will die.\nNOTE: Your pet should not be more than 2 lbs at this age. Increase age to continue.\n')
        
    elif Pet.age in range(9, 17):
        if Pet.weight in range(10,16):
            Pet.hungry = False
            Pet.weight += 1
            print('Your pet loved his healthy homemade meal. :)')
        elif Pet.weight >= 16:
            print('You have to stop feeding it or it will die.\nNOTE: Your pet should not be more than 15 lbs at this age. Increase age to continue.\n')
        else:
            print('Your pet seems weak. Be more careful with the meals.\nNOTE: Your pet should not be less than 10 lbs at this age.\n')
    elif Pet.age in range(17,31):
        if Pet.weight in range(16, 50):
            Pet.hungry = False
            Pet.weight += 1
            print('Your pet loved his healthy homemade meal. :)\n')
        elif Pet.weight >= 50:
            print('You have to stop feeding it or it will die.\nNOTE: Your pet should not be more than 50 lbs at this age. Increase age to continue.\n')
        elif Pet.weight <= 16:
            print('Your pet seems weak. Be more careful with the meals.\nNOTE: Your pet should not be less than 16 lbs at this age.\n')
        
    elif Pet.age in range(31, 41):
        if Pet.weight in range(51, 61):
            Pet.hungry = False
            Pet.weight += 1
            print('Your pet loved his healthy homemade meal. :)\n')
        elif Pet.weight >= 60:
            print('You have to stop feeding it or it will die.\nNOTE: Your pet should not be more than 60 lbs at this age. Increase age to continue.\n')
        elif Pet.weight <= 51:
            print('Your pet seems weak. Be more careful with the meals.\nNOTE: Your pet should not be less than 51 lbs at this age.\n')
    
    elif Pet.age in range(41, 53):
        if Pet.sex == 'F':
            if Pet.weight in range(61, 70):
                Pet.hungry = False
                Pet.weight += 1
                print('Your pet loved his healthy homemade meal. :)')
            elif Pet.weight >= 70:
                print('You have to stop feeding it or it will die.\nNOTE: Your pet should not be more than 70 lbs at this age. Increase age to continue.\n')
            elif Pet.weight <= 61:
                print('Your pet seems weak. Be more careful with the meals.\nNOTE: Your pet should not be less than 61 lbs at this age.\n')
        else:
            if Pet.weight in range(61, 80):
                Pet.hungry = False
                Pet.weight += 1
                print('Your pet loved his healthy homemade meal. :)')
            elif Pet.weight >= 70:
                print('You have to stop feeding it or it will die.\nNOTE: Your pet should not be more than 80 lbs at this age. Increase age to continue.\n')
            elif Pet.weight <= 61:
                print('Your pet seems weak. Be more careful with the meals.\nNOTE: Your pet should not be less than 61 lbs at this age.\n')

    Pet.happy_score += 1
    menu_in()


def menu_in():

    print('Here\'s a list of activitoes that you can do with you pet:\n\n',
    '1. Feed : Your pet from time to time so that it doesn\'t die.\nNOTE : Be careful of how much you feed your pet might get sick :(\n',
    '2. Play : Have fun with your pet as they grow :)\n',
    '3. Age : Increase the age of your pet to unlock new games. (Age is in weeks because just like your puppy this program is still growing)\n',
    '4. Bathe : Bathe your dog from time to time to increase their happy score.\n',
    '5. Show Status : Check the status of your dog from time to time.\n',
    'Take good care of your friend as they depend on you with all their heart.\n(Both real and virtual ;) )\n'
    )
    try:
        x = int(input())
        if x == 1:
            feed()
        elif x == 2:
            play()
        elif x == 3:
            Pet.age += 1
            print(Pet.age)
        elif x == 4:
            bathe()
        elif x == 5:
            show_status()
        else:
            print('Enter a valid number mate.')
            menu_in()
    except ValueError or EOFError:
        print('Enter a valid number mate.')
        menu_in()


def menu_ret():

            a = input('Would you like to go back to the menu?\n(Y for yes and N for no)')
            if a == 'Y':
                menu_in()
            elif a == 'N':
                exit()
            else:
                print('Give a valid entry.')
                menu_ret()


def fed():
        Pet.hungry = True
        print('Your pet is hungry now feed it')


def age():

    if Pet.age in range(1,52):
        Pet.age =+ 1
        print('Your pet is now', Pet.age,'weeks old.')
        menu_in()
        
    else:
        print('Your pet has now left for service dog training.\nCongratulations you have successfully completed this game.')
        menu_in()
    
def set_hungry():
    
    t = int(input('Enter the number of minutes in which the pet will be HANGRY again in: '))
    while t:
        if datetime.datetime.now().hour >=21:
            print('Your pet is asleep right now, come back after 9am tomorrow.')
            menu_in()
            time.sleep(3600*12)
            
            
        else:
            mins, secs = divmod(t, 60)
            time.sleep(t)
            Pet.hungry = True
            print('Your Pet is now hungry. Better feed it quick!!')
            ans = input('Do you want to feed now?\n(Y for yes and N for no)')
            if ans == 'Y':
                feed()
                print('Your pet loved the meal')
            else:
                print('Let\'s try another time.')
                time.sleep(5)
                menu_in()
            break

def mailman():

    pos = ['Flourist', 'Milkman', 'Treat', 'Toy', 'Furr', 'Ball', 'Squirrel', 'Car']
    x = random.choice(pos)
    pos.remove(x)
    y = random.choice(pos)
    res = ['Mailman']
    res.append(y)
    res.append(x)
    fin = random.sample(res, len(res))
    print('Which position was the mailman on?? (1, 2 or 3)')
    for i in fin:
        print('\r')
        print(i)
    
    time.sleep(5)
    print('', end = '\r')
    x = int(input())
    
    if fin[x-1] == res[0]:
    
        print('{} caught the Mailman!'.format(Pet.name))
        time.sleep(5)
        menu_in()
    
    else:
    
        print('Try Again next time :/ ')
        time.sleep(5)
        menu_in()

def unscramble():

    res = ['flourist', 'milkman', 'treat', 'toy', 'furr', 'sall', 
            'squirrel','doggo', 'catto', 'mailman', 'treat', 'ball', 'play', 'daycare']
    x = random.choice(res)
    j = ''

    while x:

        position = random.randrange(len(x))
        j += x[position]
        x = x[:position] + x[(position + 1):]
    print('Unscramble the following world:\n')
    a = input(j+'\n')

    if x == x:
        
        print('You are awesome! You absolutely killed this game :D\n')
        time.sleep(5)

    else:
        print('Better luck next time :/ ')
        time.sleep(5)
    
    menu_in()

def play():
    try:
        if Pet.hungry == False:
            Pet.happy_score += 1
            print('Select a game:')
            p = int(input('Enter the correct number for playing with your pet.\n1. Catch The Mailman.\n2. Reverse The Word\n3. Unscramble The Word\n'))
            if p == 1:
                mailman()
            elif p == 2:
                reverse_w()
            elif p == 3:
                unscramble()
            else:
                print('Enter a valid entry.')
                play()
        else:
            print('Feed your dog first!')
    except:
        print('Feed your dog first!')
        menu_in()


initiate()
