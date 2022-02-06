import functions, os

os.system('clear')

functions.directions_screen()
repeat = True
while repeat:
    a = functions.run_game()
    if a == 'n':
        repeat = False
    else:
        os.system('clear')

print('Game ended!')