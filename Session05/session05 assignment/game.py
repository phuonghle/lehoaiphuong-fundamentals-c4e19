# SOKOBAN

# Create the game

map = {
    "size_x" : 5,
    "size_y" : 5
}


player = {
    "x" : 2,
    "y" : 3
}

boxes = [
    {"x" : 1, "y" : 1},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 3}
]


destinations = [
    {"x" : 2, "y" : 1},
    {"x" : 3, "y" : 2},
    {"x" : 3, "y" : 1}
]

# loop until ends
playing = True
while playing:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):

            # set conditions

            player_is_here = False

            if x == player["x"] and y == player["y"]:
                player_is_here = True


            box_is_here = False

            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True

            destination_is_here = False

            for destination in destinations:
                if destination["x"] == x and destination["y"] == y:
                    destination_is_here = True

            # print out

            if player_is_here:
                print("P  ", end="")
            elif box_is_here:
                print("B  ", end="")
            elif destination_is_here:
                print("D  ", end="")
            else:
                print("-  ", end="")    

        print()


    # movement

    move = input("Your move: ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        print("Buzzz")
        playing = False



    # prevent P from going out of screen

    if 0 <= player["x"] + dx < map["size_x"] and 0 <= player["y"] + dy < map["size_y"]:
        player["x"] += dx
        player["y"] += dy
        
    # prevent B from going out of screen

    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player["y"]:
            box["x"] += dx
            box["y"] += dy


    # Check if player win the game: every D has been replaced by B


    # Player can’t push box out of map


    # Player can’t push multiple boxes


    # Add Obstacle or Wall into map, player can’t move across Obstacle and can’t push box over Obstacle
