print('Hello, Django girls!')
if 3>2:
    name='Sonja'
if name=='Ala':
    print('Hej Ala!')
elif name=='Sonja':
    print('Hej Sonja!')
else:
    print('Hello Ty')


volume=81
if volume <20:
    print("It is quiet.")
elif 20 <= volume <40:
    print("Super , I can hear all")
elif 60<= volume <80:
    print ("nice for parties")
elif 80<= volume <100:
    print("too loud!")
else:
    print("my ears are hurting!:(")


#change the volume if it is too loud or too quiet
if volume < 20 or volume > 80:
    volume=57
    print("That's better!")

def hi():
    print('Hej!')
    print('How are you?')
hi()

def hi(imie):
    if imie=='Ala':
        print('Hej Ala!')
    elif imie=='Kasia':
        print('Hej Kasia')
    else:
        print('Hej you!')
hi("Ala")

def hi(imie):
    print('Witaj '+ imie + '!')

dziewczyny=['Ala', 'Monika', 'Edytka', 'Zofia']
for imie in dziewczyny:
    hi(imie)
    print('kolejna dziewczyna')
    
