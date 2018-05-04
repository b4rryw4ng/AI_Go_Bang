import time as t
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
__Time_limit = 1000
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
        print (self.ID, self.dir1, self.dir1_cnt, self.dir2, self.dir2_cnt, self.dir3, self.dir3_cnt)

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
            #print (i.ID)
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

        #print (i, a, b, c, d, e, f)
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

def get_neighbor(valid_list, target_list):
    # should check if the target is in valid or not
    # implant in dummy
    target = check_neighbor(target_list)
    data = []
    for i in target:
        if i in valid_list:
            data.append(i)
    data = sorted(data)
    #finish sorting
    return data
   
def dead_or_alive_dir1(ID, node_list):
    wanted1 = -1
    wanted6 = -1    
    wanted1 = dir1_neighbor(ID) # if any neighbor exist    
    wanted6 = dir6_neighbor(ID)

    doa_dir1 = -1
    doa_dir6 = -1
    position = -1

    for node in node_list:
        if node.ID == wanted1:
            doa_dir1 = node.dir1_cnt
        if node.ID == wanted6:
            doa_dir6 = node.dir1_cnt
    
    if doa_dir1 != -1 and doa_dir6 != -1:
        # yes yes 
        new_len = doa_dir1 + doa_dir6 + 1
        position = doa_dir1 + 1
    elif doa_dir1 != -1 or doa_dir6 != -1:
        if doa_dir1 == -1:
            new_len = doa_dir6 + 1
            position = 1
        else :
            position = doa_dir1 + 1 
            new_len = doa_dir1 + 1
    else :
        position = 1
        new_len = 1
    
    return position, new_len

def dead_or_alive_dir2(ID, node_list):
    wanted2 = -1
    wanted5 = -1    
    wanted2 = dir2_neighbor(ID) # if any neighbor exist    
    wanted5 = dir5_neighbor(ID)

    doa_dir2 = -1
    doa_dir5 = -1
    position = -1

    for node in node_list:
        if node.ID == wanted2:
            doa_dir2 = node.dir2_cnt
        if node.ID == wanted5:
            doa_dir5 = node.dir2_cnt
    
    if doa_dir2 != -1 and doa_dir5 != -1:
        # yes yes 
        new_len = doa_dir2 + doa_dir5 + 1
        position = doa_dir2 + 1
    elif doa_dir2 != -1 or doa_dir5 != -1:
        if doa_dir2 == -1:
            new_len = doa_dir5 + 1
            position = 1
        else :
            position = doa_dir2 + 1 
            new_len = doa_dir2 + 1
    else :
        position = 1
        new_len = 1
    
    return position, new_len

def dead_or_alive_dir3(ID, node_list):
    wanted3 = -1
    wanted4 = -1    
    wanted3 = dir3_neighbor(ID) # if any neighbor exist    
    wanted4 = dir4_neighbor(ID)

    doa_dir3 = -1
    doa_dir4 = -1
    position = -1

    for node in node_list:
        if node.ID == wanted3:
            doa_dir3 = node.dir3_cnt
        if node.ID == wanted4:
            doa_dir4 = node.dir3_cnt
    
    if doa_dir3 != -1 and doa_dir4 != -1:
        # yes yes 
        new_len = doa_dir3 + doa_dir4 + 1
        position = doa_dir3 + 1
    elif doa_dir3 != -1 or doa_dir4 != -1:
        if doa_dir3 == -1:
            new_len = doa_dir4 + 1
            position = 1
        else :
            position = doa_dir3 + 1 
            new_len = doa_dir3 + 1
    else :
        position = 1
        new_len = 1
    
    return position, new_len

def dead_or_alive(ID, node_list):
    current_dir1_pos, dir1_case = dead_or_alive_dir1(ID, node_list)   
    current_dir2_pos, dir2_case = dead_or_alive_dir2(ID, node_list)
    current_dir3_pos, dir3_case = dead_or_alive_dir3(ID, node_list)
    return current_dir1_pos, dir1_case, current_dir2_pos, dir2_case, current_dir3_pos, dir3_case

def evaluate_function(ID, my_list, op_list, pos, new, dir):## ID is node type, new is the new_length and pos is the position. dir means dir1 or dir2 or dir3
    total_list = my_list + op_list

    evaluation = 0
    if dir == 1:
        if ID.dir1_cnt == 5:
            evaluation = 1000000
            return evaluation
    elif dir == 2:
        if ID.dir2_cnt == 5:
            evaluation = 1000000
            return evaluation
    elif dir == 3:
        if ID.dir3_cnt == 5:
            evaluation = 1000000
            return evaluation


    if new == 4:
        if pos == 1:
                num6 = 3
                num1 = 0
                num5 = 3
                num2 = 0
                num4 = 3
                num3 = 0
        elif pos == 2:
                num6 = 2
                num1 = 1
                num5 = 2
                num2 = 1
                num4 = 2
                num3 = 1
        elif pos == 3:
                num6 = 1
                num1 = 2
                num5 = 1
                num2 = 2
                num4 = 1
                num3 = 2
        elif pos == 4:
                num6 = 0
                num1 = 3
                num5 = 0
                num2 = 3
                num4 = 0
                num3 = 3

        if dir == 1:
            temp = dir6_neighbor(ID.ID)
            for i in range(num6):
                temp = dir6_neighbor(temp)
            temp1 = dir1_neighbor(ID.ID)
            for i in range(num1):
                temp1 = dir1_neighbor(temp1)
        elif dir == 2:
            temp = dir5_neighbor(ID.ID)
            for i in range(num5):
                temp = dir5_neighbor(temp)
            temp1 = dir2_neighbor(ID.ID)
            for i in range(num2):
                temp1 = dir2_neighbor(temp1)
        elif dir == 3:
            temp = dir4_neighbor(ID.ID)
            for i in range(num4):
                temp = dir4_neighbor(temp)
            temp1 = dir3_neighbor(ID.ID)
            for i in range(num3):
                temp1 = dir3_neighbor(temp1)

        if (temp in op_list or temp == -1) and temp1 not in op_list and temp1 != -1:
            evaluation = evaluation + 2000
        elif (temp1 in op_list or temp1 == -1) and temp not in op_list and temp != -1:
            evaluation = evaluation + 2000
        if temp not in op_list and temp != -1 and temp1 not in op_list and temp1 != -1:
            evaluation = evaluation + 6000

    elif new == 3:
        if pos == 1:
                num6 = 2
                num1 = 0
                num5 = 2
                num2 = 0
                num4 = 2
                num3 = 0
        elif pos == 2:
                num6 = 1
                num1 = 1
                num5 = 1
                num2 = 1
                num4 = 1
                num3 = 1
        elif pos == 3:
                num6 = 0
                num1 = 2
                num5 = 0
                num2 = 2
                num4 = 0
                num3 = 2
        if dir == 1:
            temp = dir6_neighbor(ID.ID)
            for i in range(num6):
                temp = dir6_neighbor(temp)
            temp1 = dir1_neighbor(ID.ID)
            for i in range(num1):
                temp1 = dir1_neighbor(temp1)
        elif dir == 2:
            temp = dir5_neighbor(ID.ID)
            for i in range(num5):
                temp = dir5_neighbor(temp)
            temp1 = dir2_neighbor(ID.ID)
            for i in range(num2):
                temp1 = dir2_neighbor(temp1)
        elif dir == 3:
            temp = dir4_neighbor(ID.ID)
            for i in range(num4):
                temp = dir4_neighbor(temp)
            temp1 = dir3_neighbor(ID.ID)
            for i in range(num3):
                temp1 = dir3_neighbor(temp1)

        if (temp in op_list or temp == -1) and temp1 not in op_list and temp1 != -1:
            if dir == 1:
                temp1 = dir1_neighbor(temp1)
            if dir == 2:
                temp1 = dir2_neighbor(temp1)
            if dir == 3:
                temp1 = dir3_neighbor(temp1)
            if temp1 in my_list:
                evaluation = evaluation + 2000
            elif temp1 not in op_list and temp1 != -1:
                evaluation = evaluation + 400
        elif temp not in op_list and temp != -1 and (temp1 in op_list or temp1 == -1):
            if dir == 1:
                temp = dir6_neighbor(temp)
            if dir == 2:
                temp = dir5_neighbor(temp)
            if dir == 3:
                temp = dir4_neighbor(temp)
            if temp in my_list:
                evaluation = evaluation + 2000
            elif temp not in op_list and temp != -1:
                evaluation = evaluation + 400
        elif temp not in op_list and temp != -1 and temp1 not in op_list and temp1 != -1:
            if dir == 1:
                temp = dir6_neighbor(temp)
                temp1 = dir1_neighbor(temp1)
            if dir == 2:
                temp = dir5_neighbor(temp)
                temp1 = dir2_neighbor(temp1)
            if dir == 3:
                temp = dir4_neighbor(temp)
                temp1 = dir3_neighbor(temp1)
            if temp in my_list and temp1 in my_list:
                evaluation = evaluation + 4000
            elif temp in my_list:
                evaluation = evaluation + 2000
            elif temp1 in my_list:
                evaluation = evaluation + 2000
            elif temp not in op_list and temp != -1 and temp1 not in op_list and temp1 != -1:
                evaluation = evaluation + 1200

    elif new == 2:

        if pos == 1:
                num6 = 1
                num1 = 0
                num5 = 1
                num2 = 0
                num4 = 1
                num3 = 0
        elif pos == 2:
                num6 = 0
                num1 = 1
                num5 = 0
                num2 = 1
                num4 = 0
                num3 = 1

        if dir == 1:
            temp = dir6_neighbor(ID.ID)
            for i in range(num6):
                temp = dir6_neighbor(temp)
            temp1 = dir1_neighbor(ID.ID)
            for i in range(num1):
                temp1 = dir1_neighbor(temp1)
        elif dir == 2:
            temp = dir5_neighbor(ID.ID)
            for i in range(num5):
                temp = dir5_neighbor(temp)
            temp1 = dir2_neighbor(ID.ID)
            for i in range(num2):
                temp1 = dir2_neighbor(temp1)
        elif dir == 3:
            temp = dir4_neighbor(ID.ID)
            for i in range(num4):
                temp = dir4_neighbor(temp)
            temp1 = dir3_neighbor(ID.ID)
            for i in range(num3):
                temp1 = dir3_neighbor(temp1)
        if (temp in op_list or temp == -1) and temp1 not in op_list and temp1 != -1:
            if dir == 1:
                temp1 = dir1_neighbor(temp1)
                temp11 = dir1_neighbor(temp1)
            elif dir == 2:
                temp1 = dir2_neighbor(temp1)
                temp11 = dir2_neighbor(temp1)
            elif dir == 3:
                temp1 = dir3_neighbor(temp1)
                temp11 = dir3_neighbor(temp1)
            if temp1 in my_list and temp11 in my_list:
                evaluation = evaluation + 2000
        elif temp not in op_list and temp != -1 and (temp1 in op_list or temp1 == -1):
            if dir == 1:
                temp = dir6_neighbor(temp)
                temp_1 = dir6_neighbor(temp)
            elif dir == 2:
                temp = dir5_neighbor(temp)
                temp_1 = dir5_neighbor(temp)
            elif dir == 3:
                temp = dir4_neighbor(temp)
                temp_1 = dir4_neighbor(temp)
            if temp in my_list and temp_1 in my_list:
                evaluation = evaluation + 2000
        elif temp not in op_list and temp != -1 and temp1 not in op_list and temp1 != -1:
            if dir == 1:
                temp = dir6_neighbor(temp)
                temp_1 = dir6_neighbor(temp)
                temp1 = dir1_neighbor(temp1)
                temp11 = dir1_neighbor(temp1)
            elif dir == 2:
                temp = dir5_neighbor(temp)
                temp_1 = dir5_neighbor(temp)
                temp1 = dir2_neighbor(temp1)
                temp11 = dir2_neighbor(temp1)
            elif dir == 3:
                temp = dir4_neighbor(temp)
                temp_1 = dir4_neighbor(temp)
                temp1 = dir3_neighbor(temp1)
                temp11 = dir3_neighbor(temp1)
            if temp in my_list and temp_1 in my_list:
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 4000
                elif temp1 in my_list and  temp11 not in op_list and temp11 != -1:
                    evaluation = evaluation + 3200
                elif temp11 in my_list and  temp1 not in op_list and temp1 != -1:
                    evaluation = evaluation + 2400
                elif temp1 not in op_list and temp1 != -1 and temp11 not in op_list and temp11 != -1:
                    evaluation = evaluation + 2500
            elif temp in my_list and  temp_1 not in op_list and temp_1 != -1:
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 3200
            elif temp_1 in my_list and  temp not in op_list and temp != -1:
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 2400
            elif temp not in op_list and  temp != -1 and temp_1 not in op_list and temp_1 != -1:
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 2500

    elif new == 1:
        count = 0
        count_1 = 0
        count4 = 0
        count_4 = 0
        count_44 = 0
        for i in range(4):
            if i == 0:
                if dir == 1:
                    temp = dir6_neighbor(ID.ID)
                elif dir == 2:
                    temp = dir5_neighbor(ID.ID)
                elif dir == 3:
                    temp = dir4_neighbor(ID.ID)
            else:
                if dir == 1:
                    temp = dir6_neighbor(temp)
                elif dir == 2:
                    temp = dir5_neighbor(temp)
                elif dir == 3:
                    temp = dir4_neighbor(temp)
            if temp in op_list:
                count = count + 1
            elif temp in my_list or temp == -1:
                break
        for i in range(4):
            if i == 0:
                if dir == 1:
                    temp_1 = dir1_neighbor(ID.ID)
                elif dir == 2:
                    temp_1 = dir2_neighbor(ID.ID)
                elif dir == 3:
                    temp_1 = dir3_neighbor(ID.ID)
            else:
                if dir == 1:
                    temp_1 = dir1_neighbor(temp_1)
                elif dir == 2:
                    temp_1 = dir2_neighbor(temp_1)
                elif dir == 3:
                    temp_1 = dir3_neighbor(temp_1)
            if temp_1 in op_list:
                count_1 = count_1 + 1
            elif temp_1 in my_list or temp_1 == -1:
                break
        for i in range(4):
            if i == 0:
                if dir == 1:
                    temp = dir6_neighbor(ID.ID)
                elif dir == 2:
                    temp = dir5_neighbor(ID.ID)
                elif dir == 3:
                    temp = dir4_neighbor(ID.ID)
            else:
                if dir == 1:
                    temp = dir6_neighbor(temp)
                elif dir == 2:
                    temp = dir5_neighbor(temp)
                elif dir == 3:
                    temp = dir4_neighbor(temp)
            if temp in op_list:
                count4 = count4 + 1
            elif temp in my_list or temp not in total_list or temp == -1:
                break
        for i in range(4):
            if i == 0:
                if dir == 1:
                    temp_1 = dir1_neighbor(ID.ID)
                elif dir == 2:
                    temp_1 = dir2_neighbor(ID.ID)
                elif dir == 3:
                    temp_1 = dir3_neighbor(ID.ID)
            else:
                if dir == 1:
                    temp_1 = dir1_neighbor(temp_1)
                elif dir == 2:
                    temp_1 = dir2_neighbor(temp_1)
                elif dir == 3:
                    temp_1 = dir3_neighbor(temp_1)
            if temp_1 in op_list:
                count_4 = count_4 + 1
            elif temp_1 in my_list or temp_1 not in total_list or temp_1 == -1:
                break

        if count == 3:
            evaluation = evaluation + 2400
        if count_1 == 3:
            evaluation = evaluation + 2400
        count_44 = count4 + count_4
        if count_44 >= 4 and count_44 < 8:
            evaluation = evaluation + 15000
        elif count_44 == 8:
            evaluation = evaluation + 30000

    return evaluation

def get_neighbor_dfs(valid_list, target_list, ID):
    target = check_neighbor(target_list)
    data = []
    for i in target:
        if i in valid_list and i != ID:
            data.append(i)
    data = sorted(data)
    #finish sorting
    return data    
start = t.time()
rtlist=[]
#my_list = []
#op_list = []
op_list = [99,132, 161, 174]
my_list= [115,184,185,197,207]
v_list = []
for i in range(217):
    if i not in op_list and i not in my_list:
        v_list.append(i)

my_neighbor = get_neighbor(v_list, my_list)
total_list = my_list + op_list
#print ("my_list: ", my_list)
#print ("op_list: ", op_list)

__Start = t.time()
__move = -1
__alpha = -100
__Time_flag = 0
__MAX_depth = 0
__Win = 0
__Win_move = -1
def IDS(my_list, op_list, valid_list):
    #data neighbor in valid move 
    # all input is raw data
    #start is the time 
    global __move, __alpha, __new_alpha, __Win, __Win_move
    global __Start, __MAX_depth
    depth = 0
    move = []
    while True:
        #print ("in while")
        # control max depth 
        __MAX_depth += 1
        #print ("__MAX_depth : ",__MAX_depth)

        data = []
        
        dfs(-1, -1, -1, data, my_list, op_list, valid_list, 0)
        #print ("in IDS return __move : ",__move)
        move.append(__move)
        if __Win == 1 and __MAX_depth == 1:
            break

        __alpha = -100
        __move = -1
        __Win = 0
        if t.time() - __Start > __Time_limit:
            #__Time_flag = 1
            #print (t.time() - __Start)
            break # set timer
        if __MAX_depth == 3 :
            break
    #print (__MAX_depth, __Time_flag)
    #print (move)

    if __Win :
        return move[0]
    if __Time_flag:
        __MAX_depth -=1
    
    turn = __MAX_depth % 2 
    if turn ==1 and __Time_flag == 1:
        return move[-2]
    elif turn == 0 and __Time_flag == 1:
        return move[-3]
    elif turn == 1 and __Time_flag == 0:
        return move[-1]
    else :
        return move[-2]
    
x = 0
def dfs(Index, ID, first_move, data, my_list, op_list, valid_list, depth):
    global x
    x += 1
    # Index which DFS node
    # ID current op move
    # first_move the appropriate move
    global __MAX_depth, __Win
    global __move, __alpha, __new_alpha 
    global __Time_flag
    if __Time_flag or __Win:
        return 
    if t.time() - __Start > __Time_limit:
        __Time_flag = 1
        return 

    if depth == __MAX_depth:
        #print (data)
        if __MAX_depth == 1:
                flag, alpha = evaluation_function_first_level(first_move,data, my_list, op_list)
                # data current this position 
                if flag == 0:
                    __alpha = alpha
                    __move = first_move
                    #print (__move,__alpha)
                    if __alpha == 1000000:
                        __Win = 1
        else : 
            if Index == 0:
                alpha = evaluation_function_full(first_move,data, my_list, op_list)
                # data current this position 
                __alpha = alpha
                __move = first_move
                #print (__move,__alpha)
                if __alpha == 1000000:
                    __Win = 1
                #print (__alpha)
            else :
                flag, alpha = evaluation_function_a_B(first_move, data, my_list, op_list)
                if flag == 0:
                    __alpha = alpha
                    __move = first_move
                    #print (__move,__alpha)
                    if __alpha == 1000000:
                        __Win = 1
            
        # print ("__move", __move, "alpha ",__alpha)
        return
    else :
        depth += 1
    
    temp_op_list = op_list.copy()
    temp_my_list = my_list.copy()
    #total = op_list.copy() + my_list.copy()
    #total = sorted (total)
    #print ("total : ", total)
    if depth %2 == 0 :
        # if len my > op 0 is my turn
        # my turn 
        # update op
        # find my neighbor
        if ID != -1:    
            for index, i in enumerate(op_list):
                if i > ID and ID != -1:          
                    temp_op_list.insert(index, ID)
                    #print ("add ID ", ID, " in temp_op_list ", temp_op_list )
                    break
        total = sorted( my_list + temp_op_list)
        data = get_neighbor_dfs(valid_list, total, ID)
        #print ("my_list data:", data)
    
    else:
        # op turn 
        #update op
        #find my neighbor
        if ID != -1:
            for index, i in enumerate(my_list):
                if i > ID:          
                    temp_my_list.insert(index, ID)
                    #print ("add ID ", ID, " in temp_my_list ", temp_my_list )
                    break
        total = sorted(temp_my_list + op_list)
        data = get_neighbor_dfs(valid_list, total, ID)
        #print ("op_list data:", data)

    #print ("case : ",depth %2)
    if depth %2 == 1:
        # my turn
        for index, i in enumerate(data):
            
            if depth == 1:
                first_move = i
                #print ("first_move:", first_move)

            #print ("current index :" , index, "value : ", i, "depth :", depth)
            dfs(index, i, first_move, data, op_list, temp_my_list, valid_list, depth)
    else :
        for index, i in enumerate(data):
            
            if depth == 1:
                first_move = i
                #print ("first_move:", first_move)
            #print ("current index :" , index, "value : ", i, "depth :", depth)
            dfs(index, i, first_move, data, my_list, temp_op_list, valid_list, depth)

    return
def evaluation_function_first_level(first_move, data, my_list, op_list):
    global __Time_flag, __alpha, __Win
    max_value = -100
    alpha = __alpha
    #print ("first_level evaluation")
    
    if __Time_flag:
        return max_value 
        # 1 dead-end 
    if t.time() - __Start > __Time_limit:
        __Time_flag = 1
        return max_value 

    data_node = build_node(my_list)
    #print ("in evaluation full data ", data)
    #print ("in evaluation full my_list ", my_list)
    

    temp_my_list = my_list.copy()
    for index, i in enumerate(temp_my_list):
        if i > first_move :
            temp_my_list.insert(index, first_move)
            break
        
    current_dir1_pos, dir1_case, current_dir2_pos, dir2_case, current_dir3_pos, dir3_case = \
        dead_or_alive(first_move, data_node)

    data_node = build_node(temp_my_list)
    temp = data_node[0] #initialize

    for i in data_node:
        if i.ID == first_move:
            temp = i
            break
    #temp.print_data()
    # temp is current node 

    evaluate1 = evaluate_function(temp, my_list, op_list, current_dir1_pos, dir1_case, 1)
    evaluate2 = evaluate_function(temp, my_list, op_list, current_dir2_pos, dir2_case, 2)
    evaluate3 = evaluate_function(temp, my_list, op_list, current_dir3_pos, dir3_case, 3)
    evaluated = evaluate1 + evaluate2 + evaluate3
    #evaluated = 100
    if evaluated == 1000000:
        #print (first_move, temp.ID, my_list, evaluated)
        __Win = 1
        return 0, evaluated
    if max_value == -100 or max_value == 0 : 
    #if max_value == -100 : 
        max_value = evaluated

    #print ("max_value : ",evaluated)
    if max_value < evaluated:
        max_value = evaluated
    
    if max_value == 0:
        max_value = 10
    if alpha < max_value:
        alpha = max_value
        return 0, alpha
    return 1, alpha
    # 1 set up new alpha 
def evaluation_function_full(first_move, data, my_list, op_list):
    global __Time_flag
    max_value = -100
    #print ("index 1 evaluation fucntion")
    
    if __Time_flag:
        return max_value 
        # 1 dead-end 
    if t.time() - __Start > __Time_limit:
        __Time_flag = 1
        return max_value 

    data_node = build_node(my_list)
    #print ("in evaluation full data ", data)
    #print ("in evaluation full my_list ", my_list)
    
    for ID in data:
        temp_my_list = my_list.copy()
        for index, i in enumerate(temp_my_list):
            if i > ID :
                temp_my_list.insert(index, ID)
                break
            
        current_dir1_pos, dir1_case, current_dir2_pos, dir2_case, current_dir3_pos, dir3_case = \
            dead_or_alive(ID, data_node)

        data_node = build_node(temp_my_list)
        temp = data_node[0] #initialize

        for i in data_node:
            if i.ID == ID:
                temp = i
                break
        #temp.print_data()
        # temp is current node 

        evaluate1 = evaluate_function(temp, my_list, op_list, current_dir1_pos, dir1_case, 1)
        evaluate2 = evaluate_function(temp, my_list, op_list, current_dir2_pos, dir2_case, 2)
        evaluate3 = evaluate_function(temp, my_list, op_list, current_dir3_pos, dir3_case, 3)
        evaluated = evaluate1 + evaluate2 + evaluate3
        #evaluated = 100
        if evaluated == 1000000:

            #print (first_move, temp.ID, my_list, evaluated)
            return evaluated
        if max_value == -100 or max_value == 0 : 
        #if max_value == -100 : 
            max_value = evaluated

        #print ("max_value : ",evaluated)
        if max_value < evaluated:
            max_value = evaluated
        
    if max_value == 0:
        max_value = 10
    return max_value
    # 1 set up new alpha 
#[83, 98, 114, 116, 131, 146, 147, 160, 171, 172, 173, 183, 186, 195, 196, 206, 216]
def evaluation_function_a_B(first_move, data, my_list, op_list):
    #print ("evaluation fucntion a B")
    global __Time_flag
    alpha = __alpha
    if __Time_flag:
        return 1, alpha 
        # 1 dead-end 
    if t.time() - __Start > __Time_limit:
        __Time_flag = 1
        return 1, alpha 
    
    data_node = build_node(my_list)

    max_value = -100
    min_move = -1
    #print ("in evaluation a_B data ", data)
    #print ("in evaluation a_B my_list ", my_list)
    for ID in data:
        temp_my_list = my_list.copy()
        for index, i in enumerate(temp_my_list):
            if i > ID :
                temp_my_list.insert(index, ID)
                break
            
        current_dir1_pos, dir1_case, current_dir2_pos, dir2_case, current_dir3_pos, dir3_case = \
            dead_or_alive(ID, data_node)

        data_node = build_node(temp_my_list)
        temp = data_node[0] #initialize

        for i in data_node:
            if i.ID == ID:
                temp = i
                break
        #temp.print_data()
        # temp is current node 

        evaluate1 = evaluate_function(temp, my_list, op_list, current_dir1_pos, dir1_case, 1)
        evaluate2 = evaluate_function(temp, my_list, op_list, current_dir2_pos, dir2_case, 2)
        evaluate3 = evaluate_function(temp, my_list, op_list, current_dir3_pos, dir3_case, 3)
        
        evaluated = evaluate1 + evaluate2 + evaluate3
        #evaluated = 100
        if evaluated == 1000000:
            #print (first_move, temp.ID, my_list, evaluated)
            return 0, evaluated
            
        if max_value == -100 or max_value == 0: 
        #if max_value == -100: 
            max_value = evaluated
        

        if max_value < evaluated:
            max_value = evaluated
        
        if alpha < max_value and evaluated != 0:
        #if alpha > max_value :    
            #print ("got purning ", max_value)
            return 1, alpha
    
    if alpha < max_value:
        return 0, max_value
    # after all iteration, the min value is larger than current alpha, update alpha    
    #print ("finish but no max_value", max_value)
    return 1, alpha
#print ("IDS")

if len(my_list) == 0 and len(op_list) == 0 :
    h = 108
else : 
    h = IDS(my_list, op_list, v_list)
print (t.time() - __Start)
print (h)
print (x)