import time
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
   
def dead_or_alive_dir1(ID, node_list):
    wanted1 = -1
    wanted6 = -1    
    wanted1 = dir1_neighbor(ID) # if any neighbor exist    
    wanted6 = dir6_neighbor(ID)

    doa_dir1 = -1
    doa_dir6 = -1
    position = -1

    for i in node_list:
        if node.ID == wanted1:
            doa_dir1 = i.dir1_cnt
        if node.ID == wanted6:
            doa_dir6 = i.dir1_cnt
    
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
            doa_dir2 = i.dir2_cnt
        if node.ID == wanted5:
            doa_dir5 = i.dir2_cnt
    
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
            doa_dir3 = i.dir3_cnt
        if node.ID == wanted4:
            doa_dir4 = i.dir3_cnt
    
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

def evaluation_function(ID,my_list,op_list,new,pos,dir):## ID is node type, new is the new_length and pos is the position. dir means dir1 or dir2 or dir3
    total_list = my_list + op_list
    evaluation = 0
    if ID.dir1_cnt == 5 or ID.dir2_cnt == 5 or ID.dir3_cnt == 5:
        evaluation = 1000000
        return evaluation

    #dir_1
    if dir == 1:

        if new == 4:
            if pos == 1:
                num6 = 0
                num1 = 3
            elif pos == 2:
                num6 = 1
                num1 = 2
            elif pos == 3:
                num6 = 2
                num1 = 1
            elif pos == 4:
                num6 = 3
                num1 = 0

            temp = dir6_neighbor(ID.ID)
            for i in range(num6):
                temp = dir6_neighbor(temp)
                if temp in op_list:
                    evaluation = evaluation + 2000
                else:
                    temp = dir1_neighbor(ID)
                    for i in range(num1):
                        temp = dir1_neighbor(temp)
                    if temp in op_list:
                        evaluation = evaluation + 2000
                    else:
                        evaluation = evaluation + 6000

        elif new == 3:
            if pos == 1:
                num6 = 0
                num1 = 2
            elif pos == 2:
                num6 = 1
                num1 = 1
            elif pos == 3:
                num6 = 2
                num1 = 0


            temp = dir6_neighbor(ID.ID)
            for i in range(num6):
                temp = dir6_neighbor(temp)
            temp1 = dir1_neighbor(ID.ID)
            for i in range(num1):
                temp1 = dir1_neighbor(temp1)

            if temp in op_list and temp1 not in op_list:
                temp1 = dir1_neighbor(temp1)
                if temp1 in my_list:
                    evaluation = evaluation + 2000
                elif temp1 not in op_list:
                    evaluation = evaluation + 400
            elif temp not in op_list and temp1 in op_list:
                temp = dir6_neighbor(temp)
                if temp in my_list:
                    evaluation = evaluation + 2000
                elif temp not in op_list:
                    evaluation = evaluation + 400
            else:
                temp = dir6_neighbor(temp)
                temp1 = dir1_neighbor(temp)
                if temp in my_list and temp1 in my_list:
                    evaluation = evaluation + 4000
                if temp in my_list and temp1 not in my_list:
                    evaluation = evaluation + 2000
                if temp not in my_list and temp1 in my_list:
                    evaluation = evaluation + 2000
                else:
                    evaluation = evaluation + 1200

        elif new == 2:

            if pos == 1:
                num6 = 0
                num1 = 1
            elif pos == 2:
                num6 = 1
                num1 = 0

            temp = dir6_neighbor(ID.ID)
            for i in range(num6):
                temp = dir6_neighbor(temp)
            temp1 = dir1_neighbor(ID.ID)
            for i in range(num1):
                temp1 = dir1_neighbor(temp1)

            if temp in op_list and temp1 not in op_list:
                temp1 = dir1_neighbor(temp1)
                temp11 = dir1_neighbor(temp1)
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 2000
            elif temp not in op_list and temp1 in op_list:
                temp = dir6_neighbor(temp)
                temp_1 = dir6_neighbor(temp)
                if temp in my_list and temp_1 in my_list:
                    evaluation = evaluation + 2000
            else:
                temp = dir6_neighbor(temp)
                temp_1 = dir6_neighbor(temp)
                temp1 = dir1_neighbor(temp1)
                temp11 = dir1_neighbor(temp1)
                if temp in my_list and temp_1 in my_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 4000
                    elif temp1 in my_list and  temp11 not in total_list:
                        evaluation = evaluation + 3200
                    elif temp11 in my_list and  temp1 not in total_list:
                        evaluation = evaluation + 2400
                    elif temp1 not in total_list and temp11 not in total_list:
                        evaluation = evaluation + 2500
                elif temp in my_list and  temp_1 not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 3200
                elif temp_1 in my_list and  temp not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 2400
                elif temp not in total_list and  temp_1 not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 2500


    elif dir == 2:

        if new == 4:
            if pos == 1:
                num5 = 0
                num2 = 3
            elif pos == 2:
                num5 = 1
                num2 = 2
            elif pos == 3:
                num5 = 2
                num2 = 1
            elif pos == 4:
                num5 = 3
                num2 = 0

            temp = dir5_neighbor(ID.ID)
            for i in range(num5):
                temp = dir5_neighbor(temp)
                if temp in op_list:
                    evaluation = evaluation + 2000
                else:
                    temp = dir2_neighbor(ID.ID)
                    for i in range(num2):
                        temp = dir2_neighbor(temp)
                    if temp in op_list:
                        evaluation = evaluation + 2000
                    else:
                        evaluation = evaluation + 6000

        elif new == 3:
            if pos == 1:
                num5 = 0
                num2 = 2
            elif pos == 2:
                num5 = 1
                num2 = 1
            elif pos == 3:
                num5 = 2
                num2 = 0


            temp = dir5_neighbor(ID.ID)
            for i in range(num5):
                temp = dir5_neighbor(temp)
            temp1 = dir2_neighbor(ID.ID)
            for i in range(num2):
                temp1 = dir2_neighbor(temp1)

            if temp in op_list and temp1 not in op_list:
                temp1 = dir2_neighbor(temp1)
                if temp1 in my_list:
                    evaluation = evaluation + 2000
                elif temp1 not in op_list:
                    evaluation = evaluation + 400
            elif temp not in op_list and temp1 in op_list:
                temp = dir5_neighbor(temp)
                if temp in my_list:
                    evaluation = evaluation + 2000
                elif temp not in op_list:
                    evaluation = evaluation + 400
            else:
                temp = dir5_neighbor(temp)
                temp1 = dir2_neighbor(temp)
                if temp in my_list and temp1 in my_list:
                    evaluation = evaluation + 4000
                if temp in my_list and temp1 not in my_list:
                    evaluation = evaluation + 2000
                if temp not in my_list and temp1 in my_list:
                    evaluation = evaluation + 2000
                else:
                    evaluation = evaluation + 1200

        elif new == 2:

            if pos == 1:
                num5 = 0
                num2 = 1
            elif pos == 2:
                num5 = 1
                num2 = 0

            temp = dir5_neighbor(ID.ID)
            for i in range(num5):
                temp = dir6_neighbor(temp)
            temp1 = dir2_neighbor(ID.ID)
            for i in range(num2):
                temp1 = dir1_neighbor(temp1)

            if temp in op_list and temp1 not in op_list:
                temp1 = dir2_neighbor(temp1)
                temp11 = dir2_neighbor(temp1)
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 2000
            elif temp not in op_list and temp1 in op_list:
                temp = dir5_neighbor(temp)
                temp_1 = dir5_neighbor(temp)
                if temp in my_list and temp_1 in my_list:
                    evaluation = evaluation + 2000
            else:
                temp = dir5_neighbor(temp)
                temp_1 = dir5_neighbor(temp)
                temp1 = dir2_neighbor(temp1)
                temp11 = dir2_neighbor(temp1)
                if temp in my_list and temp_1 in my_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 4000
                    elif temp1 in my_list and  temp11 not in total_list:
                        evaluation = evaluation + 3200
                    elif temp11 in my_list and  temp1 not in total_list:
                        evaluation = evaluation + 2400
                    elif temp1 not in total_list and  temp11 not in total_list:
                        evaluation = evaluation + 2500
                elif temp in my_list and  temp_1 not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 3200
                elif temp_1 in my_list and  temp not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 2400
                elif temp not in total_list and  temp_1 not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 2500

    if dir == 3:

        if new == 4:
            if pos == 1:
                num4 = 0
                num3 = 3
            elif pos == 2:
                num4 = 1
                num3 = 2
            elif pos == 3:
                num4 = 2
                num3 = 1
            elif pos == 4:
                num4 = 3
                num3 = 0

            temp = dir4_neighbor(ID.ID)
            for i in range(num3):
                temp = dir4_neighbor(temp)
                if temp in op_list:
                    evaluation = evaluation + 2000
                else:
                    temp = dir3_neighbor(ID.ID)
                    for i in range(num3):
                        temp = dir3_neighbor(temp)
                    if temp in op_list:
                        evaluation = evaluation + 2000
                    else:
                        evaluation = evaluation + 6000

        elif new == 3:
            if pos == 1:
                num4 = 0
                num3 = 2
            elif pos == 2:
                num4 = 1
                num3 = 1
            elif pos == 3:
                num4 = 2
                num3 = 0


            temp = dir4_neighbor(ID.ID)
            for i in range(num4):
                temp = dir4_neighbor(temp)
            temp1 = dir3_neighbor(ID.ID)
            for i in range(num3):
                temp1 = dir3_neighbor(temp1)

            if temp in op_list and temp1 not in op_list:
                temp1 = dir3_neighbor(temp1)
                if temp1 in my_list:
                    evaluation = evaluation + 2000
                elif temp1 not in op_list:
                    evaluation = evaluation + 400
            elif temp not in op_list and temp1 in op_list:
                temp = dir4_neighbor(temp)
                if temp in my_list:
                    evaluation = evaluation + 2000
                elif temp not in op_list:
                    evaluation = evaluation + 400
            else:
                temp = dir4_neighbor(temp)
                temp1 = dir3_neighbor(temp)
                if temp in my_list and temp1 in my_list:
                    evaluation = evaluation + 4000
                if temp in my_list and temp1 not in my_list:
                    evaluation = evaluation + 2000
                if temp not in my_list and temp1 in my_list:
                    evaluation = evaluation + 2000
                else:
                    evaluation = evaluation + 1200

        elif new == 2:

            if pos == 1:
                num4 = 0
                num3 = 1
            elif pos == 2:
                num4 = 1
                num3 = 0

            temp = dir4_neighbor(ID.ID)
            for i in range(num4):
                temp = dir4_neighbor(temp)
            temp1 = dir3_neighbor(ID.ID)
            for i in range(num3):
                temp1 = dir3_neighbor(temp1)

            if temp in op_list and temp1 not in op_list:
                temp1 = dir3_neighbor(temp1)
                temp11 = dir3_neighbor(temp1)
                if temp1 in my_list and temp11 in my_list:
                    evaluation = evaluation + 2000
            elif temp not in op_list and temp1 in op_list:
                temp = dir4_neighbor(temp)
                temp_1 = dir4_neighbor(temp)
                if temp in my_list and temp_1 in my_list:
                    evaluation = evaluation + 2000
            else:
                temp = dir4_neighbor(temp)
                temp_1 = dir4_neighbor(temp)
                temp1 = dir3_neighbor(temp1)
                temp11 = dir3_neighbor(temp1)
                if temp in my_list and temp_1 in my_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 4000
                    elif temp1 in my_list and  temp11 not in total_list:
                        evaluation = evaluation + 3200
                    elif temp11 in my_list and  temp1 not in total_list:
                        evaluation = evaluation + 2400
                    elif temp1 not in total_list and  temp11 not in total_list:
                        evaluation = evaluation + 2500
                elif temp in my_list and  temp_1 not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 3200
                elif temp_1 in my_list and  temp not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 2400
                elif temp not in total_list and  temp_1 not in total_list:
                    if temp1 in my_list and temp11 in my_list:
                        evaluation = evaluation + 2500

    return evaluation
start = time.time()
rtlist=[]
op_list = [0,186]
my_list=[132, 161, 174]
total_list = my_list + op_list
print ("my_list: ", my_list)
print ("op_list: ", op_list)
#print ("total_list: ", total_list)
my_node = build_node(my_list)
move = 147
current_dir1_pos, dir1_case, current_dir2_pos, dir2_case, current_dir3_pos, dir3_case = dead_or_alive(move, my_node)
for index,i in enumerate(my_list):
    if i > move:
        my_list.insert(index,move)
        break

my_node = build_node(my_list)

evaluation_1 = 0
evaluation_2 = 0
evaluation_3 = 0

for node in my_node:
    if node.ID == move:
        #i.print_data()
        evaluation_1 = evaluation_function(node,my_list,op_list,dir1_case,current_dir1_pos,1)
        evaluation_2 = evaluation_function(node,my_list,op_list,dir2_case,current_dir2_pos,2)
        evaluation_3 = evaluation_function(node,my_list,op_list,dir3_case,current_dir3_pos,3)
        break

print (time.time() - start)

'''
for i in rtlist:
    i.print_data()
'''

print(evaluation_1, " ", evaluation_2, " ", evaluation_3)
