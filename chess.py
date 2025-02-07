box = [['___' for _ in range(8)] for _ in range(8)]

# White Default Coin
box[0][0] = "WE1"
box[0][1] = "WH1" 
box[0][2] = "WC1" 
box[0][3] = "WK1" 
box[0][4] = "WQ1" 
box[0][5] = "WC2" 
box[0][6] = "WH2" 
box[0][7] = "WE2" 

box[7][0] = "BE1"
box[7][1] = "BH1" 
box[7][2] = "BC1" 
box[7][3] = "BK1" 
box[7][4] = "BQ1" 
box[7][5] = "BC2" 
box[7][6] = "BH2" 
box[7][7] = "BE2" 

# White
for i in range(1,2):
    num = 1
    for j in range(0,8):
        box[i][j] = "WS" + str(num)
        num += 1
        
#  Black
for i in range(6,7):
    num = 1
    for j in range(0,8):
        box[i][j] = "BS" + str(num)
        num += 1
        
# print box
no = 0
for i in range(8):
    print(f"   {i}",end="")
    
print("")
for row in box:
    print(no," ".join(row))
    no += 1

flag = True
dict_position = {}

# adding Coin in Dictionary
def add_coin(row,col,element):
    out = True
    for k in dict_position:
        if k == element:
            dict_position[f"{element}"][f"{row}{col}"] = 1
            out = False 
            break
    if out == True:
        dict_position.update({f"{element}" : {f"{row}{col}" : 1}})
    
# Check Coin - Which Coin Available position do play
def check_element(row,col,element):
    if element[1] == 'S':
        soldier(row,col,element)
    elif element[1] == "E":
        elephant(row,col,element)
    elif element[1] == "H":
        horse(row,col,element)
    elif element[1] == "C":
        camel(row,col,element)
    elif element[1] == "K":
        king(row,col,element)
    elif element[1] == "Q":
        queen(row,col,element)
    
    
# CHECKMATE KING FUNCTION
def checkmate_king(row,col,element):
    if "K" in box[row][col] and element[0] != box[row][col]:
        print("\n --------- Checked ---------")
    
    
#  soldier code
def soldier(row,col,element):
    # White
    if element[0] == "W":
        #  Center
        if row+1 <= 7:
            if box[row+1][col] == "___":
                print(f"{element} : {row+1} {col}")
                add_coin(row+1,col,element)
        else:
            return
        
        # left
        if row+1 <= 7 and col-1 >= 0:
            if "B" in box[row+1][col-1]:
                print(f"{element} : {row+1} {col-1}")
                add_coin(row+1,col-1,element)
                checkmate_king(row,col,element)
                
        # right
        if row+1 <= 7 and col+1 <= 7:
            if "B" in box[row+1][col+1]:
                print(f"{element} : {row+1} {col+1}")
                add_coin(row+1,col+1,element)
                checkmate_king(row,col,element)
                
    if element[0] == "B":
        #  Center
        if row-1 >= 0:
            if box[row-1][col] == "___":
                print(f"{element} : {row-1} {col}")
                add_coin(row-1,col,element)
        else:
            return
        # left
        if row-1 >= 0 and col-1 >= 0:
            if "W" in box[row+1][col-1]:
                print(f"{element} : {row-1} {col-1}")
                add_coin(row-1,col-1,element)
                checkmate_king(row,col,element)
        # right
        if row-1 >= 0 and col+1 <= 7:
            if "W" in box[row-1][col+1]:
                print(f"{element} : {row-1} {col+1}")
                add_coin(row-1,col+1,element)
                checkmate_king(row,col,element)
                

# COMON COIN FUNCTION
def comon_coin(row,col,element):
    global flag
    if box[row][col] == "___":
        print(f"{element}: {row} {col}")
        add_coin(row,col,element)
    elif element[0] not in box[row][col]:
        print(f"{element}: {row} {col}")
        add_coin(row,col,element)
        flag = False
        checkmate_king(row,col,element)
    elif element[0] in box[row][col]:
        flag = False
        
        
# Elephant code
def elephant(i,j,element):
    global flag
    # Position - UP
    row = i
    col = j
    flag = True
    while(flag==True):
        if row-1 >= 0:
            row-=1
            comon_coin(row,col,element)
        else:
            break
        
    # Position - DOWN
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1 <= 7:
            row+=1
            comon_coin(row,col,element)
        else:
            break
        
    # Position - RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if col+1 <= 7:
            col+=1
            comon_coin(row,col,element)
        else:
            break
        
    # Position - LEFT
    row = i
    col = j
    flag = True
    while(flag==True):
        if col-1 >= 0:
            col-=1
            comon_coin(row,col,element)
        else:
            break
        
#  CHECK HORSE FUNCTION
def check_horse(row,col,element):
    if element[0] in box[row][col]:
        pass
    else:
        print(f"{element} : {row} {col}")
        add_coin(row,col,element)
        checkmate_king(row,col,element)
        
               
        
#  Horse Code
def horse(row,col,element):
    # UP
    if row-2>=0 and col+1<=7:
        check_horse(row-2,col+1,element)
    if row-2>=0 and col-1>=0:
        check_horse(row-2,col-1,element)
        
    # DOWN
    if row+2<=7 and col+1<=7:
        check_horse(row+2,col+1,element)
    if row+2<=7 and col-1>=0:
        check_horse(row+2,col-1,element)
        
    # RIGHT
    if row+1<=7 and col+2<=7:
        check_horse(row+1,col+2,element)
    if row-1>=0 and col+2<=7:
        check_horse(row-1,col+2,element)
        
    # LEFT
    if row+1<=7 and col-2>=0:
        check_horse(row+1,col-2,element)
    if row-1>=0 and col-2>=0:
        check_horse(row-1,col-2,element)
    
#  CAMEL CODE 
def camel(i,j,element):
    global flag
    # UP-RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row-1 >= 0 and col+1 <= 7:
            row-=1
            col+=1
            comon_coin(row,col,element)
        else:
            break
        
    # UP-LEFT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row-1 >= 0 and col-1 >= 0:
            row-=1
            col-=1
            comon_coin(row,col,element)
        else:
            break
        
    # DOWN-RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1 <= 7 and col+1 <= 7:
            row+=1
            col+=1
            comon_coin(row,col,element)
        else:
            break
        
    # DOWN-RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1 <= 7 and col-1 >= 0:
            row+=1
            col-=1
            comon_coin(row,col,element)
        else:
            break
   
#  CHECK KING COIN FUNCTION
def check_king(row,col,element):
    if element[0] in box[row][col]:
        pass
    else:
        print(f"{element} : {row} {col}")
        add_coin(row,col,element)
        checkmate_king(row,col,element)
    
#  KING CODE
def king(row,col,element):
    # UP
    if row-1>=0:
        check_king(row-1,col,element)
    # UP-RIGHT
    if row-1>=0 and col+1<=7:
        check_king(row-1,col+1,element)
    # RIGHT
    if col+1<=7:
        check_king(row,col+1,element)
    # DOWN-RIGHT
    if row+1<=7 and col+1<=7:
        check_king(row+1,col+1,element)
    # DOWN
    if row+1<=7:
        check_king(row+1,col,element)
    # DOWN-LEFT
    if row+1<=7 and col-1>=0:
        check_king(row+1,col-1,element)
    # LEFT
    if col-1>=0:
        check_king(row,col-1,element)
    # UP-LEFT
    if row-1>=0 and col-1>=0:
        check_king(row-1,col-1,element)
        
# QUEEN COIN FUNCTION
def queen(i,j,element):
    global flag
    # UP
    row = i
    col = j
    flag = True
    while(flag==True):
        if row-1 >= 0:
            row -= 1
            comon_coin(row,col,element)
        else:
            break
        
    # UP-RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row-1 >= 0 and col+1<=7:
            row -= 1
            col += 1
            comon_coin(row,col,element)
        else:
            break
        
    # RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if col+1<=7:
            col += 1
            comon_coin(row,col,element)
        else:
            break
        
    # DOWN-RIGHT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1 <= 7 and col+1<=7:
            row += 1
            col += 1
            comon_coin(row,col,element)
        else:
            break
        
    # DOWN
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1 <= 7:
            row += 1
            comon_coin(row,col,element)
        else:
            break
        
    # DOWN-LEFT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1 <= 7 and col-1>=0:
            row += 1
            col -= 1
            comon_coin(row,col,element)
        else:
            break
        
    # LEFT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row+1<= 7 and col-1>=0:
            row += 1
            col -= 1
            comon_coin(row,col,element)
        else:
            break
        
    # UP-LEFT
    row = i
    col = j
    flag = True
    while(flag==True):
        if row-1 >= 0 and col-1>=0:
            row -= 1
            col -= 1
            comon_coin(row,col,element)
        else:
            break
        
def check_swap(i,j,element):
    # Black
    if element[0] == "B":
        row = i
        col = j
        out = True
        if row == 7 and col == 3:
            for coll in range(col+1,7):
                if box[row][coll] != "___":
                    out = False
                    break
            if out == True:
                if box[row][7] == "BE2":
                    print("BK1_SWAP : Swap king And Elephant")
                    dict_position.update({"BK1_SWAP" : {"76":1,"75":1}})
                    
    # WHITE
    if element[0] == "W":
        row = i
        col = j
        out = True
        if row == 0 and col == 3:
            for coll in range(col-1,0,-1):
                if box[row][coll] != "___":
                    out = False
                    break
            if out == True:
                if box[row][0] == "WE1":
                    print("WK1_SWAP : Swap king And Elephant")
                    dict_position.update({"WK1_SWAP" : {"01":1,"02":1}})
    
def swap(element):
    if element[0] == "B":
        box[7][3] = "___"
        box[7][7] = "___"
        box[7][6] = "BK1"
        box[7][5] = "BE2"
        
    if element[0] == "W":
        box[0][3] = "___"
        box[0][0] = "___"
        box[0][1] = "WK1"
        box[0][2] = "WE1"
          
      
change = "B"
run = True
while(run):
    dict_position = {}
        
    print(f"\n --------- Now Turn {change} ----------")
    print("Choose Coin & Positions :")
    for i in range(0,8):
        for j in range(0,8):
            if change in box[i][j]:
                check_element(i,j,box[i][j])
                if "K" in box[i][j]:
                    check_swap(i,j,box[i][j])
                
    # print(dict_position)
                             
    user_coin = input("enter coin :")
    while(True):
        if "SWAP" in user_coin:
            user_position = list(dict_position[f"{user_coin}"].keys())
            break
        elif user_coin[0] == change:
            if len(dict_position[f"{user_coin}"]) == 1:
                user_position = int(list(dict_position[f"{user_coin}"].keys())[0])
                break
            else:
                user_position = int(input("enter position :"))
                break
        else:
            print("Wrong Coin Play Pleass Try Again and play correct Coin")
            user_coin = input("enter coin :")
        
    if "SWAP" in user_coin:
        swap(user_coin)
    else:
        b = user_position % 10
        user_position = int(user_position/ 10)
        a = user_position % 10
    
        temp = True
        for i in range(0,8):
            if temp == True:
                for j in range(0,8):
                    if user_coin == box[i][j]:
                        box[i][j] = "___"
                        if "K" in box[a][b]:
                            run = False
                        box[a][b] = user_coin
                        temp = False
                        break
            else:
                break
    # check the checkmate King or not
    check_element(a,b,user_coin)
    
            
    # Changing Coin
    if change == "W":
        change = "B"
    else:
        change = "W"
        
    # print box
    no = 0
    for i in range(8):
        print(f"   {i}",end="")
        
    print("")
    for row in box:
        print(no," ".join(row))
        no += 1
      
print("----------- GAME OVER ---------")