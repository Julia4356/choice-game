define narrator = Character("Narrator", window_style="narrator_window")

init:
    # Custom style for the narrator's text box
    style narrator_window is default:
        xalign 0.5
        yalign 0.85  # Lower part of the screen, but not all the way down
        xsize 900  # Width of the box
        ysize 150  # Height of the box
        background "#000000"  # Black box
        padding 15

    style namebox is default:
        background "#ffffff"  # White name box
        color "#000000"       # Black name text
        padding 5
        xalign 0.5            # 0.5 = Centered

        init:
    transform speaker:
        alpha 1.0
        linear 0.2 alpha 1.0

    transform dimmed:
        alpha 0.4
        linear 0.2 alpha 0.4

        style choice_button is default
    style choice_button:
        background "#ffffff10"  # semi-transparent white background
        foreground "#ffffff"    # text color
        font "DejaVuSans.ttf"   # or any font you want
        size 28
        xalign 0.5
        padding 10
        outlines [(1, "#00000080", 0, 0)]  # subtle black outline

    style choice_button_hover is choice_button
    style choice_button_hover:
        background "#ffffff30"  # brighter background on hover
        foreground "#ffcc00"    # yellowish text when hovered


label start:

    # Set a simple grey background
    scene expression Solid("#888888")

    # Narration begins
    narrator "They say the truth always comes to light. But sometimes..."
    narrator "It’s buried deep — under power, under fear."
    narrator "I’ve chased stories before. Some made headlines. Others nearly got me killed."
    narrator "But this one..."
    narrator "This one is different."
    narrator "People are disappearing. Whispers of illegal weapons, strange experiments."
    narrator "And at the center of it all… a corporation with too much to hide."
    narrator "And only one person capable of exposing them."
    narrator "And that man is..."

    scene police_office with fade
    show james neutral

    define j = Character("James")
    define s = Character("Chief")
    define l = Character("Lin Richfield")
    define v = Character("Veronica Grey")
    define d = Character("Dean Vale")
    define librarian = Character("Librarian")
    define t = Character("Thomas Blackwell")
    define e = Character("Edd Parker")
    define JL = Character("Julia Lioren")

    show james neutral at left speaker
    j "You called, Chief?"
    show chief serious at right speaker
    show james neutral at left dimmed
    s "Rivers. Close the door behind you."
    show james neutral at left speaker
    show chief serious at right dimmed
    j "That bad, huh?"
    show chief serious at right speaker
    show james neutral at left dimmed
    s "Worse."
    show james concerned at left speaker
    show chief serious at right dimmed
    j "Alright. Hit me with it."
    show chief holding papers at right speaker
    show james concerned at left dimmed
    s "You've been following the Allbright Corporation reports, right?"
    show james serious at left speaker
    show chief holding papers at right dimmed
    j "The ones involving missing persons, rumors of weapons testing, and a whole lot of people staying quiet? Yeah. Hard to miss."
    show chief crossed arms at right speaker
    show james serious at left dimmed
    s "Well, we've got a problem. A body showed up this morning. Third one in two weeks."
    show james tense at left speaker
    show chief crossed arms at right dimmed
    j "Let me guess — unidentifiable wounds, strange residue, no witnesses?"
    show chief crossed arms at right speaker
    show james tense at left dimmed
    s "You're getting good at this."
    show james smirk at left speaker
    show chief crossed arms at right dimmed
    j "It's almost like I do this for a living."
    show chief concerned at right speaker
    show james smirk at left dimmed
    s "Listen, Rivers... This case is bigger than either of us thought. We're hitting walls everywhere. I need you to dig."
    show james amused at left speaker
    show chief concerned at right dimmed
    j "You're bringing me in now? Must mean you’re desperate."
    show chief crossed arms at right speaker 
    show james amused at left dimmed
    s "Desperate enough to give you access to restricted evidence, confidential files... and one name."
    show james confused at left speaker
    show chief crossed arms at right dimmed
    j "And who might that be?"
    show chief serious at right speaker
    show james intrigued at left dimmed
    s "Lin Richfield. She’s a top-level scientist. Works alone. Brilliant, but… well, she doesn’t play well with others."
    show james intrigued at left speaker
    show chief serious at right dimmed
    j "Sounds like my kind of person."
    show chief stern at right speaker
    show james intrigued at left dimmed
    s "I’m serious, Rivers. She’s difficult. Unpredictable. But she’s the only one who can help us get to the bottom of this."
    show chief holding papers at right speaker
    show james confused at left dimmed
    s "She’s been working on classified projects tied to Allbright — nuclear testing, chemical compounds, weaponized research... all the stuff we’ve been hitting dead ends on."
    show james confused at left speaker
    show chief holding papers at right dimmed
    j "So, you’re saying I need to convince her to help me crack this case?"
    show chief uneasy at right speaker
    show james confused at left dimmed
    s "I’m not saying it’ll be easy. I’m saying we don’t have another option. But... be careful. If she refuses, you’re on your own."
    show james determined at left speaker
    show chief uneasy at right dimmed
    j "I’ll take my chances."
    show chief warning at right speaker
    show james determined at left dimmed
    s "Just know this, Rivers — she doesn’t trust anyone. Especially people like you."
    show james shrugging at left speaker
    show chief warning at right dimmed
    j "Well, she hasn’t met anyone like me then."
    show chief warning at right speaker
    show james shrugging at left dimmed
    s "Don’t underestimate her. And don’t think you can charm your way through this one. She’s smarter than that."
    show james smirk at left speaker
    show chief warning at right dimmed
    j "I’ll keep that in mind."
    show james confident at left speaker
    show chief concerned at right dimmed
    j "Thanks, Chief. But I've gotta go. There's no time to waste."
    show chief panicked at right speaker
    show james confused at left dimmed
    s "Rivers, wait!" 
    show chief concerned at left speaker
    show james neutral at left dimmed
    s "You think you know everything, but this is no ordinary case. You need to be careful."

    menu:
    "Leave without hearing the Chief out":
        jump leave_without_advice

    "Hear the Chief out":
        jump listen_to_advice

label leave_without_advice:
    show james reassuring at left speaker
    show chief concerned at right dimmed
    j "I appreciate the concern, but I’ve got this, Chief." 
    hide james
    show chief concerned at right speaker
    s "Rivers, don't be a fool..."
    hide chief
    narrator "And he left. Just like that."
    narrator "Maybe too fast. Maybe too sure of himself."
    jump next_scene

label listen_to_advice:
    show james neutral at left speaker
    show chief concerned at right dimmed
    j "What is it, Chief? I’m listening."
    show chief serious at right speaker
    show james neutral at left dimmed
    s "You don’t know who you’re dealing with. Lin’s more than she seems."
    show james thoughtful at left speaker
    show chief serious at right dimmed 
    j "..."
    show james confident at left speaker
    show chief concerned at right dimmed
    j "It'll be alright, Chief. I got this."
    hide chief
    hide james
    narrator "And with that, he stepped out into the unknown."
    jump next_scene

    label next_scene:
    # This is the shared continuation
    scene bg street_day with fade
    show james thoughtful at left speaker
    j "Alright, Lin Richfield..."
    show james amused at left speaker
    j "The Chief said you were the best — and the most impossible to work with."
    show james thinking at left speaker
    j "Now... how the hell do I even find her?"
    show james annoyed at left speaker
    j "Perfect."
    hide james at left 
    narrator "James's phone buzzed."
    show james holding phone at left speaker
    j "Hm ?"
    hide james
    narrator "A message from the chief."
    # Display the text as if he's reading it
    window hide
    pause 0.5
    centered "Sent you a possible location. Don’t scare her off. — Chief"
    pause 1.0
    window show
    show james putting phone back at left speaker
    j "..."
    show james thoughtful at left speaker
    j "...A library?"
    show james smirk at left speaker 
    j "Hiding in plain sight. Clever."
    hide james
    narrator "He pocketed the phone, the sounds of the city fading as he turned toward the quiet part of town."
    jump approach_lin_library

    label approach_lin_library:

    scene bg library_day with fade
    show james neutral at left

    narrator "The air was still inside the old city library — dust drifting through light shafts, pages rustling in the distance."
    show james smirk at left speaker 
    j "Figures she'd hide out in a place like this."
    hide james
    narrator "The library, with its towering shelves and the scent of old paper, felt like a maze. James wasn’t in the mood to waste time."

    menu:
        "Ask the librarian for Lin Richfield's location":
            jump ask_librarian

        "Look for Lin himself":
            jump find_lin_by_himself

           
            label ask_librarian:

    show james neutral at left speaker
    j "Excuse me. I’m looking for someone — Lin Richfield. Has she been around today?"
    show librarian neutral at right speaker
    show james neutral at left dimmed
    librarian "Dr. Richfield? She’s upstairs. Rarely talks to anyone. Most folks don’t even know she’s here."
    show james shrugging at left speaker
    show librarian neutral at right dimmed
    j "Well, I’m not most folks."
    show librarian serious at right speaker 
    show james shrugging at left dimmed 
    librarian "She doesn’t like being disturbed."
    show james confident at left speaker
    show librarian serious at right dimmed
    j "Noted."
    hide james
    hide librarian
    narrator "He followed the librarian’s vague directions, weaving past shelves and academic silence until he reached a restricted corner of the library."
    narrator "Then he saw it. A door marked 'Staff Only', slightly ajar. Beyond it — a soft glow and the hum of electronics."
    jump meet_lin

    label find_lin_by_himself:

    narrator "He wandered past endless shelves — biographies, scientific journals, tomes on theoretical physics. No sign of Lin."
    show james annoyed at left speaker
    j "Could be anywhere in here…"
    show james surprised
    j "...!" at left speaker
    hide james
    narrator "Then he saw it. A door marked 'Staff Only', slightly ajar. Beyond it — a soft glow and the hum of electronics."
    jump meet_lin


    default lin_relationship = 0  # Hidden variable to track relationship with Lin
    label meet_lin:

    scene bg library_stairs with fade
    narrator "As he opened the door, he was met with the sight of a narrow staircase, half-hidden behind a sagging shelf of encyclopedias."
    narrator "No signs. No noise. Just a faint blue glow spilling from above."
    show james tense at left speaker
    j "Guess this is it..."
    hide james
    narrator "Each step creaked underfoot. The kind of sound that made you feel like you were being watched."
    show james tense at left speaker
    j "Definitely not a public area..."
    hide james
    scene bg library_upper_floor with dissolve
    narrator "At the top, the air shifted — colder, quieter. This wasn’t just a study nook. It felt... fortified."
    show james cautious at left speaker
    j "Lin Richfield?"
    hide james
    narrator "No answer. Just the low hum of machines and the faint tapping of keys."
    narrator "He raised a hand and knocked. Firm, but not aggressive."
    narrator "Silence. Then — footsteps. Light. Cautious. The door creaked open."
    show lin neutral at right speaker
    show james confused at left dimmed
    l "You’re late. I said chamomile this time."
    show james confused at left speaker 
    show lin neutral at right dimmed
    j "...Chamomile?"
    show lin annoyed at right speaker
    show james confused at left speaker
    l "Who is this ? Are you a trainee or something ? Now leave before I do it myself."
    menu:
    "Cut to the chase":
        $ lin_relationship += 1  # More direct, bold
        jump lin_direct

    "Start with manners":
        $ lin_relationship -= 1  # More reserved
        jump lin_polite

    label lin_direct :
        label lin_direct:
    show james serious at left speaker 
    show lin annoyed at right dimmed
    j "I’m here about Allbright."
    hide james
    narrator "Her expression hardened. The air in the room felt colder."
    show lin skeptical at right speaker
    l "...You're either brave, stupid, or desperate."
    show james shrugging at left speaker
    show lin skeptical at right dimmed
    j "Why not all three?"
    show lin annoyed at right speaker
    show james shrugging at left dimmed
    l "People who say that name out loud tend to disappear. You planning on joining them?"
    show james smirk at left speaker
    show lin annoyed at right dimmed
    j "Not if you help me figure out what they’re hiding."
    show lin irritated at right speaker 
    show james smirk at left dimmed
    l "Look, I don't have the time for this- just who even are you ?"
    show james neutral at left speaker
    show lin irritated at right dimmed
    j "James Rivers, journalist working at the WZNT Radio."
    show lin skeptical at right speaker 
    show james neutral at left dimmed
    l "And what's a journalist like you getting involved in a criminal case? Don't you care about your reputation ?"
    show james serious at left speaker 
    show lin skeptical at right dimmed
    j "That's not important right now. I came here for a reason, and I think you might as well know just as much as I do about the Allbright case."
    show lin crossed arms at right speaker 
    show james serious at left dimmed
    l "I don't know what you're talking about-"
    show james serious at left speaker 
    show lin crossed arms at right dimmed
    j "Yes, you do. People are dying. And they won't stop. That's why I'm here."
    show lin wary at right speaker
    show james serious at left dimmed
    l "..."
    show james slightly worried at left speaker 
    show lin wary at right dimmed
    j "I need your help. Please."
    show lin skeptical at right speaker 
    show james slightly worried at left dimmed
    l "You do realize I work alone, right? No interns, no partners, no tag-alongs. So why chase me down when there are a dozen eager experts who'd jump at this?"
    show james serious at left speaker 
    show lin wary at right dimmed
    j "Because they’d follow orders. You’d follow the truth."
    jump after_lin_convo

    label lin_polite :
    show james neutral at left speaker 
    show lin neutral at right dimmed
    j "James Rivers. Journalist, working with WZNT Radio. May I come in?"
    show lin annoyed at right speaker 
    show james neutral at left dimmed
    l "A journalist?"  
    show lin skeptical at right speaker 
    show james neutral at left dimmed
    l "Right. Because media involvement always makes these things better."
    show james serious at left speaker 
    show lin skeptical at right dimmed
    j "I’m not here to stir the pot. I just need to ask a few questions... about Allbright."
    show lin irritated at right speaker 
    show james serious at left dimmed
    l "You walked all the way here to ask about a ghost corporation? That’s bold — and incredibly stupid."
    show james stern at left speaker 
    show lin irritated at right dimmed
    j "I know you’re connected to the case. You’ve seen what’s happening."
    show lin cold at right speaker 
    show james worried at left dimmed
    l "You need to leave."
    hide lin
    narrator "She stepped back toward the door, already beginning to close it."
    show james desperate at left speaker 
    j "Wait—please ! I’ve lost people. Good people... And I know you’ve seen it too."
    show lin wary at rigyt speaker 
    show james desperate at left dimmed
    l "..."
    show james worried at left speaker 
    show lin wary at right dimmed
    j "I'm not looking for a headline. I'm looking for someone who understands what this really is."
    show james slightly worried at left speaker 
    show lin wary at right dimmed
    j "I need your help. Please."
    jump after_lin_convo

    label after_lin_convo :
    show lin reluctant
    l "...come in."
    hide lin
    scene bg lin_studio with fade
    with dissolve
    narrator "Lin led James through a narrow hallway into what looked more like a bunker than a bureau — piled-up boxes, papers on the floor, pictures of crime scenes pinned to every surface."
    show lin holding papers at right speaker
    show james curious at left dimmed
    l "Don’t mind the mess. Careful not to trip."
    show james smirk at left speaker
    show lin holding papers at right dimmed 
    j "Noted."
    if lin_relationship >= 1:
        show lin narrowing eyes at right speaker
        show james smirk at left dimmed
        l "You're persistent. I hate that. But it means you're not wasting my time."
    else:
        show lin cold at right speaker
        show james tense at left dimmed
        l "This doesn't mean I trust you. You're still an outsider."
    show james serious at left speaker
    show lin annoyed at right dimmed
    j "I don’t expect trust. I expect facts."
    show lin serious at right speaker
    show james serious at left dimmed
    l "Then you’re in the wrong place — facts are exactly what Allbright has been trying to erase."
    hide lin
    hide james
    narrator "She moved to a table stacked with folders, stopping just short of handing him one She then turned around to face him and said..."
    show lin guarded at right speaker
    show james tense at left dimmed
    l "What I show you doesn't leave this room. Not without my say-so. Understood ?"
    menu:
        "Agree without hesitation":
            $ lin_relationship += 1
            jump agree_without_hesitation

        "Hesitate, then agree":
            $ lin_relationship -= 1
            jump agree_with_hesitation


    label agree_without_hesitation:
    show james serious at left speaker
    show lin guarded at right dimmed
    j "You have my word."
    show lin thinking at right speaker
    show james serious at left dimmed
    l "..."
    hide Lin
    hide james
    narrator "She studied him for a second. Then moved on like nothing needed to be said."
    jump after_agreement

    label agree_with_hesitation:
    show james hesitant at left speaker
    show lin guarded at right dimmed
    j "..."
    show lin annoyed at right speaker
    show james hesitant at left dimmed 
    l "...So? Didn't get a response from you."
    show james conflicted at left speaker
    show lin annoyed at right dimmed
    j "...Yeah. I understand."
    show lin skeptical at right speaker
    show james conflicted at left dimmed
    l "Hm."
    hide lin
    hide james
    narrator "She didn't look convinced."
    jump after_agreement

    label after_agreement :
    show lin holding papers at right speaker
    show james neutral at left dimmed
    l "The files I’m about to show you don’t exist. Officially."



























    label determine_ending:
    if lin_relationship >= 2:
        jump ending_romantic
    else:
        jump ending_professional











