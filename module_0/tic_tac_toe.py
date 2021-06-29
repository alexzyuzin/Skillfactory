# Tic Tac Toe for human vs computer. Computer makes random moves.
# Here we take code from the Skill factory course and update it
# with the change of one player with computer.

import random


# By definition we set X to computer, 0 to player.
machine = '0'
human = 'X'
first_player = human
count = 1


# Function which determines the game-board.
def show(field):
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, j in enumerate(field):
        print(f"  {i} | {' | '.join(j)} | ")
        print("  --------------- ")
    print()


# Function which determines the game-board. Taken from course.
def check_win(field):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show(field)
            print("You win.")
            return True
        if symbols == ["0", "0", "0"]:
            show(field)
            print("You lost.")
            return True
    return False


# Computer moves. Return two random integers in the interval [0, 2]
def machine_move():
    return random.randint(0, 2), random.randint(0, 2)


# Ask for input from player. Computer enters random numbers and checks for overlap.
def ask_turn(player, field):
    while True:
        if player is machine:
            cord_x, cord_y = machine_move()

            if field[cord_x][cord_y] != " ":
                continue

        else:
            cords = input("         Your turn: ").split()
        
            if len(cords) != 2:
                print(" Enter two coordinates. ")
                continue
        
            cord_x, cord_y = cords
        
            if not(cord_x.isdigit()) or not(cord_y.isdigit()):
                print(" Enter numbers. ")
                continue
        
            cord_x, cord_y = int(cord_x), int(cord_y)
        
            if 0 > cord_x or cord_x > 2 or 0 > cord_y or cord_y > 2:
                print(" Out of range input. Try again. ")
                continue
        
            if field[cord_x][cord_y] != " ":
                print(" Place was already filled. Try again. ")
                continue
        
        return cord_x, cord_y


# Switch the player based on how many moves have been made.
def switch_player(turn):
    current_player = machine if turn % 2 == 0 else human
    return current_player


# Asks if player wants to play again.
def replay():
    play_again = input("Do you want to play again (y/n) ? ")
    if play_again.lower() == 'y':
        return True
    if play_again.lower() == 'n':
        return False


# Clears field before and after the game.
def clear_field():
    field = [[" "] * 3, [" "] * 3, [" "] * 3]
    return field


# Main game function.
def game(player, turn):
    field = clear_field()
    while True:
        show(field)
        x, y = ask_turn(player, field)
    
        if turn % 2 == 0:
            print("         Computer moves....")
            field[x][y] = machine
        else:
            field[x][y] = human
    
        if check_win(field):
            if not replay():
                break
            else:
                turn = 0
                field = clear_field()

        if turn == 9:
            print(" Tie")
            if not replay():
                break
            else:
                turn = 0
                field = clear_field()

        turn += 1
        player = switch_player(turn)


game(first_player, count)
