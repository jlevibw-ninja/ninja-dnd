import weapons as wp

def spy_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        enemy_hp -= damage
        if weapon == "daggers":
            return f"Critical hit! You hit the enemy with your daggers for {damage} damage! "
        elif weapon == "ninja stars":
            return f"Critical hit! You hit the enemy with your ninja star for {damage} damage! "
    if attack_roll >= enemy_ac:       
        enemy_hp -= damage
        if weapon == "daggers":
            return f"You slashed the enemy with your daggers for {damage} damage! "
        elif weapon == "ninja stars":
            return f"You threw your ninja stars at the enemy for {damage} damage! "
    if attack_roll >= enemy_ac - 5:
        return f"You hit the enemy's armor and did no damage."     
    else:
        return f"You missed the enemy."
    return enemy_hp

def fighter_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        enemy_hp -= damage
        if weapon == "sword":
            return f"Critical hit! You hit the enemy with your sword for {damage} damage!"
        elif weapon == "axe":
            return f"Critical hit! You hit the enemy with your axe for {damage} damage!"
    if attack_roll >= enemy_ac:       
        enemy_hp -= damage
        if weapon == "sword":
            return f"You swung your sword at the enemy for {damage} damage! "
        elif weapon == "axe":
            return f"You swung your axe at the enemy for {damage} damage!"
    if attack_roll >= enemy_ac - 5:
        return f"You hit the enemy's armor and did no damage."     
    else:
        return f"You missed the enemy."
    return enemy_hp

def adventurer_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        enemy_hp -= damage
        if weapon == "whip":
            return f"Critical hit! You hit the enemy with your whip for {damage} damage!"
        elif weapon == "daggers":
            return f"Critical hit! You hit the enemy with your daggers for {damage} damage!"
        elif weapon == "machete":
            return f"Critical hit! You hit the enemy with your machete for {damage} damage!"
           
    if attack_roll >= enemy_ac:       
        enemy_hp -= damage
        if weapon == "whip":
            return f"You lashe the enemy with your whip for {damage} damage!"
        elif weapon == "daggers":
            return f"You slash the enemy with your daggers for {damage} damage!"
        elif weapon == "machete":
            return f"You swing your machete at the enemy for {damage} damage!"
    if attack_roll >= enemy_ac - 5:
        return f"You hit the enemy's armor and did no damage."     
    else:
        return f"You missed the enemy."
    return enemy_hp

def ranger_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        enemy_hp -= damage
        if weapon == "bow and arrow":
            return f"Critical hit! You hit the enemy with your bow and arrow for {damage} damage!"
        elif weapon == "daggers":
            return f"Critical hit! You hit the enemy with your daggers for {damage} damage!"
        elif weapon == "crossbow":
            return f"Critical hit! You hit the enemy with your crossbow for {damage} damage!"
           
    if attack_roll >= enemy_ac:       
        enemy_hp -= damage
        if weapon == "bow and arrow":
            return f"You hit the enemy with your bow and arrow for {damage} damage!"
        elif weapon == "daggers":
            return f"You slash the enemy with your daggers for {damage} damage!"
        elif weapon == "crossbow":
            return f"You fire your crossbow at the enemy for {damage} damage!"
    if attack_roll >= enemy_ac - 5:
        return f"You hit the enemy's armor and did no damage."     
    else:
        return f"You missed the enemy."
    return enemy_hp

def assassin_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        enemy_hp -= damage
        if weapon == "blowgun":
            return f"Critical hit! You hit the enemy with your blowgun for {damage} damage!"
        elif weapon == "daggers":
            return f"Critical hit! You hit the enemy with your daggers for {damage} damage!"
        elif weapon == "throwing knife":
            return f"Critical hit! You hit the enemy with your throwing knife for {damage} damage!"
           
    if attack_roll >= enemy_ac:       
        enemy_hp -= damage
        if weapon == "blowgun":
            return f"You hit the enemy with your blowgun for {damage} damage!"
        elif weapon == "daggers":
            return f"You slash the enemy with your daggers for {damage} damage!"
        elif weapon == "throwing knife":
            return f"You hit the enemy with your throwing knife for {damage} damage!"
    if attack_roll >= enemy_ac - 5:
        return f"You hit the enemy's armor and did no damage."     
    else:
        return f"You missed the enemy."
    return enemy_hp

def animal_trainer_attack(weapon, enemy_hp, enemy_ac):
    damage = wp.weapon_damage[weapon]
    attack_roll = random.randint(1, 20)
    if attack_roll == 20:
        damage *= 2
        enemy_hp -= damage
        if weapon == "whip":
            return f"Critical hit! You hit the enemy with your whip for {damage} damage!"
        elif weapon == "sling":
            return f"Critical hit! You hit the enemy with your sling for {damage} damage!"
                   
    if attack_roll >= enemy_ac:       
        enemy_hp -= damage
        if weapon == "whip":
            return f"You lashes the enemy with your whip for {damage} damage!"
        elif weapon == "sling":
            return f"You hit the enemy with your sling for {damage} damage!"

    if attack_roll >= enemy_ac - 5:
        return f"You hit the enemy's armor and did no damage."     
    else:
        return f"You missed the enemy."
    return enemy_hp

attack_functions = {"spy": spy_attack, "fighter": fighter_attack, "adventurer": adventurer_attack, "ranger": ranger_attack, "assassin": assassin_attack, "animal_trainer": animal_trainer_attack}