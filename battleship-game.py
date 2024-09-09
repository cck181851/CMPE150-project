def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")

def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")

def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
     


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")

def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")



def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")



board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True 

print_rules()



try:
    player1_board = [[['-' for _ in range(10)] for _ in range(10)], [['-' for _ in range(10)] for _ in range(10)]]
    player2_board = [[['-' for _ in range(10)] for _ in range(10)], [['-' for _ in range(10)] for _ in range(10)]]

    is_placement_confirmed1 = False
    occupied_coordinates1 = []

    # Player 1 ship placement
    while not is_placement_confirmed1:
        current_board1 = [[['-' for _ in range(10)] for _ in range(10)], [['-' for _ in range(10)] for _ in range(10)]]
        print_3d_list(current_board1)

        placed_ships1 = []
        available_ships1 = []

        case_number = 0
        while case_number < 5:
            is_input_valid = True
            case_number += 1
            print_ships_to_be_placed()
            ship_list1 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
            lower_ship_list1 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
            displayable_ships1 = [ship for ship in ship_list1 if ship not in available_ships1]
            remaining_ships1 = [ship for ship in lower_ship_list1 if ship not in placed_ships1]
            for ship in displayable_ships1:
                print_single_element(ship)
            print_empty_line()
            print_player_turn_to_place(1)
            print_to_place_ships()
            user_input = input()
            input_list = user_input.split()
            if len(input_list) < 4:
                print_incorrect_input_format()
                case_number -= 1
                is_input_valid = False
                print_3d_list(current_board1)
            else:
                ship_name = input_list[0]
                x_coordinate = input_list[1]
                y_coordinate = input_list[2]

                if is_input_valid:
                    try:
                        x_coordinate = int(x_coordinate)
                        y_coordinate = int(y_coordinate)
                    except:
                        print_incorrect_input_format()
                        case_number -= 1
                        is_input_valid = False

                if is_input_valid:
                    if (x_coordinate not in range(1, 11)) or (y_coordinate not in range(1, 11)):
                        print_incorrect_coordinates()
                        case_number -= 1
                        is_input_valid = False

                if ship_name.lower() in remaining_ships1:
                    if ship_name.lower() == lower_ship_list1[0]:
                        ship_length = 5
                    elif ship_name.lower() == lower_ship_list1[1]:
                        ship_length = 4
                    elif ship_name.lower() in lower_ship_list1[2:4]:
                        ship_length = 3
                    else:
                        ship_length = 2
                elif ship_name.lower() in placed_ships1:
                    if is_input_valid:
                        print_ship_is_already_placed(ship_name.title())
                        case_number -= 1
                        is_input_valid = False
                else:
                    ship_length = 0
                    if is_input_valid:
                        print_incorrect_ship_name()
                        case_number -= 1
                        is_input_valid = False

                orientation = input_list[3]
                if orientation not in ['h', 'v'] and is_input_valid:
                    print_incorrect_orientation()
                    case_number -= 1
                    is_input_valid = False

                if is_input_valid:
                    if orientation == 'h' and x_coordinate <= 10 and x_coordinate + ship_length > 11:
                        print_ship_cannot_be_placed_outside(ship_name.title())
                        case_number -= 1
                        is_input_valid = False
                    if orientation == 'v' and y_coordinate <= 10 and y_coordinate + ship_length > 11:
                        print_ship_cannot_be_placed_outside(ship_name.title())
                        case_number -= 1
                        is_input_valid = False

                if is_input_valid and orientation == 'h':
                    new_ship_coordinates = [(x_coordinate + i, y_coordinate) for i in range(ship_length)]
                    if any(coord in occupied_coordinates1 for coord in new_ship_coordinates):
                        print_ship_cannot_be_placed_occupied(ship_name.title())
                        case_number -= 1
                        is_input_valid = False

                if is_input_valid and orientation == 'v':
                    new_ship_coordinates = [(x_coordinate, y_coordinate + i) for i in range(ship_length)]
                    if any(coord in occupied_coordinates1 for coord in new_ship_coordinates):
                        print_ship_cannot_be_placed_occupied(ship_name.title())
                        case_number -= 1
                        is_input_valid = False

                if orientation == 'h' and is_input_valid and ship_length > 1:
                    for i in range(ship_length):
                        current_board1[0][y_coordinate - 1][x_coordinate - 1 + i] = '#'
                        placed_ships1.append(ship_name.lower())
                        available_ships1 = [ship.title() for ship in placed_ships1]
                    for i in range(ship_length):
                        occupied_coordinates1.append((x_coordinate + i, y_coordinate))

                if orientation == 'v' and is_input_valid and ship_length > 1:
                    for i in range(ship_length):
                        current_board1[0][y_coordinate - 1 + i][x_coordinate - 1] = '#'
                        placed_ships1.append(ship_name.lower())
                        available_ships1 = [ship.title() for ship in placed_ships1]
                    for i in range(ship_length):
                        occupied_coordinates1.append((x_coordinate, y_coordinate + i))
                
                print_3d_list(current_board1)

        while True:
            print_confirm_placement()
            confirmation = input()
            if confirmation in ['N', 'n']:
                occupied_coordinates1 = []
                is_placement_confirmed1 = False
                break
            elif confirmation in ['Y', 'y']:
                is_placement_confirmed1 = True
                break

    is_placement_confirmed2 = False
    occupied_coordinates2 = []

    while not is_placement_confirmed2:
        current_board2 = [[['-' for _ in range(10)] for _ in range(10)], [['-' for _ in range(10)] for _ in range(10)]]
        print_3d_list(current_board2)

        placed_ships2 = []
        available_ships2 = []

        case_number = 0
        while case_number < 5:
            is_input_valid = True
            case_number += 1
            print_ships_to_be_placed()
            ship_list2 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
            lower_ship_list2 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
            displayable_ships2 = [ship for ship in ship_list2 if ship not in available_ships2]
            remaining_ships2 = [ship for ship in lower_ship_list2 if ship not in placed_ships2]
            for ship in displayable_ships2:
                print_single_element(ship)
            print_empty_line()
            print_player_turn_to_place(2)
            print_to_place_ships()
            user_input = input()
            input_list = user_input.split()
            if len(input_list) < 4:
                print_incorrect_input_format()
                case_number -= 1
                is_input_valid = False
                print_3d_list(current_board2)
            else:
                ship_name = input_list[0]
                x_coordinate = input_list[1]
                y_coordinate = input_list[2]

                if is_input_valid:
                    try:
                        x_coordinate = int(x_coordinate)
                        y_coordinate = int(y_coordinate)
                    except:
                        print_incorrect_input_format()
                        case_number -= 1
                        is_input_valid = False

                if is_input_valid:
                    if (x_coordinate not in range(1, 11)) or (y_coordinate not in range(1, 11)):
                        print_incorrect_coordinates()
                        case_number -= 1
                        is_input_valid = False

                if ship_name.lower() in remaining_ships2:
                    if ship_name.lower() == lower_ship_list2[0]:
                        ship_length = 5
                    elif ship_name.lower() == lower_ship_list2[1]:
                        ship_length = 4
                    elif ship_name.lower() in lower_ship_list2[2:4]:
                        ship_length = 3
                    else:
                        ship_length = 2
                elif ship_name.lower() in placed_ships2:
                    if is_input_valid:
                        print_ship_is_already_placed(ship_name.title())
                        case_number -= 1
                        is_input_valid = False
                else:
                    ship_length = 0
                    if is_input_valid:
                        print_incorrect_ship_name()
                        case_number -= 1
                        is_input_valid = False

                orientation = input_list[3]
                if orientation not in ['h', 'v'] and is_input_valid:
                    print_incorrect_orientation()
                    case_number -= 1
                    is_input_valid = False

                if is_input_valid:
                    if orientation == 'h' and x_coordinate <= 10 and x_coordinate + ship_length > 11:
                        print_ship_cannot_be_placed_outside(ship_name.title())
                        case_number -= 1
                        is_input_valid = False
                    if orientation == 'v' and y_coordinate <= 10 and y_coordinate + ship_length > 11:
                        print_ship_cannot_be_placed_outside(ship_name.title())
                        case_number -= 1
                        is_input_valid = False

                if is_input_valid and orientation == 'h':
                    new_ship_coordinates = [(x_coordinate + i, y_coordinate) for i in range(ship_length)]
                    if any(coord in occupied_coordinates2 for coord in new_ship_coordinates):
                        print_ship_cannot_be_placed_occupied(ship_name.title())
                        case_number -= 1
                        is_input_valid = False

                if is_input_valid and orientation == 'v':
                    new_ship_coordinates = [(x_coordinate, y_coordinate + i) for i in range(ship_length)]
                    if any(coord in occupied_coordinates2 for coord in new_ship_coordinates):
                        print_ship_cannot_be_placed_occupied(ship_name.title())
                        case_number -= 1
                        is_input_valid = False

                if orientation == 'h' and is_input_valid and ship_length > 1:
                    for i in range(ship_length):
                        current_board2[1][y_coordinate - 1][x_coordinate - 1 + i] = '#'
                        placed_ships2.append(ship_name.lower())
                        available_ships2 = [ship.title() for ship in placed_ships2]
                    for i in range(ship_length):
                        occupied_coordinates2.append((x_coordinate + i, y_coordinate))

                if orientation == 'v' and is_input_valid and ship_length > 1:
                    for i in range(ship_length):
                        current_board2[1][y_coordinate - 1 + i][x_coordinate - 1] = '#'
                        placed_ships2.append(ship_name.lower())
                        available_ships2 = [ship.title() for ship in placed_ships2]
                    for i in range(ship_length):
                        occupied_coordinates2.append((x_coordinate, y_coordinate + i))
                
                print_3d_list(current_board2)

        while True:
            print_confirm_placement()
            confirmation = input()
            if confirmation in ['N', 'n']:
                occupied_coordinates2 = []
                is_placement_confirmed2 = False
                break
            elif confirmation in ['Y', 'y']:
                is_placement_confirmed2 = True
                break

    attack_board = [['-' for _ in range(10)] for _ in range(10)]
    player1_attack_set = set()
    player2_attack_set = set()

    game_active = True
    player1_turn = True
    while game_active:
        is_attack_valid = True

        while is_attack_valid:
            print_3d_list([player1_board[0], attack_board])
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            try:
                target_x, target_y = input().split()
                target_x = int(target_x)
                target_y = int(target_y)
            except:
                print_incorrect_input_format()
                continue

            if target_x < 1 or target_x > 10 or target_y < 1 or target_y > 10:
                print_incorrect_coordinates()
                continue

            if (target_x, target_y) in player1_attack_set:
                print_tile_already_struck()
            else:
                player1_attack_set.add((target_x, target_y))
                if (target_x, target_y) not in occupied_coordinates2:
                    print_miss()
                    current_board2[1][target_y - 1][target_x - 1] = 'O'
                    attack_board[target_y - 1][target_x - 1] = 'O'
                    hit = False
                    game_active = True
                else:
                    hit = True
                    occupied_coordinates2.remove((target_x, target_y))
                    print_hit()
                    current_board2[1][target_y - 1][target_x - 1] = '!'
                    attack_board[target_y - 1][target_x - 1] = '!'
                    if not occupied_coordinates2:
                        print_3d_list([player1_board[0], attack_board])
                        print_player_won(1)
                        print_thanks_for_playing()
                        game_active = False
                        break

                while hit == False:
                    print_type_done_to_yield(2)
                    if input().lower() == 'done':
                        break
                    else:
                        continue
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()
