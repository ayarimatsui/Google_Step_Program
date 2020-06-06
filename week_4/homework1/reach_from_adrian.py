# Google STEP Program week4 homework1

from collections import deque

class Node:
    def __init__(self, nickname):
        self.nickname = nickname
        self.follows = []
        self.followers = []
        self.dist_from_root = None

    def add_follow(self, user_id):
        self.follows.append(user_id)

    def add_follower(self, user_id):
        self.followers.append(user_id)

    def input_dist(self, dist):
        self.dist_from_root = dist

    def get_dist(self):
        return self.dist_from_root


# breadth first search
def bfs(node_list, start, goal):
    N = len(node_list)   # total number of nodes
    # create queue and append root node
    q = deque()
    q.append(start)
    node_list[start].input_dist(0)  # set the distance of the root node
    # create a list to check whether nodes are visited or not
    check_list = [0 * N]  # 1 if already checked
    check_list[start] = 1

    # repeat while the queue is not empty
    while len(q) > 0:
        # take out the first node in the queue
        node_id = q.popleft()
        distance = node_list[node_id].get_dist()

        if node_id == goal:
            print('reached from target!!')
            return distance

        for user_id in node_list[node_id].follows:
            if check_list[user_id] == 0:  # if the node is unchecked
                check_list[user_id] = 1
                q.append(user_id)
                node_list[user_id].input_dist(distance + 1)

    return None


if __name__ == '__main__':

    my_name = 'jamie'
    target_name = 'adrian'

    node_list = []
    # read nicknames.txt and make a list of nodes
    # also indentify the IDs of target and myself
    with open('nicknames.txt') as nicknames_f:
        for line in nicknames_f:
            ID, nickname = line.strip().split()
            node_list.append(Node(nickname))
            if nickname == my_name:
                my_id = ID
            elif nickname == target_name:
                target_id = ID

    # read links.txt and record follows
    with open('links.txt') as links_f:
        for line in links_f:
            ID, follow = map(int, line.strip().split())
            node_list[ID].add_follow(follow)
            node_list[follow].add_follower(ID)

    distance_from_target = bfs(node_list, target_id, my_id)

    if distance_from_target is None:
        print('There is no path from adrian to me')
    else:
        print('the distance from target : ' + distance_from_target)
