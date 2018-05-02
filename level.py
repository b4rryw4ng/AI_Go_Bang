# Global Value
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

    if ID <= 116:
        wanted = ID - level 
    else :
        wanted = ID - level -1

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

    if ID <= 116:
        wanted = ID - level + 1
    else :
        wanted = ID - level

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
            #print(i.ID)
            #i.print_data()
            if i.dir1 == True:
                return i.dir3_cnt

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
    elif ID <= 207:
        return 10
    elif ID <= 216:
        return 9
        



# check if 1, 2, 3 direction has value 
# if not compute 4, 5, 6 direction respectively
def build_node(op_list):
    global dir6_cnt, dir5_cnt, dir4_cnt
    node_list = []
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
            else : 
                dir4_cnt = flag_dir3
            dir5_next_node( i, op_list) #5
            dir6_next_node( i, op_list) #6
        elif i == point100:
            if flag_dir2 == -1: #check 2
                dir5_cnt = 1
            else: 
                dir5_cnt = flag_dir2
            dir4_next_node( i, op_list) #4
            dir6_next_node( i, op_list) #6
        elif i == point116:
            if check_valid_1( i, node_list) == -1: #check 1
                dir6_cnt = 1
            if flag_dir3 == -1: #check 3
                dir4_cnt = 1
            else :
                dir4_cnt = flag_dir3
            dir5_next_node( i, op_list) #5
        elif i == point208:
            if flag_dir1 == -1: #check 1
                dir6_cnt = 1
            else:
                dir6_cnt = flag_dir1
            if flag_dir2 == -1: #check 2
                dir5_cnt = 1
            else : 
                dir5_cnt = flag_dir2
            dir4_next_node( i, op_list) #4
        elif i == point216:
            if flag_dir1 == -1: #check 1
                dir6_cnt = 1
            else : 
                dir6_cnt = flag_dir1
            if flag_dir2 == -1: #check 2
                dir5_cnt = 1
            else : 
                dir5_cnt = flag_dir2
            if flag_dir3 == -1: #check 3
                dir4_cnt = 1
            else : 
                dir4_cnt = flag_dir3
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
                dir4_cnt = flag_dir3
            dir5_next_node( i, op_list) #5
            dir6_next_node( i, op_list) #6
        elif i in boarder3: 
            if flag_dir1 == -1: #check 1
                dir6_next_node( i, op_list) #6
            else:
                dir6_cnt = flag_dir1
            if flag_dir3 == -1: #check 3
                dir4_cnt = 1
            else :
                dir4_cnt = flag_dir3

            dir5_next_node( i, op_list) #5
            
        elif i in boarder4: 
            if flag_dir1 == -1: #check 1
                dir6_cnt = 1
            else :
                dir6_cnt = flag_dir1
            if flag_dir2 == -1: #check 2
                dir5_next_node( i, op_list) #5
            else :
                dir5_cnt = flag_dir2
            if flag_dir3 == -1: #check 3
                dir4_cnt = 1
            else :
                dir4_cnt = flag_dir3
        elif i in boarder5:
            if flag_dir1 == -1: #check 1
                dir6_cnt = 1
            else :
                dir6_cnt = flag_dir1
            if flag_dir2 == -1: #check 2
                dir5_cnt = 1
            else :
                dir5_cnt = flag_dir2
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
            else : 
                dir5_cnt = flag_dir2
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
    return node_list
def dir1_neighbor(ID):
    level = get_level(ID)

    if ID == point0 or ID == point8 or ID == point100:
        return -1
    elif ID in boarder1 or ID in boarder2:
        return -1

    if ID <= 116:
        wanted = ID - level 
    else :
        wanted = ID - level -1
    return wanted

def dir2_neighbor(ID):
    level = get_level(ID)

    if ID == point0 or ID == point8 or ID == point116:
        return -1
    elif ID in boarder2 or ID in boarder3:
        return -1

    if ID <= 116:
        wanted = ID - level + 1
    else :
        wanted = ID - level

    return wanted

def dir3_neighbor(ID):
    
    if ID == point0 or ID == point100 or ID == point208:
        return -1
    elif ID in boarder1 or ID in boarder6:
        return -1

   
    wanted = ID - 1
    
    return wanted


def dir4_neighbor(ID):
    if ID == point8 or ID == point116 or ID == point216:
        return -1
    elif ID in boarder3 or ID in boarder4:
        return -1
        
    wanted = ID + 1
    return wanted

def dir5_neighbor(ID):
    level = get_level(ID)

    if ID == point100 or ID == point208 or ID == point216:
        return -1
    elif ID in boarder5 or ID in boarder6:
        return -1

    if ID >= 100:
        wanted = ID + level - 1
    else : 
        wanted = ID + level

    return wanted


def dir6_neighbor(ID):
    level = get_level(ID)

    if ID == point116 or ID == point208 or ID == point216:
        return -1
    elif ID in boarder5 or ID in boarder4:
        return -1

    if ID >= 100:
        wanted = ID + level
    else :
        wanted = ID + level + 1

    return wanted

def check_neighbor(target_list): # my point 
    target = []
    #print (case, wanted_list)

    for i in target_list :
        a = -1
        b = -1
        c = -1
        d = -1
        e = -1
        f = -1

        a = dir1_neighbor(i)
        b = dir2_neighbor(i)
        c = dir3_neighbor(i)
        d = dir4_neighbor(i)
        e = dir5_neighbor(i)
        f = dir6_neighbor(i)

        print (i, a, b, c, d, e, f)
        if a != -1:
            if a not in target_list and a not in target:
                target.append(a)
        if b != -1:
            if b not in target_list and b not in target:
                target.append(b)
        if c != -1:
            if c not in target_list and c not in target:
                target.append(c) 
        if d != -1:
            if d not in target_list and d not in target:
                target.append(d) 
        if e != -1:
            if e not in target_list and e not in target:
                target.append(e) 
        if f != -1:
            if f not in target_list and f not in target:
                target.append(f)  

    return target 

def get_neighbor(op_list):
    # should check if the target is in valid or not
    # implant in dummy
    target = check_neighbor(op_list)
    #print()
    return target
"""    
def dead_or_alive_dir1(ID, node_list):
    flag1 = 0
    flag2 = 0
    if ID == point0 or ID == point8 or ID == point100:
        flag1 = 1
    elif ID in boarder1 or ID in boarder2:
        flag1 = 1

    if ID == point116 or ID == point208 or ID == point216:
        flag2 = 1
    elif ID in boarder4 or ID in boarder5:
        flag2 = 1

    wanted1 = -1
    wanted6 = -1
    
    if flag1 == 0:
        wanted1 = dir1_neighbor(ID) # if any neighbor exist 
    if flag2 == 0:
        wanted6 = dir6_neighbor(ID)

    doa_dir1 = -1
    doa_dir6 = -1
    position = -1

    for i in node_list:
        if i.ID = wanted1:
            doa_dir1 = i.dir1_cnt
        if i.ID = wanted6:
            doa_dir6 = i.dir1_cnt
    
    if doa_dir1 != -1 and doa_dir6 != -1:
        # yes yes 
        new_dir = doa_dir1 + doa_dir6
        position = doa_dir1 + 1
    elif doa_dir1 != -1 or doa_dir6 != -1:
        if doa_dir1 == -1:
            new_dir = doa_dir6 + 1
            position = 1
        else :
            position = doa_dir1 + 1 
            new_dir = doa_dir1 + 1
    else :
        position = 1
        new_dir = 1
    
    return position, new_dir


def dead_or_alive(ID, node_list):
    current_dir1_pos, dir1_case = dead_or_alive_dir1(ID, node_list) 
    # fuc (pos, case)   
    current_dir2_pos, dir1_case = dead_or_alive_dir2(ID, node_list)
    current_dir3_pos, dir1_case = dead_or_alive_dir3(ID, node_list)
"""
rtlist=[]
op_list = [48, 66, 75, 100, 116, 151, 195, 206]
my_list=[0, 8, 100, 116, 208, 216]
#total_list = my_list + op_list
print ("my_list: ", my_list)
print ("op_list: ", op_list)
#print ("total_list: ", total_list)
rtlist = get_neighbor(my_list)

''' 
for i in rtlist:
    i.print_data()
'''

print ("rtlist: ",rtlist)