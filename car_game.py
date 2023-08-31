command_list = """ 
start - to turn ON the engine 
stop - to turn OFF the engine 
quit - to exit
"""
user_input = ""
is_engine_running = False

while True:
    user_input = input('> ').lower()

    if user_input == "start":
        if is_engine_running:
            print('Engine is already ON')
        else:
            is_engine_running = True
            print('Engine is ON')
    elif user_input == "stop":
        if not is_engine_running:
            print('Engine is already OFF')
        else:
            is_engine_running = False
            print('Engine is OFF')
    elif user_input == "help":
        print(command_list)
    elif user_input == "quit":
        break
    else:
        print('I did not understand. Write "Help" to see the command list')

