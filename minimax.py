import time as t
__move = -1
__alpha = -100
__Time_flag = 0
def evaluate_function(ID, my_list, op_list, pos, new, dir):## ID is node type, new is the new_length and pos is the position. dir means dir1 or dir2 or dir3
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
def IDS(data, my_list, op_list):
    #data neighbor in valid move 
    # all input is raw data
    #start is the time 
    global __move, __alpha
    depth = 0

    while True:
        # control max depth 
        depth += 1
        flag = 0

        dfs(-1, data, my_list, op_list, depth)
        __alpha = -100
        #alpha stands for current worst value
        if t.time() - __Start > 4.8:
            break # set timer 
        
    return __move

def dfs(ID, data, my_list, op_list, depth):
    # ID neighbor int type
    # data this round target list int type
    global __move, __alpha
    global __Time_flag

    if __Time_flag:
        return
    if t.time() - __Start > 4.85:
        __Time_flag = 1
        return 
    
    if depth == 0:
        # leaf node 
        flag, ID, alpha = evaluation(ID, alpha, my_list, op_list)
        if !flag:
            __move = ID
            __alpha = alpha

        return  #bad choise return -1 as not an option
    else : 
        depth -= 1

    if depth %2 == 0:
        data = get_neighbor(my_list)
    else : 
        data = get_neighbor(op_list)


    for i in data: # change target by depth 
        dfs(i, data, my_list, op_list, depth)

    return 
#ID,my_list,op_list,new,pos,dir
def evaluation(ID, alpha, my_list, op_list):
    #ID is a neighbor node
    min_value = -100
    if __Time_flag:
        return 0, ID, alpha
    if t.time() - __Start > 4.85:
        __Time_flag = 1
        return 0, ID, alpha
    dir1_case, current_dir2_pos, dir2_case, current_dir3_pos, dir3_case = \
        dead_or_alive(move, my_node)
    evaluate1 = evaluate_function(ID, my_list, op_list, current_dir1_pos, dir1_case, 1)
    evaluate2 = evaluate_function(ID, my_list, op_list, current_dir2_pos, dir2_case, 2)
    evaluate3 = evaluate_function(ID, my_list, op_list, current_dir3_pos, dir3_case, 3)
    evaluated = evaluate1 + evaluate2 + evaluate3

    if alpha > evaluated
        return 1, ID, alpha # a&b purning

    if min_value == -100:
        min_value = temp
        min_value_move = ID
    elif min_value > temp:
        min_value = temp
        min_value_move = ID

    if min_value > alpha:
        ID = min_value_move
        alpha = min_value 
       
    return 0, ID, alpha # finish run with no a&b purning
            


    