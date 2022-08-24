game_array = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]

game_board = None


def update():
    global game_board
    game_board = f"""{game_array[0]} | {game_array[1]} | {game_array[2]} 
-----------
{game_array[3]} | {game_array[4]} | {game_array[5]} 
-----------
{game_array[6]} | {game_array[7]} | {game_array[8]} """


update()
print(game_board)

print("""How to place the nots and cross:
From number keys 1 to 9, with 1 being top left and 9 being bottom right
moving to the right and down""")


def placing(position, sign):
    global game_array
    if int(position) > 0 and int(position) < 10:
        grid_number = int(position) - 1
        if game_array[grid_number] == " ":
            game_array[grid_number] = f"{sign}"
            update()
            print(game_board)
            return "success"
        else:
            print("grid already taken")
            return "fail"

def win():
    i = game_array
    winner = (i[0] == i[1] == i[2] and i[0] != " " and i[0]) or (i[3] == i[4] == i[5] and i[3] != " " and i[3]) or (i[6] == i[7] == i[8] and i[6] != " " and i[6]) or (i[0] == i[3] == i[6] and i[0] != " " and i[0]) or (i[1] == i[4] == i[7] and i[1] != " " and i[1]) or (i[2] == i[5] == i[8] and i[2] != " " and i[1]) or (i[0] == i[4] == i[8] and i[0] != " " and i[0]) or (i[2] == i[4] == i[6] and i[2] != " " and i[2]) or "no winner"
    return winner


game_is_finished = False
while not game_is_finished:
    game_turn = "n/a"
    while game_turn != "success":
        placement_x = input("X: Where do you want to place your cross?  ")
        game_turn = placing(placement_x, "x")

    winner = win()
    if winner != "no winner":
        print(f"THE WINNER IS {winner.upper()}")
        game_is_finished = True
        break
    elif len(set(game_array)) == 2 and "x" in game_array and "o" in game_array:
        print("It's a draw!")
        game_is_finished = True
        break

    game_turn = "n/a"
    while game_turn != "success":
        placement_o = input("O: Where do you want to place your nought?  ")
        game_turn = placing(placement_o, "o")

    winner = win()
    if winner != "no winner":
        print(f"THE WINNER IS {winner.upper()}")
        game_is_finished = True
    elif len(set(game_array)) == 2 and "x" in game_array and "o" in game_array:
        print("It's a draw!")
        game_is_finished = True



