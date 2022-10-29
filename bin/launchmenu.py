import os
from time import sleep

print("-----New Game-----")
print("-----Load Game-----")
launch = input("Input a comand, new to start a new game, load to load the latest autosave, and back to go back to the main menu>")
if launch == "new" or launch == "New" or launch == "NEW":
    os.system("python  game_scenarios/a1_ph1_beggining.py")
if launch == "load" or launch == "Load" or launch == "LOAD":
    print("Sorry, this feature isn't available yet. Maybe wait a little  bit until I figure out how to do a save/load system.")
    launch
if launch == "back" or launch == "Back" or launch == "BACK":
    os.system("python main.py")