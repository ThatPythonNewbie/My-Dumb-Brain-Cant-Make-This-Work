import os
from time import sleep

print("  _______ _    _ ______ ")
print(" |__   __| |  | |  ____|")
print("    | |  | |__| | |__   ")
print("    | |  |  __  |  __|  ")
print("    | |  | |  | | |____ ")
print("    |_|  |_|  |_|______|")
sleep(0.3)
print("  _      ____  _   _  _____ ")
print(" | |    / __ \| \ | |/ ____|")
print(" | |   | |  | |  \| | |  __ ")
print(" | |   | |  | |     | | |_ |")
print(" | |___| |__| | |\  | |__| |")
print(" |______\____/|_| \_|\_____|")
sleep(0.3)
print("       _  ____  _    _ _____  _   _ ________     __")
print("      | |/ __ \| |  | |  __ \| \ | |  ____\ \   / /")
print("      | | |  | | |  | | |__) |  \| | |__   \ \_/ / ")
print("  _   | | |  | | |  | |  _  /|     |  __|   \   /  ")
print(" | |__| | |__| | |__| | | \ \| |\  | |____   | |   ")
print("  \____/ \____/ \____/|_|  \_\_| \_|______|  |_|   ")
sleep(0.3)
print(" ")
print("-----Start-----")
print("-----Options-----")
print("-----Quit-----")
menu = input("Type a command to continue>")
if menu == "start" or menu == "Start" or menu == "START":
    os.system("python launchmenu.py")

if menu == "options" or menu == "Options" or menu == "OPTIONS":
    os.system("python options.py")

if menu == "quit" or menu == "Quit" or menu == "QUIT":
    quit()