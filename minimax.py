import time as t
__move = 0
__alpha = -100

def IDS(start,data, my_list, op_list):
    #data neighbor in valid move 
    # all input is raw data
    #start is the time 
    global __move, __alpha
    depth = 0

    while True:
        # control max depth 
        depth += 1
        flag = 0

        dfs( data, my_list, op_list, depth)
        __alpha = -100
        
        if t.time() - start > 4.8:
            break
        #alpha stands for current worst value
    return __move

def dfs( data, my_list, op_list, depth):
    global __move, __alpha

    if depth == 0:
        # leaf node 
        flag, ID, alpha = evaluate(data, alpha)
        if !flag:
            __move = ID
            __alpha = alpha

        return  #bad choise return -1 as not an option
    else : 
        depth -= 1

    dfs( data, my_list, op_list, depth)

    return 
        
def evaluate(data, alpha):
    min_value = -100
    for ID in data :
        temp = evaluate_function(ID)

        if alpha > evaluated
            return 1, ID, 0, alpha # a&b purning

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
            


    