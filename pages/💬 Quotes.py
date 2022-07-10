import streamlit as st
import pandas as pd
st.set_page_config(
     page_title="Incorrect Quotes",
     page_icon=":speech_balloon:",
     layout="wide",
     initial_sidebar_state="expanded",
 )
st.title("K&M Incorrect Quotes")
st.markdown("""
Here you'll be able to create incorrect quotes
****
""")
numberpeople = int(st.selectbox("Choose how many people you want to involve",('1','2','3','4','5','6')))
pronounslist = ["they/them", "she/her", "he/him"]
c1, c2 = st.columns(2)
if numberpeople >= 1:
    name1 = c1.text_input("What's the first name?")
    pronouns_1 = c2.selectbox("What are the first pronouns?", pronounslist)
    import random
    if pronouns_1 == "he/him":
        sub_1 = "he"
        obj_1 = "him"
        poss_1 = "his"
        poss_pr_1 = "his"
        refl_1 = "himself"
        part_1 = "boyfriend"
    if pronouns_1 == "she/her":
        sub_1 = "she"
        obj_1 = "her"
        poss_1 = "her"
        poss_pr_1 = "hers"
        refl_1 = "herself"
        part_1 = "girlfriend"
    if pronouns_1 == "they/them":
        sub_1 = "they"
        obj_1 = "them"
        poss_1 = "their"
        poss_pr_1 = "theirs"
        refl_1 = "themselves"
        part_1 = "partner"
if numberpeople >= 2:
    name2 = c1.text_input("What's the second name?")
    pronouns_2 = c2.selectbox("What are the second pronouns?", pronounslist)
    import random
    if pronouns_2 == "he/him":
        sub_2 = "he"
        obj_2 = "him"
        poss_2 = "his"
        poss_pr_2 = "his"
        refl_2 = "himself"
        part_2 = "boyfriend"
    if pronouns_2 == "she/her":
        sub_2 = "she"
        obj_2 = "her"
        poss_2 = "her"
        poss_pr_2 = "hers"
        refl_2 = "herself"
        part_2 = "girlfriend"
    if pronouns_2 == "they/them":
        sub_2 = "they"
        obj_2 = "them"
        poss_2 = "their"
        poss_pr_2 = "theirs"
        refl_2 = "themselves"
        part_2 = "partner"
if numberpeople >= 3:
    name3 = c1.text_input("What's the third name?")
    pronouns_3 = c2.selectbox("What are the third pronouns?", pronounslist)
    import random
    if pronouns_3 == "he/him":
        sub_3 = "he"
        obj_3 = "him"
        poss_3 = "his"
        poss_pr_3 = "his"
        refl_3 = "himself"
        part_3 = "boyfriend"
    if pronouns_3 == "she/her":
        sub_3 = "she"
        obj_3 = "her"
        poss_3 = "her"
        poss_pr_3 = "hers"
        refl_3 = "herself"
        part_3 = "girlfriend"
    if pronouns_3 == "they/them":
        sub_3 = "they"
        obj_3 = "them"
        poss_3 = "their"
        poss_pr_3 = "theirs"
        refl_3 = "themselves"
        part_3 = "partner"
if numberpeople >= 4:
    name4 = c1.text_input("What's the fourth name?")
    pronouns_4 = c2.selectbox("What are the fourth pronouns?", pronounslist)
    import random
    if pronouns_4 == "he/him":
        sub_4 = "he"
        obj_4 = "him"
        poss_4 = "his"
        poss_pr_4 = "his"
        refl_4 = "himself"
        part_4 = "boyfriend"
    if pronouns_4 == "she/her":
        sub_4 = "she"
        obj_4 = "her"
        poss_4 = "her"
        poss_pr_4 = "hers"
        refl_4 = "herself"
        part_4 = "girlfriend"
    if pronouns_4 == "they/them":
        sub_4 = "they"
        obj_4 = "them"
        poss_4 = "their"
        poss_pr_4 = "theirs"
        refl_4 = "themselves"
        part_4 = "partner"
if numberpeople >= 5:
    name5 = c1.text_input("What's the fifth name?")
    pronouns_5 = c2.selectbox("What are the fifth pronouns?", pronounslist)
    import random
    if pronouns_5 == "he/him":
        sub_5 = "he"
        obj_5 = "him"
        poss_5 = "his"
        poss_pr_5 = "his"
        refl_5 = "himself"
        part_5 = "boyfriend"
    if pronouns_5 == "she/her":
        sub_5 = "she"
        obj_5 = "her"
        poss_5 = "her"
        poss_pr_5 = "hers"
        refl_5 = "herself"
        part_5 = "girlfriend"
    if pronouns_5 == "they/them":
        sub_5 = "they"
        obj_5 = "them"
        poss_5 = "their"
        poss_pr_5 = "theirs"
        refl_5 = "themselves"
        part_5 = "partner"
if numberpeople == 6:
    name6 = c1.text_input("What's the sixth name?")
    pronouns_6 = c2.selectbox("What are the sixth pronouns?", pronounslist)
    import random
    if pronouns_6 == "he/him":
        sub_6 = "he"
        obj_6 = "him"
        poss_6 = "his"
        poss_pr_6 = "his"
        refl_6 = "himself"
        part_6 = "boyfriend"
    if pronouns_6 == "she/her":
        sub_y = "she"
        obj_6 = "her"
        poss_6 = "her"
        poss_pr_6 = "hers"
        refl_6 = "herself"
        part_6 = "girlfriend"
    if pronouns_6 == "they/them":
        sub_6 = "they"
        obj_6 = "them"
        poss_6 = "their"
        poss_pr_6 = "theirs"
        refl_6 = "themselves"
        part_6 = "partner"

with st.form("my form"):
    def frase():
        if numberpeople == 1:
            phraseposition = random.randint(1, 2)
            if phraseposition == 1:
                st.markdown(
                    f"""{name1}: "I’m going to defeat you with the power of friendship! ... And this knife I found." """)
            if phraseposition == 2:
                st.markdown(
                    f"""{name1} : "You’ll have a hard time believing this because it never happens, but I made a mistake." """)

        if numberpeople == 2:
            phraseposition = random.randint(21, 36)
            if phraseposition == 21:
                st.markdown(f"""{name1}: "You know, not every problem can be solved with a sword" \n {name2}: "That's why I carry two swords" """)
            if phraseposition == 22:
                st.markdown(f"""{name1}: "{name2}..."  \n {name2}  ": Oh no, {name2} in B flat, you're disappointed""")
            if phraseposition == 23:
                st.markdown(f"""{name1}: "Who tf is burning down my kitchen" \n {name2}: "making breakfast for my beautiful {part_1}" """)
            if phraseposition == 24:
                st.markdown(f"""{name1}: "I might be stupid...."  \n {name2}  : "... and?"  \n {name1}: "That's it" """)
            if phraseposition == 25:
                st.markdown(f"""{name1} *Accidentally hits {name2} in the face* \n {name1} :*Trying to decide between saying "I'm sorry" or "are you ok"*  \n {name1}: "ARE YOU SORRY?!"  \n {name2}: "What's wrong with you?!" """)
            if phraseposition == 26:
                st.markdown(f"""{name1}: I hope I don't have to fight my evil shadow self today"  \n {name2}: "hey"  \n {name1}: "no fucking way" """)
            if phraseposition == 27:
                st.markdown(f"""{name1}: "What is it called when hands are bisexuals?" \n {name2}: "Ambidextrous?" \n {name1}: "I'm in love with you" """)
            if phraseposition == 28:
                st.markdown(f"""{name1} *Watching the news* : "Some idiot tried to fight a squid at the aquarium" \n {name2}  "*Covered in ink* : "maybe the squid was being a dick" """)
            if phraseposition == 29:
                st.markdown(f"""{name1}: You wanna go upstairs?"  \n {name2}: "Sure..."  \n {name1}: "You got protection?" \n {name2}: "Why, what's up there?" """)
            if phraseposition == 30:
                st.markdown(f"""{name1}: "I need boy advice help!"  \n {name2}: "Kill him" """)
            if phraseposition == 31:
                st.markdown(f"""{name1}: "heads up: if you try to make a candle with food coloring, the food coloring will just sink to the bottom of the glass, and when the flame eventually reaches the bottom, all the food coloring will catch fire and become one giant tall flame that you cannot possibly blow out and the glass will start to crack and then you'll throw your tea on it in a panic and them the extremely hot food coloring will boil and sizzle horribly and then the glass will shatter." \n {name1}: "trust me on this." \n {name2}: "{name1}, what did you do?" \n {name1}: "a Mistake." """)
            if phraseposition == 32:
                st.markdown(f"""{name1}: "The next person to say ‘weird flex but okay’ is getting a kick to the shin." \n {name2}: "Preposterous boast but alas." """)
            if phraseposition == 33:
                st.markdown(f"""{name1} *tries to focus her magic* \n 
                {name2} *runs in and hugs {obj_1} from behind* \n 
                {name1}: "mmm what was that for?" \n 
                {name2}: "you looked like you needed a hug" \n 
                {name1}: "well I didn’t say stop" \n 
                {name2} *hugs {obj_1} tighter.* \n
               {name1} *giggles.* """)
            if phraseposition == 34:
                st.markdown(f"""{name1}: "How many kids do you have?" \n
                {name2}: "Biologically, emotionally, or legally?" """)
            if phraseposition == 35:
                st.markdown(f"""kidnappers: we have the enemy \n
                {name1}: but i dont have any enemies \n
                kidnappers: but the contact name says "fucking bitch"\n
                {name1}: oh my god they have {name2}""")
            if phraseposition == 36:
                st.markdown(f"""{name1}: "I love cheating. If you don’t cheat, what the hell is wrong with you?"\n
                {name2}: "Have you ever been cheated on?"\n
                {name1}: "I forgot some people are in relationships. To clarify, I love to violate academic integrity on tests." """)

            


        if numberpeople == 3:
            phraseposition = random.randint(41, 44)
            if phraseposition == 41:
                st.markdown(f"""{name1}: "Hey, {name2}? Can I get some dating advice?" \n
                {name2}: "Just because I’m with {name3} doesn’t mean I know how I did it." """)
            if phraseposition == 42:
                st.markdown(f"""{name1}: "Are you sure this is the right direction?" \n
                {name2}: "Certainly, I'm as sure as I am honest!" \n
                {name3}: "In that case, we're definitely lost." """)
            if phraseposition == 43:
                st.markdown(f"""{name1}: "Why does {name2} call you babygirl?" \n
                {name3}: "How about we stop talking for a little while?" """)
            if phraseposition == 44:
                st.markdown(f"""{name1}, driving {name2} and {name3} \n
                {name1}: "So how was your day?" \n
                {name2}: "We almost got surprise adopted!" \n
                {name1}: "What?" \n
                {name3}: "We almost got kidnapped." \n
                {name1}: "Oh, okay." \n
                {name1} *slams on the breaks* : "WAIT WHAT?!" """)

                    
        if numberpeople == 4:
            phraseposition = random.randint(61, 67)
            if phraseposition == 61:
                st.markdown(f"""{name1}: "Can I be frank with you guys?" \n
                {name2}: "Sure, but I don’t see how changing your name is gonna help." \n 
                {name3}: "Can I still be {name3}?"  \n
                {name4}: "Shh, let Frank speak." """)
            if phraseposition == 62:
                st.markdown(f"""{name1}: "On the count of three, what's your favorite cake? One, two, three" \n
                {name1} and {name2}, in unison: "Chocolate cake peanut butter frosting with chocolate chunks!" \n 
                {name3}: Our turn, {name4}! One, two, three- vanilla!"  \n
                {name4}, deadpan: I've never had cake, what is cake." """)
            if phraseposition == 63:
                st.markdown(f""" {name1}: "Why are {name2} and {name3} sitting with their backs to each other?" \n
                {name4}: "They had a fight." \n
                {name1}: "Then why are they holding hands?" \n
                {name4}: "They get sad when they fight." """)
            if phraseposition == 64:
                st.markdown(f"""{name1}: "I think we're missing something." \n
                {name2}: "Teamwork?" \n
                {name3}: "Cohesion?" \n
                {name4}: "A general sense of what we’re doing?" """)
            if phraseposition == 65:
                st.markdown(f"""{name1}, about {name2}: "I get this weird feeling in my chest whenever i see {obj_2}." \n
                {name3}: \n
                {name4}: \n
                {name4}: "is it heartburn?" """)
            if phraseposition == 66:
                st.markdown(f"""{name1}: "Yeah, we just met, but I would fuck you if you asked." \n
                {name2}: "What?" \n
                {name1}: "What?" \n
                {name3} and {name4}, in the background, eating chips: \n
                {name4}: "You said you would fuck {obj_2} if {sub_1} asked." """)
            if phraseposition == 67:
                st.markdown(f"""{name1}: "I understand why none of us have partners." \n
                {name1}: "{name2} is dating {poss_2} cat." \n
                {name1}: {name3} is a freak. \n
                {name1}: And {name4} is addicted to games. \n
                {name1}: No wonder we don't have anyone.""")


        if numberpeople == 5:
            phraseposition = random.randint(81, 83)
            if phraseposition == 81:
                st.markdown(f"""{name1}  ": I'm an idiot."  \n
                {name2}:  \n
                {name3}: \n
                {name4}:  \n
                {name5}: \n
                {name1}:  \n
                {name2}: "If you're waiting for us to disagree, this is going to be a long day" """)
            if phraseposition == 82:
                st.markdown(f"""{name1}: Bye {name2}! Bye {name3}! Bye {name4}! Bye {name5}! Bye {name2}!"  \n
                {name3}: "You said "bye {name2}" twice."  \n
                {name1}: "I like {name2}."  """)
            if phraseposition == 83:
                st.markdown(f"""{name1}: "I've done a lot of dumb shit" \n
                {name2}: "I joined you in the dumb shit" \n
                {name3}: "I helped you in the dumb shit"
                {name4}: "I recorded the dumb shit" \n
                {name5}: I TRIED to stop YOU ALL from doing the dumb shit SEVERAL TIMES""")                    

        if numberpeople == 6:
            phraseposition = random.randint(101, 103)
            if phraseposition == 101:
                st.markdown(f"""{name1}, walking into their house: "Hello, people who do not live here." \n
                {name2}: "Hey." \n
                {name3}: "Hi."  \n
                {name4}: "Hello."  \n
                {name5}: Hey!"  \n
                {name1}: "I gave you the key to my place for emergencies only!" \n 
                {name6}: "We were out of Doritos." """)
            if phraseposition == 102:
                st.markdown(f"""{name1}: "{name2}... How do I begin to explain {name2}?" \n
                {name3}: "{name2} is flawless." \n
                {name4}: "I hear {poss_2} hair's insured for $10,000." \n
                {name5}: "I hear {sub_2} do car commercials... in Japan." \n
                {name6}: "One time {sub_2} punched me in the face... it was awesome." """)
            if phraseposition == 103:
                st.markdown(f"""{name1}: "Imagine if someone handed you a box full of all the items you have lost throughout your life." \n
                {name2}: "It would be nice to get my sense of purpose back." \n
                {name3}: "Oh wow, my childhood innocence! Thank you for finding this." \n
                {name4}: "My will to live! I haven't seen this in 10 years!" \n
                {name5}: "I knew I lost that potential somewhere!" \n
                {name6}: "Mental stability, my old friend!"\n
                {name1}: "Guys, could you lighten up a little?" """)


    submitted = st.form_submit_button("Generate")
    if submitted:
        frase()



