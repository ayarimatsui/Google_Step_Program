# Google STEP Program week4 homework1

from collections import deque

class Node:
    def __init__(self, nickname):
        self.nickname = nickname
        self.follows = []
        
    def add_follow(self, user_id):
        self.follows.append(user_id)


# breadth first search
# search the path and distance from start to goal
def bfs(node_list, start, goal):
    N = len(node_list)   # total number of nodes
    # create queue and append root node
    q = deque()
    q.append(start)
    # create a list to check whether nodes are visited or not
    dist_list = [None] * N  # 1 if already checked
    dist_list[start] = 0

    # repeat while the queue is not empty
    while len(q) > 0:
        # take out the first node in the queue
        node_id = q.popleft()
        distance = dist_list[node_id]

        if node_id == goal:
            print('reached {} from {}!!'.format(node_list[goal].nickname, node_list[start].nickname))
            return distance

        for user_id in node_list[node_id].follows:
            if dist_list[user_id] is None:  # if the node is unchecked
                dist_list[user_id] = distance + 1
                q.append(user_id)

    return None


# find the farthest node from the root node
# find by bfs
# also find whether there are nodes that cannot be reached from root node
def find_farthest(node_list, root_node):
    N = len(node_list)   # total number of nodes
    # create queue and append root node
    q = deque()
    q.append(root_node)
    # create a list to check whether nodes are visited or not
    dist_list = [None] * N  # 1 if already checked
    dist_list[root_node] = 0

    # repeat while the queue is not empty
    while len(q) > 0:
        # take out the first node in the queue
        node_id = q.popleft()
        distance = dist_list[node_id]

        for user_id in node_list[node_id].follows:
            if dist_list[user_id] is None:  # if the node is unchecked
                dist_list[user_id] = distance + 1
                q.append(user_id)

        # if the node is the last one
        if len(q) == 0:
            print('the farthest node from {} is {}'.format(node_list[root_node].nickname, node_list[node_id].nickname))
            print('the distance is {}'.format(distance))

    # return unvisited nodes (the nodes cannot be reached from root node)
    unvisited = []
    for id, d in enumerate(dist_list):
        if d is None:
            unvisited.append(node_list[id].nickname)

    return unvisited



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
                my_id = int(ID)
            elif nickname == target_name:
                target_id = int(ID)

    # read links.txt and record follows
    with open('links.txt') as links_f:
        for line in links_f:
            ID, follow = map(int, line.strip().split())
            node_list[ID].add_follow(follow)

    # check whether my account(jamie) can be reached from target(adrian)
    distance_from_target = bfs(node_list, target_id, my_id)
    if distance_from_target is None:
        print('There is no path from {} to {}'.format(node_list[target_id].nickname, node_list[my_id].nickname))
    else:
        print('the distance from {} to {} : {}'.format(node_list[target_id].nickname, node_list[my_id].nickname, distance_from_target))

    # check the farthest node from my account
    # also find whether there are nodes that cannot be reached from my account
    unreachable = find_farthest(node_list, my_id)
    if len(unreachable) > 0:
        print('unreachable accounts from {} : {}'.format(node_list[my_id].nickname, ' '.join(unreachable)))
    else:
        print('every account is reachable from {}'.format(node_list[my_id].nickname))