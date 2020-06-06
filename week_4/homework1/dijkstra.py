# Google STEP Program week4 homework1
# optional, advanced
# Dijkstra Algorithm

import heapq

class Station:
    def __init__(self, name):
        self.name = name
        self.next_stations = []

    def add_next_station(self, station_id, cost):
        self.next_stations.append([station_id, cost])


def dijkstra(stations_list, start, goal):
    N = len(stations_list)
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
        
        for station_id, cost in stations_list[last].next_stations:
            if dist[station_id] > dist[last] + cost:
                dist[station_id] = dist[last] + cost
                heapq.heappush(q, [dist[station_id], route + [station_id]])

    return None, []



if __name__ == '__main__':
    start_name = input('input the start (station name) : ')
    goal_name = input('input the goal (station name) : ')
    stations_list = []
    # read stations.txt and make a list of stations
    # also indentify the IDs of start and goal
    with open('stations.txt') as stations_f:
        for line in stations_f:
            ID, station_name = line.strip().split()
            stations_list.append(Station(station_name))
            if station_name == start_name:
                start_id = int(ID)
            elif station_name == goal_name:
                goal_id = int(ID)


    # read edges.txt and record cost(time)
    with open('edges.txt') as edges_f:
        for line in edges_f:
            from_ID, to_ID, cost = map(int, line.strip().split())
            stations_list[from_ID].add_next_station(to_ID, cost)
            stations_list[to_ID].add_next_station(from_ID, cost)


    total_cost, route = dijkstra(stations_list, start_id, goal_id)
    if total_cost is None:
        print('There is no route to go to {} from {}'.format(goal_name, start_name))
    else:
        route_names = []
        for station_id in route:
            route_names.append(stations_list[station_id].name)
        print('The shortest route from {} to {} is : {}'.format(start_name, goal_name, ' -> '.join(route_names)))
        print('total time from {} to {} is :  {} min'.format(start_name, goal_name, total_cost))