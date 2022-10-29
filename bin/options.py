import os
from time import sleep

print("lol there are no options, this game runs on a command prompt")
sleep(0.5)
print("I know, I know, you'll probably be saying: Why did you make an options menu if you dont need one?")
sleep(0.7)
print("Well, because all games have one.")
sleep(0.3)
back = input("Input the command back to go back to the main menu, type any other command to quit>")
if back == "back" or back == "Back" or back == "BACK":
    os.system("python main.py")
else:
    quit()