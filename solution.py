from queue import PriorityQueue
from constants import *
from environment import *
from state import State
import math

class Solver:

    def __init__(self, environment, loop_counter):
        self.environment = environment
        self.loop_counter = loop_counter

    def solve_ucs(self):
        """
        Find a path which solves the environment using Uniform Cost Search (UCS).
        :return: path (list of actions, where each action is an element of ROBOT_ACTIONS)
        """
        start_node = self.environment.get_init_state()
        dict_id = {
            id(start_node) : start_node
        }
        queue = PriorityQueue()
        queue.put((0, id(start_node)))

        visited = set()
        parents = {
            #state : (parent_node, action, cost)
            start_node : (None, None, 0)
        }
        while not queue.empty():
            self.loop_counter.inc()
            current_node_id = queue.get()[1]
            current_node = dict_id[current_node_id]
            successors = [] 

            for action in ROBOT_ACTIONS:
                successful, cost_of_action, successor_node = self.environment.perform_action(current_node, action)
                if not successful:
                    continue
                successors.append((successor_node, action, cost_of_action))

            for successor in successors:

                if self.environment.is_solved(successor[0]):
                    path = [successor[1]]
                    child_node = current_node
                    while child_node != start_node:
                        parent_node = parents[child_node]
                        path.insert(0, parent_node[1])
                        child_node = parent_node[0]
                    return path

                if successor[0] not in visited or (parents[current_node][2] + successor[2]) < parents[successor[0]][2]:
                    cost = parents[current_node][2] + successor[2]
                    parents[successor[0]] = (current_node, successor[1], cost)
                    dict_id[id(successor[0])] = successor[0]
                    queue.put((cost, id(successor[0])))
                    visited.add(successor[0])
            

    def heuristic(self, node):
        """
        Summed manhattan distance from widget centres to closest target node.
        """
        distance = 0

        for element in node.widget_centres:
            new_distance = 9999
            for target in self.environment.target_list:
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = abs(node_rows - goal_rows) + abs(node_cols - goal_cols) if abs(node_rows - goal_rows) + abs(node_cols - goal_cols) < new_distance else new_distance    
            distance += new_distance * 1.5
        return distance

    def heuristic3(self, node):
        """
        
        """
        widget_cells = [widget_get_occupied_cells(self.environment.widget_types[i], node.widget_centres[i], node.widget_orients[i]) for i in range((len(self.environment.widget_types)))]
        targets = set(self.environment.target_list)
        distance = len(targets)
        print(distance)
        for e1 in widget_cells[0]:
            if e1 in targets:
                distance -= 1
        return distance / 3
    
    
    def heuristic2(self, node):

        distance = 0

        for element in node.widget_centres:
            new_distance = 9999
            for target in self.environment.target_list:
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = math.sqrt(abs(node_rows - goal_rows)**2 + abs(node_cols - goal_cols)**2) \
                    if math.sqrt(abs(node_rows - goal_rows)**2 + abs(node_cols - goal_cols)**2) < new_distance \
                    else new_distance
            distance += new_distance * 1.5
        return distance


    def solve_a_star(self):
        """
        Find a path which solves the environment using A* search.
        :return: path (list of actions, where each action is an element of ROBOT_ACTIONS)
        """
        start_node = self.environment.get_init_state()
        dict_id = {
            id(start_node) : start_node
        }
        queue = PriorityQueue()
        queue.put((0, id(start_node)))

        visited = set()
        parents = {
            #state : (parent_node, action, cost)
            start_node : (None, None, 0)
        }
        while not queue.empty():
            self.loop_counter.inc()
            current_node_id = queue.get()[1]
            current_node = dict_id[current_node_id]
            successors = []

            for action in ROBOT_ACTIONS:
                successful, cost_of_action, successor_node = self.environment.perform_action(current_node, action)
                if not successful:
                    continue
                successors.append((successor_node, action, cost_of_action))
            
            for successor in successors:
                if self.environment.is_solved(successor[0]):
                    path = [successor[1]]
                    child_node = current_node
                    while child_node != start_node:
                        parent_node = parents[child_node]
                        path.insert(0, parent_node[1])
                        child_node = parent_node[0]
                    print(f" number of visited: {len(visited)}")
                    print(f" length of frontier: {queue.qsize()}")
                    return path
                cost_so_far = parents[current_node][2] + successor[2]
                if successor[0] not in visited or cost_so_far < parents[successor[0]][2]:
                    parents[successor[0]] = (current_node, successor[1], cost_so_far)
                    dict_id[id(successor[0])] = successor[0]
                    queue.put((parents[current_node][2] + successor[2] + self.heuristic3(current_node), id(successor[0])))
                    visited.add(successor[0])

