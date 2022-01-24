old_command_value = ""

while True:
        new_command_value = input(">").lower()
        if new_command_value == old_command_value:
            print(f"Heyy! you already press this same key")
            continue
        else:
            old_command_value = new_command_value
        if old_command_value == "help":
            print("start - to start the car")
            print("stop - to stop the car")
            print("quit - to exit")
        elif old_command_value == "start":
            print("Wow your game is start ... ready for play!")
        elif old_command_value == "stop":
            print("Your game stopped")
        elif old_command_value == "quit":
             break
        else:
            print("Your command is wrong")