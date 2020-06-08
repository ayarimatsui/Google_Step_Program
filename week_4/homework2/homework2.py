from collections import deque
import heapq

class Page:
    def __init__(self, name):
        self.name = name
        self.link_to = []
        self.link_from = []

    def add_link_to(self, page_id):
        self.link_to.append(page_id)

    def add_link_from(self, page_id):
        self.link_from.append(page_id)

    def get_linked_pages(self):
        return self.link_to



# breadth first search
# find the loop size of 6
# bfs
def find_loop(page_list, N, target):
    # create queue and append root node
    q = deque()
    q.append([0, [target]])  # distance, route
    check_list = [0] * N  # 1 if already checked

    route_list = []
    # repeat while the queue is not empty
    while len(q) > 0:
        # take out the first node in the queue
        dist, route = q.popleft()
        if dist >= 7:
            break

        node_id = route[-1]

        if dist == 6 and node_id == target:
            if len(set(route)) == 6:
                print('found a loop size of 6 from {} to {}!!'.format(page_list[target].name, page_list[target].name))
                route_list = route
                break

        for page in page_list[node_id].link_to:
            if check_list[page] == 0:
                if page != target:
                    check_list[page] = 1
                q.append([dist + 1, route + [page]])

    loop_pages = []
    for page_id in route_list:
        loop_pages.append(page_list[page_id].name)
    
    return loop_pages


# dijkstra algorithm
def dijkstra(page_list, N, start, goal):
    dist = [float('inf')] * N
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, [start]])

    while len(q) > 0:
        # take out the smallest from the heap
        total_cost, route = heapq.heappop(q)
        last = route[-1]
        # if it reaches the goal
        if last == goal:
            return total_cost, route
        
        for page_id in page_list[last].link_to:
            if dist[page_id] > dist[last] + 1:
                dist[page_id] = dist[last] + 1
                heapq.heappush(q, [dist[page_id], route + [page_id]])

    return None, []


if __name__ == '__main__':
    target_name = 'Google'
    start_name = '渋谷'
    goal_name = '東京ディズニーランド'
    wiki_page_list = []
    N = 0
    # read wikipedia_links/pages.txt and make a list of pages
    with open('wikipedia_links/pages.txt') as pages_f:
        for line in pages_f:
            ID, name = line.strip().split()
            wiki_page_list.append(Page(name))
            N += 1
            if name == target_name:
                target_id = int(ID)
            if name == start_name:
                start_id = int(ID)
            if name == goal_name:
                goal_id = int(ID)

    # read links.txt and record follows
    # this takes a lot of time
    with open('wikipedia_links/links.txt') as links_f:
        for line in links_f:
            ID, link = map(int, line.strip().split())
            wiki_page_list[ID].add_link_to(link)
            wiki_page_list[link].add_link_from(ID)

    # find a loop size of 6 from target to target
    route = find_loop(wiki_page_list, N, target_id)

    print(' -> '.join(route))


    # find the shortest path from start to goal
    total_cost, route = dijkstra(wiki_page_list, N, start_id, goal_id)

    if total_cost is None:
        print('There is no route to go to {} from {}'.format(goal_name, start_name))
    else:
        route_names = []
        for page_id in route:
            route_names.append(wiki_page_list[page_id].name)
        print('The shortest route from {} to {} is : {}'.format(start_name, goal_name, ' -> '.join(route_names)))
        print('total count from {} to {} is :  {}'.format(start_name, goal_name, total_cost))

    ####### 実行結果 #######
    #   found a loop size of 6 from Google to Google!!
    #   Google -> Amazon.com -> オランダ -> 電力自由化 -> 中国華能集団 -> 中国のソフトウェア産業 -> Google
    #   The shortest route from 渋谷 to 東京ディズニーランド is : 渋谷 -> 川越市 -> 東京ディズニーランド
    #   total count from 渋谷 to 東京ディズニーランド is :  2