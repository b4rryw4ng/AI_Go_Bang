def minimax(data, my_list, op_list):
    evaluate_neighbor(data) #recalculate the sequence for the data
    depth = 0
    alpha = -100
    while True:
        depth += 1
        expand_node(data, my_list, op_list, alpha, beta, depth)
    pass

def expand_node(data, my_list, op_list, alpha, beta, depth):
    if depth == 0:
        return
    else : 
        depth -= 1

    evaluate = evaluate_function(data)
    if alpha == -100:
        alpha = evaluate
    elif evaluate > alpha
    