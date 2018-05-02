def IDS(data, my_list, op_list): #data neighbor in valid move 
    evaluate_neighbor(data) #recalculate the sequence for the data
    depth = 0

    while True:
        # control max depth 
        depth += 1
        flag = 0

        dfs( data, my_list, op_list, alpha, beta, depth)
        

        #alpha stands for current worst value
        # beta stands for current best next move position
    pass
__move = 0
__alpha = -100
def dfs( data, my_list, op_list, depth):
    global next_move, 
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
        else if min_value > temp:
            min_value = temp
            min_value_move = ID

    if min_value > alpha:
        ID = min_value_move
        alpha = min_value 
       
    return 0, ID, alpha # finish run with no a&b purning
            


    