import streamlit as st
import time
import training as training

def find_quest(stats):
    
    talk_to_steve = ""
    find_steve = st.selectbox("Do you want to find Steve by going to the bar or searching in the crowd?", ["Stand there", "Go to bar", "Search crowd"])
    if find_steve == "Go to bar":
        st.write(f"You go to the bar. You find Steve there. You are glad that you did not search the crowd.") 
        st.write(f"''Why are you here?'' asks Steve.")
        talk_to_steve = st.selectbox("How do you respond?", ["", "Do not tell Steve who sent you.", "Tell steve a wizard sent you.", "Tell Steve that John the wizard sent you."])

    elif find_steve == "Search crowd":
        st.write(f"You did not find him, but someone did tell you that Steve will almost always be at the bar. you check the bar and he is there.")
        st.write(f"''Why are you here?'' asks Steve.")
        talk_to_steve = st.selectbox("How do you respond?", ["", "Do not tell Steve who sent you.", "Tell steve a wizard sent you.", "Tell Steve that John the wizard sent you."])

       
    else:
        st.write("...")


    talked = False

    if talk_to_steve == "Do not tell Steve who sent you.":
        st.write(f"You say, ''I am {stats[10]}. I just walked in here looking for an adnventure.''")
        st.write(f"Steve says, ''Interesting. I thought someone sent you here. You say you are looking for an adventure, {stats[10]}?''")
        st.write("''Yes,'' you say.")
        st.write("''Then come follow me,'' says Steve. He leads you behind the bar.")
        talked = True
    elif talk_to_steve == "Tell steve a wizard sent you.":
        st.write(f"You say, ''I am {stats[10]}. I found a wizard that told me you could give me an adventure.''")
        st.write(f"''I know alot of wizards. Can you tell me wich one it was {stats[10]}?'' asks Steve.")
        st.write(f"''I do not remember his name'' you lie.")
        st.write(f"You have a feeling that Steve knows you are lying. He motions for you to follow him.")
        talked = True
    elif talk_to_steve == "Tell Steve that John the wizard sent you.":
        st.write(f"''I am {stats[10]}. John the wizard sent me here,'' you say.")
        st.write(f"''John the wizard is a good friend of mine, come follow me {stats[10]},'' says Steve cheerfully")
        talked = True
    ready = False
    if talked:
        st.write("You follow Steve behind the bar. When you get there, you notice that there are lots of weapons, and what looks like a training area.")
        st.write("''Do you want to do a training session?'' asks Steve")
        train = st.selectbox("Do you want to do training?", ["Think about it", "Yes", "No"])
        if train == "No":
            st.write("''I do not want to train. I can do this,'' you say.")
            st.write("''Alright. That is the door. There is an evil scientest that we want. You can bring him back alive, or dead. Now go,'' sais Steve.")
        elif train == "Yes":
            st.write("''I will train,'' you say.")
            st.write("''Good,'' Steve says. Smiling mischievously, he flips a lever and iron bars suround you. The wall starts to open.")
            fight = st.selectbox("How do you respond?", ["Stand there", "Panic", "Question Steve's judgement", "Prepare to fight"])
            if fight == "Panic":
                st.write("You start panicing. ''GET ME OUT OF HERE!!!'' you yell.")
                st.write(f"''Good luck {stats[10]}!'' says Steve, as he walks away.")
                st.write("''You can't just leave me here!'' you say. The wall is now completely moved away, and there is an animal that looks like a cat. You let out a sigh of relif as it licks its paw. It looks at you, then attacks.")
                st.write(f"You manage to jump out of the way in time. The cat lands past you, and turns around as you draw your {stats[8]}.")
                ready = True
            elif fight == "Question Steve's judgement":
                st.write("''I seriously question your judgement,'' you say.")
                st.write(f"''What is there to question about my judgement {stats[10]}?'' asks Steve as he walks away. ''You have asked me to train you, and I am training you.''")
                st.write(f"You shake you head as you draw your {stats[8]}. The wall is now completely moved away, and there is a beast that looks like a cat.")
                
                ready = True
            elif fight == "Prepare to fight":
                st.write(f"You dramatically draw your {stats[8]} and say ''Bring it on''. Right then, the wall completely moves away, and there is a beast that looks like a cat in the doorway. Or, more acurately a wallway, you think as you smile. You do not notice Steve walking away.")
                ready = True
            else:
                st.write("...")
        else:
            st.write("...")
        if ready == True:
            st.write(f"Your you have {stats[7]} hp")
            training.training_func(stats=stats)
def start(stats):
    st.set_page_config(layout="wide")
    
    if "intro_started" not in st.session_state:
        st.session_state.intro_started = False

    if not st.session_state.intro_started:
        
        col1, col2 = st.columns(2)

        placeholder = col1.empty()
        val1 = 0

        with placeholder.container():
            st.set_page_config(layout="wide")
            st.title(f"You are a ninja looking for an adventure.")
            
            time.sleep(3)

            placeholder.empty()
            st.session_state.intro_started = True
            st.rerun()
    else:
        st.write(f"A wizard named John told you to go to the Tavern of Adventure. He said that the bartender named Steve would point you in the right direction for an adventure. You found the tavern no problem. Finding Steve will be the hard part.")
        st.write(f"When you walk into the tavern, you notice that it is crowded. Finding Steve will take a while. You can go to the bar and see if Steve is there, but you have a feeling that he is in the crowd.")
        
        
        find_quest(stats)        
game_start = {"start" : start, "quest": find_quest}