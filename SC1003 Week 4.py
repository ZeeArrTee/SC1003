board_size = 10
n = 0
x_attack = int(input("please input the column youre attacking:"))
y_attack = int(input("please input the row youre attacking:"))

while (x_attack < 0 or x_attack > 10 ) or (y_attack < 0 or y_attack > 10):
    print ('invalid coordinated please input again')
    x_attack = int(input("please input the column youre attacking:"))
    y_attack = int(input("please input the row youre attacking:"))
    continue
else:
    print("valid coordaintes")

for n in range(board_size):
    if n == y_attack: #to choose when the input chooses the y axis row
        for n in range(board_size): #per row 0s
            if n == x_attack:
                print ("1",end="") #x axis attack
            else:
                print("0",end="")
        print("")
    else:
        for n in range(board_size):
            print("0", end="")
        print("")