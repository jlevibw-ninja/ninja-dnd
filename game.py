"""
Use streamlit to create text-based DnD game.
"""
import streamlit as st
import random 
import game_start as gs

st.set_page_config(layout="wide")

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if not st.session_state.game_started:
    col1, col2 = st.columns([10, 1])
    placeholder = col1.empty()
    with placeholder.container():
        
        spy = [0, 3, 4, 2, 1, -1]
        fighter = [4, -1, 0, 3, 2, 1]
        adventurer = [1, 2, 0, 3, -1, 4]
        ranger = [1, -1, 4, 3, 2, 0]
        assassin = [0, 4, 3, 2, -1, 1]
        animal_trainer = [0, -1, 2, 1, 3, 4]
        weapon_list = [""]
        armor_list = [""]

        st.title("Welcome to Ninja DnD. Continue if you dare.")
        name = st.text_input("Enter your name:")

        class_choice = st.selectbox(name + ", choose your class:", ["", "Spy", "Fighter", "Adventurer", "Ranger", "Assassin", "Animal Trainer"])
        modifiers = [0, 0, 0, 0, 0, 0]
        if class_choice == "Spy":
            modifiers = spy
            weapon_list.extend(["daggers", "ninja stars"])
            armor_list.extend(["leather armor"])
        elif class_choice == "Fighter":
            modifiers = fighter
            weapon_list.extend(["sword", "axe"])
            armor_list.extend(["studded leather armor", "chainmail", "iron armor"])
        elif class_choice == "Adventurer":
            modifiers = adventurer
            weapon_list.extend(["machete", "whip", "daggers"])
            armor_list.extend(["leather armor", "studded leather armor"])
        elif class_choice == "Ranger":
            modifiers = ranger
            weapon_list.extend(["bow and arrow", "crossbow", "daggers"])
            armor_list.extend(["leather armor"])
        elif class_choice == "Assassin":
            modifiers = assassin
            weapon_list.extend(["daggers", "throwing knife", "blowgun"])
            armor_list.extend(["leather armor"])
        elif class_choice == "Animal Trainer":
            modifiers = animal_trainer
            weapon_list.extend(["whip", "sling"])
            armor_list.extend(["leather armor"])
        weapon = st.selectbox(name + ", choose your weapon:", weapon_list)
        if weapon == "bow and arrow":
            st.write("You have chosen wisely. Your ranged attacks will be deadly.")
        elif weapon == "sword":
            st.write("A classic choice. Your swordsmanship will be unmatched.")
        elif weapon == "daggers":
            st.write("Swift and precise. Your daggers will strike fear into your enemies.")
        elif weapon == "axe":
            st.write("A formidable weapon. Your axe will crush your foes. Literally and figuratively.")
        elif weapon == "machete":
            st.write("A versatile weapon. Your machete will be useful in many situations.")
        elif weapon == "whip":
            st.write("A flexible weapon. Your whip will allow you to strike from a distance.")
        elif weapon == "sling":
            st.write("A simple but effective weapon. Your sling will be useful for hunting and combat.")
        elif weapon == "throwing knife":
            st.write("A deadly weapon. Your throwing knives will be lethal in the right hands.")
        elif weapon == "blowgun":
            st.write("A silent weapon. Your blowgun will allow you to strike from a distance without alerting your enemies.")
        elif weapon == "ninja stars":
            st.write("A classic ninja weapon. Your ninja stars will be deadly in the right hands.")
        elif weapon == "crossbow":
            st.write("A powerful ranged weapon. Your crossbow will allow you to strike from a distance with deadly accuracy.")

        armor = st.selectbox(name + ", choose your armor:", armor_list)
        player_ac = 10 + modifiers[2]
        if armor == "leather armor":
            player_ac = 11 + modifiers[2]
            st.write("Light and flexible. You can move quickly and silently.")
        elif armor == "studded leather armor":
            player_ac = 12 + modifiers[2]
            st.write("A good balance of protection and mobility. You can withstand some hits.")
        elif armor == "chainmail":
            player_ac = 13 + modifiers[2]
            st.write("Heavy and protective. You can take a lot of damage.")
        elif armor == "iron armor":
            player_ac = 15
            st.write("Heavy and protective. You can take a lot of damage, but you will be slower.")
        player_hp = 10 + modifiers[3]

        val1 = st.button("Start Your Adventure")


    if val1 and name != "" and class_choice != "" and weapon != "" and armor != "":
        placeholder.empty()  # This clears the first set of widgets
        st.session_state.game_started = True
        stats = [modifiers[0], modifiers[1], modifiers[2], modifiers[3], modifiers[4], modifiers[5], player_ac, player_hp, weapon, armor, name, class_choice]
        st.session_state.stats = stats
        st.rerun()
else:
    gs.start(st.session_state.stats)