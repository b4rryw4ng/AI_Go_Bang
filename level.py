
class Node:
    def __init__(self, ID, dir1_cnt, dir2_cnt, dir3_cnt):
        self.ID = ID
        if dir1_cnt != 0:
            self.dir1 = True
            self.dir1_cnt = dir1_cnt
        else:
            self.dir1 = False
            self.dir1_cnt = 0
        if dir2_cnt != 0:
            self.dir2 = True
            self.dir2_cnt = dir2_cnt
        else:
            self.dir2 = False
            self.dir2_cnt = 0
        if dir3_cnt != 0:
            self.dir3 = True
            self.dir3_cnt = dir3_cnt
        else:
            self.dir3 = False
            self.dir3_cnt = 0

    def print_data(self):
        print(self.ID, self.dir1, self.dir1_cnt, self.dir2, self.dir2_cnt, self.dir3, self.dir3_cnt)

def check_valid_1(ID, node_list):
    flag = 0
    if ID == point0 or ID == point8 or ID == point100:
        flag = 1
    elif ID in boarder1 or ID in boarder2:
        flag = 1

    if flag:
        return -1

    level = get_level(ID)

    if ID > 116:
        wanted = ID - level -1
    else :
        wanted = ID - level

    for i in node_list:
        if wanted == i.ID:
            if i.dir1 == True:
                return i.dir1_cnt

    return -1

def check_valid_2(ID, node_list):
    flag = 0
    if ID == point0 or ID == point8 or ID == point116:
        flag = 1
    elif ID in boarder2 or ID in boarder3:
        flag = 1

    if flag:
        return -1

    level = get_level(ID)

    if ID > 116:
        wanted = ID - level
    else :
        wanted = ID - level + 1

    for i in node_list:
        if wanted == i.ID:
            if i.dir2 == True:
                return i.dir2_cnt

    return -1

def check_valid_3(ID, node_list):
    flag = 0
    if ID == point0 or ID == point100 or ID == point208:
        flag = 1
    elif ID in boarder1 or ID in boarder6:
        flag = 1

    if flag:
        return -1


    wanted = ID - 1
    

    for i in node_list:
        if wanted == i.ID:
            if i.dir1 == True:
                return i.dir1_cnt

    return -1

dir4_cnt = 0
def dir4_next_node(ID, op_list):
    global dir4_cnt 
    flag = 0

    if ID == point8 or ID == point116 or ID == point216:
        flag = 1
    elif ID in boarder3 or ID in boarder4:
        flag = 1
    
    if ID in op_list:
        dir4_cnt += 1
        
        if flag:
            return
        else:
            dir4_next_node(ID + 1, op_list)
    else :
        return

dir5_cnt = 0
def dir5_next_node(ID, op_list):
    global dir5_cnt 
    flag = 0
    level = get_level(ID)
    if ID == point100 or ID == point208 or ID == point216:
        flag = 1
    elif ID in boarder5 or ID in boarder6:
        flag = 1
    
    

    if ID in op_list:
        dir5_cnt += 1
        if flag:
            return
        elif ID >= 100:
            dir5_next_node(ID + level - 1, op_list)
        else:
            dir5_next_node(ID + level, op_list)
    else :
        return

dir6_cnt = 0
def dir6_next_node(ID, op_list):
    global dir6_cnt 
    flag = 0
    level = get_level(ID)
    if ID == point116 or ID == point208 or ID == point216:
        flag = 1
    elif ID in boarder4 or ID in boarder5:
        flag = 1
    if ID in op_list:
        dir6_cnt += 1
        if flag:
            return
        elif ID >= 100:
            dir6_next_node(ID + level , op_list)
        else:
            dir6_next_node(ID + level +1, op_list)
    else :
        return

def get_level(ID):
    if ID <= 8:
        return 9
    elif ID <= 18:
        return 10
    elif ID <= 29:
        return 11
    elif ID <= 41:
        return 12
    elif ID <= 54:
        return 13
    elif ID <= 68:
        return 14
    elif ID <= 83:
        return 15
    elif ID <= 99:
        return 16
    elif ID <= 116:
        return 17
    elif ID <= 132:
        return 16
    elif ID <= 147:
        return 15
    elif ID <= 161:
        return 14
    elif ID <= 174:
        return 13
    elif ID <= 186:
        return 12
    elif ID <= 197:
        return 11
    elif ID <= 216:
        return 10
        
point0 = 0 # without 1, 2, 3
boarder1 = [ 9, 19, 30, 42, 55, 69, 84 ] # without 1, 3
point8 = 8 # without 1, 2, 4
boarder2 = [ 1, 2, 3, 4, 5, 6, 7 ] # without 1, 2
point116 = 116 # without 2, 4, 6
boarder3 = [ 18, 29, 41, 54, 68, 83, 99 ] # without 2, 4
point216 = 216 # without 4, 5, 6
boarder4 = [ 132, 147, 161, 174, 186, 197, 207 ] # without 4, 6
point208 = 208 # without 3, 5, 6
boarder5 = [ 209, 210, 211, 212, 213, 214, 215 ] # without 5, 6
point100 = 100 # without 1, 3, 5
boarder6 = [ 117, 133, 148, 162,175, 187, 198 ] # without 3, 5
node_list = []
op_list = [0, 8, 100, 116, 208, 216]
# check if 1, 2, 3 direction has value 
# if not compute 4, 5, 6 direction respectively
for i in op_list:
    #check point 
    # dir1 dir1_cnt dir2 dir2_cnt dir3 dir3_cnt
    flag_dir1 = check_valid_1( i, node_list)
    flag_dir2 = check_valid_2( i, node_list)
    flag_dir3 = check_valid_3( i, node_list)
    if i == point0:
        dir4_next_node( i, op_list) #4
        dir5_next_node( i, op_list) #5
        dir6_next_node( i, op_list) #6
    elif i == point8:
        if flag_dir3 == -1: #check 3
            dir4_cnt = 1
        dir5_next_node( i, op_list) #5
        dir6_next_node( i, op_list) #6
    elif i == point100:
        if flag_dir2 == -1: #check 2
            dir5_cnt = 1
        dir4_next_node( i, op_list) #4
        dir6_next_node( i, op_list) #6
    elif i == point116:
        if check_valid_1( i, node_list) == -1: #check 1
            dir6_cnt = 1
        if flag_dir3 == -1: #check 3
            dir4_cnt = 1
        dir5_next_node( i, op_list) #5
    elif i == point208:
        if flag_dir1 == -1: #check 1
            dir6_cnt = 1
        if flag_dir2 == -1: #check 2
            dir5_cnt = 1
        dir4_next_node( i, op_list) #4
    elif i == point216:
        if flag_dir1 == -1: #check 1
            dir6_cnt = 1
        if flag_dir2 == -1: #check 2
            dir5_cnt = 1
        if flag_dir3 == -1: #check 3
            dir4_cnt = 1
    #check border
    elif i in boarder1: 
        if flag_dir2 == -1: #check 2
            dir5_next_node( i, op_list) #5
        else:
            dir5_cnt = flag_dir2

        dir4_next_node( i, op_list) #4
        dir6_next_node( i, op_list) #6
    elif i in boarder2:
        if flag_dir3 == -1: #check 3
            dir4_next_node( i, op_list) #4
        else:
            dir4_cnt
        dir5_next_node( i, op_list) #5
        dir6_next_node( i, op_list) #6
    elif i in boarder3: 
        if flag_dir1 == -1: #check 1
            dir6_next_node( i, op_list) #6
        else:
            dir6_cnt = flag_dir1
        if flag_dir3 == -1: #check 3
            dir4_cnt = 1

        dir5_next_node( i, op_list) #5
        
    elif i in boarder4: 
        if flag_dir1 == -1: #check 1
            dir6_cnt = 1
        if flag_dir2 == -1: #check 2
            dir5_next_node( i, op_list) #5
        else :
            dir5_cnt = flag_dir2
        if flag_dir3 == -1: #check 3
            dir4_cnt = 1
    elif i in boarder5:
        if flag_dir1 == -1: #check 1
            dir6_cnt = 1
        if flag_dir2 == -1: #check 2
            dir5_cnt = 1
        if flag_dir3 == -1: #check 3
            dir4_next_node( i, op_list) #4
        else:
            dir4_cnt = flag_dir3
    elif i in boarder6: 
        if flag_dir1 == -1: #check 1
            dir6_next_node( i, op_list) #6
        else : 
            dir6_cnt = flag_dir1
        if flag_dir2 == -1: #check 2
            dir5_cnt = 1
        dir4_next_node( i, op_list) #4
    #get level
    else:
        if flag_dir1 == -1: #check 1
            dir6_next_node( i, op_list) #6
        else:
            dir6_cnt = flag_dir1
        if flag_dir2 == -1: #check 2
            dir5_next_node( i, op_list) #5
        else:
            dir5_cnt = flag_dir2
        if flag_dir3 == -1: #check 3
            dir4_next_node( i, op_list) #4
        else:
            dir4_cnt = flag_dir3

    node_list.append(Node(i,dir6_cnt,dir5_cnt,dir4_cnt))
    dir4_cnt = 0
    dir5_cnt = 0
    dir6_cnt = 0

for i in node_list:
    i.print_data()