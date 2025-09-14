
board_size = 10

print("enter the start position of the carrier:__,__") #carrier tuple
input_user = input("enter coordinates:")
x_coordiante_carrier= input_user.split(",")[0]
y_coordinates_carrier= input_user.split(",")[1]
print(x_coordiante_carrier,"and",end = "")
print(y_coordinates_carrier)
Carrier_coor_tup = (x_coordiante_carrier,y_coordinates_carrier)
print(Carrier_coor_tup)

print("enter the start position of the :__,__") #submarine tuple
input_user = input("enter coordiantes of sub:")
x_coordiante_sub= input_user.split(",")[0]
y_coordinates_sub= input_user.split(",")[1]
print(x_coordiante_sub,"and",end="")
print(y_coordinates_sub)
Suba_coor_tup = (x_coordiante_sub,y_coordinates_sub)
print(Suba_coor_tup)

Ship_details = {"Carrier":{'length':4 , "ship_position":Carrier_coor_tup},
                "Submarine":{"length":4 , "ship_position":Suba_coor_tup}}
#dictionary for the details


board = list() #instead of printing out, update board
for i in range(board_size+1):
    if i % 10 != 0:
        board.append(['0']*10) #insert list with 10 elements for a row, repeat 10 times


print(Ship_details["Carrier"])
print(Ship_details["Submarine"])

def place_carrier(ship_details): #operation to be repeated
    ship_position = ship_details["Carrier"]["ship_position"] #extract details from the dictionary
    ship_length = ship_details["Carrier"]["length"]
    ship_x = int(ship_position[0])
    ship_y = int(ship_position[1])
    board[ship_y][ship_x] = "X"
    for i in range(ship_length):
        board[ship_y][ship_x+i] = "X"
    return ship_position

def place_sub(ship_details): #place sub vertically
    ship_position = ship_details["Submarine"]["ship_position"] #extract details from the dictionary
    ship_length = ship_details["Submarine"]["length"]
    ship_x = int(ship_position[0])
    ship_y = int(ship_position[1])
    board[ship_y][ship_x] = "X"
    for i in range(ship_length):
        board[ship_y+i][ship_x] = "Y"
    return ship_position

place_carrier(Ship_details)
place_sub(Ship_details)


for i in board: #print board
    print(i)




