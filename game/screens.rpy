# screens.rpy

screen main_menu():
    tag menu
    
    # Background image (dark cityscape, or any image that fits your theme)
    add "cover_image.png"  # Your cover page background image
    
    # Optional: Add a gradient or dark overlay effect
    window:
        xalign 0.5
        yalign 0.6
        style "menu_window"  # Add custom window style if desired

    # Title text (adjust to fit your game theme)
    vbox:
        xalign 0.5
        yalign 0.3
        spacing 10
        
        # Main title
        text "Chasing Shadows" size 70 color "#FFFFFF" font "fonts/your_font.ttf"  # Game title
        text "A Detective Story" size 40 color "#AAAAAA" font "fonts/your_font.ttf"  # Subtitle (optional)

    # Buttons for the main menu
    vbox:
        xalign 0.5
        yalign 0.7
        spacing 20
        
        # Start Button (replace with your custom button images)
        imagebutton auto "start_button_%s.png" action Start()
        
        # Load Button (to load saved games)
        imagebutton auto "load_button_%s.png" action ShowMenu("load")
        
        # Preferences Button (for settings like sound, display, etc.)
        imagebutton auto "preferences_button_%s.png" action ShowMenu("preferences")
        
        # Quit Button
        imagebutton auto "quit_button_%s.png" action Quit()
# screens.rpy

screen main_menu():
    tag menu
    frame:
        # Background for the main menu screen
        add "main_menu_bg.png"  # Replace with your actual background image

        vbox:
            textbutton "Start Game" action Start()  # Starts the game from the beginning
            textbutton "Load Game" action ShowMenu("load")  # Opens the load game screen
            textbutton "Preferences" action ShowMenu("preferences")  # Opens the preferences screen
            textbutton "Quit" action Quit(confirm=True)  # Confirms and exits the game

screen load():
    tag menu
    frame:
        vbox:
            text "Load Game"
            for save in renpy.playable_saves():  # Loops through the saved games
                textbutton save.name action Load(save)  # Each button corresponds to a saved game
            textbutton "Back" action Return()  # Goes back to the main menu

screen preferences():
    tag menu
    frame:
        vbox:
            text "Preferences"
            
            hbox:
                text "Music Volume"
                bar value music_volume  # Adjusts the music volume
            hbox:
                text "Sound Volume"
                bar value sound_volume  # Adjusts the sound effects volume
            
            textbutton "Back" action Return()  # Goes back to the main menu
