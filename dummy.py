# This is a dummy AI example to help you doing program assignment 2.
# We implemented the file I/O part. 
# You may focus on the method, _get_next_move(), 
# which is a method to decide where to place your stone based on the current game state,
# including (1) valid position, (2) your position, (3) your opponent position, 
# (4) board and (5) the winner of first game.

# !! Remember to change the team number in main() !!
import os
from random import randint
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
dir4_cnt = 0
dir5_cnt = 0
dir6_cnt = 0

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
        return 16
    elif ID <= 132:
        return 15
    elif ID <= 147:
        return 14
    elif ID <= 161:
        return 13
    elif ID <= 174:
        return 12
    elif ID <= 186:
        return 11
    elif ID <= 197:
        return 10
    elif ID <= 216:
        return 9   

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

def build_node(oplist):
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
    return node_list

class Agent:
    """
    Game agent.
    The procedure:
        1. process_state_info: check game state
        2. is_my_turn: if it is my turn, decide a position to put stone
        3. step: call get_next_move and write the result to move file
    """
    def __init__(self, team_number):
        self.team_number = team_number
        self.stat_file = "state_" + str(team_number) + ".txt"
        self.move_file = "move_" + str(team_number) + ".txt"

        self.cur_move = -1
        self.next_first_move = -1
        self.first_winner = -1
        self.game_stop = False

        self.valid_pos = []
        self.my_pos = []
        self.opponent_pos = []
    
    def process_state_info(self):
        """
        Read state file and get valid position.
        If not my turn to make move, return an empty list.
        """
        self.valid_pos = []
        self.my_pos = []
        self.opponent_pos = []

        # get state file info
        try:
            if not os.path.isfile(self.stat_file):
                return

            sfile = open(self.stat_file, "r")
            if os.stat(self.stat_file).st_size == 0:
                return

            move = int(sfile.readline())
            self.board = map(int, sfile.readline().split())
            self.first_winner = int(sfile.readline())
            sfile.close()
        except:
            return

        if move == -100:
            self.game_stop = True
            return

        # The only condition of move read from state file being less than our record move (cur_move)
        # is that the second game starts.
        # So, if move is less than cur_move and is not next_first_move,
        # just skip it
        if move > self.cur_move or (move == self.next_first_move and self.cur_move != self.next_first_move):
            # If we are making the first move of first game,
            # record the first move of the second game
            if self.cur_move == -1:
                self.next_first_move = 2 if move == 1 else 1
            
            # Record current move
            self.cur_move = move

            self.valid_pos = [i for i in range(217) if self.board[i] == 0]
            self.my_pos = [i for i in range(217) if self.board[i] == 1]
            self.opponent_pos = [i for i in range(217) if self.board[i] == 2]
        else:
            return

    def step(self):
        """
        Get the next move and write it into move file.
        """
        pos = self._get_next_move()
        self._write_move(pos)

    def _get_next_move(self):

        """
        Get a position from valid_pos randomly.
        You should implement your algorithm here.
        These utilities may be helpful:
            self.get_valid_pos()
            self.get_my_pos()
            self.get_opponent_pos()
            self.get_board()

        Check them below for more detail
        """
        op_list = build_node(self.get_opponent_pos()) #input a list of data
        #op_list is node list with directional commutation
        #Minimax(self.get_valid_pos(), oplist, alpha, depth)
        return self.valid_pos[randint(0, len(self.valid_pos)-1)]

    def _write_move(self, pos):
        """
        Write my move into move file.
        """
        with open(self.move_file, "w") as mfile:
            mfile.write(str(self.cur_move) + " " + str(pos))

    def is_my_turn(self):
        """
        If the valid position is not empty, it is my turn.
        """
        return len(self.valid_pos) != 0

    def is_game_stop(self):
        return self.game_stop

    # some utilities to get the game state
    def get_valid_pos(self):
        """
        Get the valid position where you can put your stone.
        A list of int. e.g. [0, 1, 3, 5, 6, 9, 12,...]
        """
        return self.valid_pos

    def get_my_pos(self):
        """
        Get the position where you have put.
        A list of int. e.g. [2, 4, 7, 8, ...]
        """
        return self.my_pos

    def get_opponent_pos(self):
        """
        Get the position where your opponent have put.
        A list of int. e.g. [10, 11, 13, ...]
        """
        return self.opponent_pos

    def get_board(self):
        """
        Get current board. 0: valid pos, 1: your pos, 2: opponent pos
        A list of int. e.g. [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 2, 2, 0, 2...]
        """
        return self.board

    def is_first_winner(self):
        """
        Are you the winner of first game?
        Return -1: the first game is still continuing.
                1: yes, you are.
                0: no, you are not.
        """
        return self.first_winner

def main():
    # Change the team number to yours.
    agent = Agent(22)

    while True:
        agent.process_state_info()
        if (agent.is_game_stop()):
            break

        if (agent.is_my_turn()):
            agent.step()


if __name__ == "__main__":
    main()