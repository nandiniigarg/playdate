from PIL import Image
import pandas as pd
#

class doggie:

    def __init__(self, name, email, gender, age, breed, medical_history):
        self.name = name
        self.email = email
        self.gender = gender
        self.age = age
        self.breed = breed
        self.medical_history = medical_history

class article:
    
    def __init__(self, origin, popu, looks, temper, health, diet):
        self.origin = origin
        self.popu = popu
        self.looks = looks
        self.temper = temper
        self.health = health
        self.diet = diet
    


dog1 = doggie("Max", "abc1@email.com", "F", 3, "beagle", False)
dog2 = doggie("Royce","abc2@email.com", "M",2,"retriever", False)
dog3 = doggie("Nala","abc3@email.com", "F", 2,"labra", False)
dog4 = doggie("Fendi","abc4@email.com", "M", 2, "beagle", False)
dog5 = doggie("Odin", "abc5@email.com", "M", 1,"pitbull", False)
dog6 = doggie("hydra", "abc6@gmail.com", "F", 3, "labra", False)
dog7 = doggie("flusher", "abc7@gamil.com", "F", 1, "pug", False)
dog8 = doggie("Mathur", "abc8@gmail.com", "F", 3, "pom", False)
dog9 = doggie("ruby", "abc9@gmail.com", "M", 3, "pom", False)
dog10 = doggie("myster", "abc10@gmail.com", "F", 2, "retriever", False)

dog11 = doggie("Pokemone", "abc11@gmail.com", "M", 3, "pug", False)
dog12 = doggie("Leksi", "abc12@gmail.com", "M", 4, "beagle", False)
dog13 = doggie("Matti", "abc13@gamil.com", "F", 3, "Borzoi", False)
dog14 = doggie("lupi", "abc14@gmail.com", "M", 3, "labra", True)
dog15 = doggie("natti", "abc15@gmail.com", "F", 3, "Cavador", False)
dog16 = doggie("Billu", "abc16@gmail.com", "F",2,"Cavapoo", False)

doglist = [dog1, dog2, dog3, dog4, dog5, dog6, dog7, dog8, dog9, dog10, dog11, dog12, dog13, dog14, dog16]

def couple(a):
        match_email = []
        match_name = []
        for i in doglist:
            if a.age == i.age - 1 or a.age ==  i.age+1 or a.age == i.age:
                if a.gender != i.gender:
                    if a.medical_history == i.medical_history:
                        if a.breed == i.breed:
                            match_email.append(i.email)
                            match_name.append(i.name)
        return match_name, match_email

print(couple(dog4))

beagle = article("Great Britain", 
"The association of Masters of Beagles called as Beagle Club in the year 1896 held their first show at Peterborough in the United Kingdom.\nThe regular showing of the breed brought limelight to them and slowly their popularity started increasing.\nBut still they became more popular in the United States and Canada than in their native England.", 
"The general appearance of the beagle is like a miniature Foxhound,legs shorter as compared to full body proportion.\nThey are mostly between 13 to 16 inches high and weigh between 18 to 35 lb ,\nfemales being slightly smaller than the males.",
"They are very friendly and curious in nature.\nThey are neither aggressive nor timid,\nthey enjoy company of people a lot even with strangers if treated well they easily become friendly with them. ", 
"Beagles are prone to epilepsy, dwarfism is also seen in most of the breed.\nThey are considered chondrodystrophic breeds which are prone to types of disk diseases.\nHip dysplasia is also a common health issue found in some of the larger breeds.\nSome of the above mentioned issues can be cured with medications as well but their proper care is needed.",
"Beagles can eat eggs, fish, most of the meats, cheese, peanut butter, popcorn, tuna, yogurt wheat and most of the grains.\nAvoid feeding them avocado, mustard seeds, coffee, Raisins, tea, sugarless gum anything that contains xylitol should be avoided.")

def personal_blog(a):
        week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("What day is it today? \n")
        br = a.breed
        if day == week[0]:
            print("Your dog is from:",br.origin)
        elif day == week[1]:
            print("Your dog is popular for many reasons but here is one of them:\n",br.popu)
        elif day == week[2]:
            print("Here are some facts about your dog's appearance:\n",br.looks)
        elif day == week[3]:
            print("Some facts about your dog's temper:\n",br.temper)
        elif day == week[4]:
            print("How about some health facts about your loyal friend?\n",br.health)
        elif day == week[5]:
            print("Here are some dietary facts about your dog:\n",br.diet)
        elif day == week[6]:
            print("Here's a puppy picture to make your sunday! ;)") 
            im = Image.open("/Users/nandinigarg/Desktop/beagle.jpg")
            im.show()       
            
#personal_blog(dog1)

#personal profile

#x = input("Which one is your furry friend?")


#CoviCheck

url = 'https://www.mohfw.gov.in/'

web_content = requests.get(url).content

soup = BeautifulSoup(web_content, "html.parser")

extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

stats = [] 
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td')) 

    if len(stat) == 5:
        stats.append(stat)

new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
state_data = pd.DataFrame(data = stats, columns = new_cols)
state_data['Confirmed'] = state_data['Confirmed'].map(int)
state_data['Recovered'] = state_data['Recovered'].map(int)
state_data['Deceased']  = state_data['Deceased'].map(int)

#print(state_data)

