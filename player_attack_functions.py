import weapons as wp

def spy_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        
        if weapon == "daggers":
            st.write(f"Critical hit! You hit the enemy with your daggers for {damage} damage! ")
        elif weapon == "ninja stars":
            st.write(f"Critical hit! You hit the enemy with your ninja star for {damage} damage! ")
    if attack_roll >= enemy_ac:       
        
        if weapon == "daggers":
            st.write(f"You slashed the enemy with your daggers for {damage} damage! ")
        elif weapon == "ninja stars":
            st.write(f"You threw your ninja stars at the enemy for {damage} damage! ")
    if attack_roll >= enemy_ac - 5:
        st.write(f"You hit the enemy's armor and did no damage."  )   
    else:
        st.write(f"You missed the enemy.")

    enemy_hp -= damage
    return enemy_hp

def fighter_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        
        if weapon == "sword":
            st.write(f"Critical hit! You hit the enemy with your sword for {damage} damage!")
        elif weapon == "axe":
            st.write(f"Critical hit! You hit the enemy with your axe for {damage} damage!")
    if attack_roll >= enemy_ac:       
        
        if weapon == "sword":
            st.write(f"You swung your sword at the enemy for {damage} damage! ")
        elif weapon == "axe":
            st.write(f"You swung your axe at the enemy for {damage} damage!")
        
        else:
            st.write(f"You missed the enemy.")

    enemy_hp -= damage
    return enemy_hp

def adventurer_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        
        if weapon == "whip":
            st.write(f"Critical hit! You hit the enemy with your whip for {damage} damage!")
        elif weapon == "daggers":
            st.write(f"Critical hit! You hit the enemy with your daggers for {damage} damage!")
        elif weapon == "machete":
            st.write(f"Critical hit! You hit the enemy with your machete for {damage} damage!")
           
    if attack_roll >= enemy_ac:       
        
        if weapon == "whip":
            st.write(f"You lashe the enemy with your whip for {damage} damage!")
        elif weapon == "daggers":
            st.write(f"You slash the enemy with your daggers for {damage} damage!")
        elif weapon == "machete":
            st.write(f"You swing your machete at the enemy for {damage} damage!")
    if attack_roll >= enemy_ac - 5:
        st.write(f"You hit the enemy's armor and did no damage." )    
    else:
        st.write(f"You missed the enemy.")

    enemy_hp -= damage
    return enemy_hp

def ranger_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        
        if weapon == "bow and arrow":
            st.write(f"Critical hit! You hit the enemy with your bow and arrow for {damage} damage!")
        elif weapon == "daggers":
            st.write(f"Critical hit! You hit the enemy with your daggers for {damage} damage!")
        elif weapon == "crossbow":
            st.write(f"Critical hit! You hit the enemy with your crossbow for {damage} damage!")
           
    if attack_roll >= enemy_ac:       
        
        if weapon == "bow and arrow":
            st.write(f"You hit the enemy with your bow and arrow for {damage} damage!")
        elif weapon == "daggers":
            st.write(f"You slash the enemy with your daggers for {damage} damage!")
        elif weapon == "crossbow":
            st.write(f"You fire your crossbow at the enemy for {damage} damage!")
    if attack_roll >= enemy_ac - 5:
        st.write(f"You hit the enemy's armor and did no damage.")    
    else:
        st.write(f"You missed the enemy.")

    enemy_hp -= damage
    return enemy_hp

def assassin_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        
        if weapon == "blowgun":
            st.write(f"Critical hit! You hit the enemy with your blowgun for {damage} damage!")
        elif weapon == "daggers":
            st.write(f"Critical hit! You hit the enemy with your daggers for {damage} damage!")
        elif weapon == "throwing knife":
            st.write(f"Critical hit! You hit the enemy with your throwing knife for {damage} damage!")
           
    if attack_roll >= enemy_ac:       
        
        if weapon == "blowgun":
            st.write(f"You hit the enemy with your blowgun for {damage} damage!")
        elif weapon == "daggers":
            st.write(f"You slash the enemy with your daggers for {damage} damage!")
        elif weapon == "throwing knife":
            st.write(f"You hit the enemy with your throwing knife for {damage} damage!")
    if attack_roll >= enemy_ac - 5:
        st.write(f"You hit the enemy's armor and did no damage.")     
    else:
        st.write(f"You missed the enemy.")

    enemy_hp -= damage
    return enemy_hp

def animal_trainer_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        
        if weapon == "whip":
            st.write(f"Critical hit! You hit the enemy with your whip for {damage} damage!")
        elif weapon == "sling":
            st.write(f"Critical hit! You hit the enemy with your sling for {damage} damage!")
                   
    if attack_roll >= enemy_ac:       
        
        if weapon == "whip":
            st.write(f"You lashes the enemy with your whip for {damage} damage!")
        elif weapon == "sling":
            st.write(f"You hit the enemy with your sling for {damage} damage!")

    if attack_roll >= enemy_ac - 5:
        st.write(f"You hit the enemy's armor and did no damage.")    
    else:
        st.write(f"You missed the enemy.")

    enemy_hp -= damage
    return enemy_hp

attack_functions = {"spy": spy_attack, "fighter": fighter_attack, "adventurer": adventurer_attack, "ranger": ranger_attack, "assassin": assassin_attack, "animal_trainer": animal_trainer_attack}