import streamlit as st
import random
from weapons import weapon_damage as wd
from player_attack_functions import attack_functions as af
import time

def cat_attack(player_hp, player_ac, player_state):
    damage = random.randint(1, 4)
    attack = random.randint(1, 20)
    if player_state == "Hiding":
        st.write("The cat did not find you.")
    elif player_state == "Run":
        st.write("The cat could not catch up to you.")
    elif attack == 20:
        damage *= 2
        player_hp -= damage
        st.write(f"The cat slashed you across the chest. You take {damage} damgage. You are now at {player_hp} hp.")
    elif attack >= player_ac:
        player_hp -= damage
        st.write(f"The cat slashed you doing {damage} damage. You are ow at {player_hp} hp.")
    else:
        st.write("The cat missed you.")
    
    return player_hp


def player_attack(stats, enemy_hp, enemy_ac, num):
    
    player_state = st.selectbox("Do you want to attack, run or hide?", ["Stand there", "Attack", "Run"], key = num)
    if player_state == "Attack":
        if stats[11] == "spy":
            enemy_hp = af.spy(stats[8], enemy_hp, enemy_ac)
        elif stats[11] == "assasin":
            enemy_hp = sf.assasin(stats[8], enemy_hp, enemy_ac)
        elif stats[11] == "adventurer":
            enemy_hp = af.adventurer(stats[8], enemy_hp, enemy_ac)
        elif stats[11] == "fighter":
            enemy_hp = af.fighter(stats[8], enemy_hp, enemy_ac)
        elif stats[11] == "ranger":
 elif player_state == "Run":        st.write("You run away from the cat.")        time_to_attack == 100    elif player_state == "Hide":        hide = random.randint(1, 20)        if hide >= 12:            st.write("You have succesfully hidden.")        else:            st.write("You could not find a place to hide.")            player_state = "Attack"        time_to_attack = 100                enemy_hp = af.ranger(stats[8], enemy_hp, enemy_ac)
        elif stats[11] == "animal trainer":
            enemy_hp = af.animal_trainer(stats[8], enemy_hp, enemy_ac)
        
    
    
    else:
        st.write("...")
    num += 1
    return enemy_hp
def training_func(stats):
    player_hp = stats[7]
    player_ac = stats[6]
    enemy_hp = 15
    enemy_ac = 12

    current_enemy_hp = enemy_hp
    current_player_hp = player_hp

    
    player_state = "Attack"
    num = 0
    while player_hp > 0:
        current_enemy_hp = player_attack(stats, current_enemy_hp, enemy_ac, num)
        time.sleep(3)  
        if current_enemy_hp <= 0:
            break
        current_player_hp = cat_attack(current_player_hp, player_ac, player_state)
        time.sleep(1)
        st.write(f"Your hp is {current_player_hp}")

            
        num += 1
training_dict = {"train": training_func}