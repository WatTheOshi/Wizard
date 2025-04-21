# Training loop, lists, if statements

import random

# Enemies and their reward exp
Rat = {'name': 'Rat', 'exp': 20}
Worm = {'name': 'Worm', 'exp': 10}
Flea = {'name': 'Flea', 'exp': 5}
Toad = {'name': 'Toad', 'exp': 25}
Snail = {'name': 'Snail', 'exp': 15}
Teacup = {'name': 'Teacup', 'exp': 100}
Mind = {'name': 'Mind', 'exp': 200}
Butterfly = {'name': 'Butterfly', 'exp': 50}
Sapling = {'name': 'Sapling', 'exp': 30}
Puddle = {'name': 'Puddle', 'exp': 75}

monsters = [Rat,Worm,Flea,Toad,Snail,Teacup,Mind,Butterfly,Sapling,Puddle]

# adding a level bar to the game
level = 1
exp_count = 0
maximum_exp = 20

while level < 10:
    print("--==========================--")
    print(f"Your current level is {level}")

    # Battle encounter
    next_encounter = random.sample(monsters, 3)
    print("??? You have encountered:")
    for monster in next_encounter:
        print("=>", monster['name'])
    gain = input("/// Who is gonna be slain? [Enemy or Stop]: ")
    if gain == "Stop":
        print("You have spared them...")
        break
    for monster in next_encounter:
        if gain.lower() == monster['name'].lower():
            gain = monster['exp']
            print(f"$ You have earned {gain} exp!")
            exp_count += gain
            break
    else:
        print("!!! This enemy has not arrived yet !!!")
        continue

    # checking if the player has leveled up
    while exp_count >= maximum_exp:
        exp_count -= maximum_exp
        level += 1
        maximum_exp = 20 + abs((level - 1) + 1) * 8
        print("^ You have leveled up! ^")

    # Recalculate progress bar *after* level check
    bar_length = 20 
    progress = int((exp_count / maximum_exp) * bar_length)
    bar = '#' * progress + '-' * (bar_length - progress)
    print(f"& Progress: [{bar}] {exp_count}/{int(maximum_exp)} exp")
    
print("There is no enemy left to slay...") #FIXME: Normal ending

