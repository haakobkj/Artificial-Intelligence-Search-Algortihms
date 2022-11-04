    
    
    def heuristic(self, node):  
        """
        Heuristic which expands fewer nodes in the first cases, but more nodes in the last cases
        """
        distance = 9999

        for element in node.widget_centres:
            for target in self.environment.target_list:          
                if element not in self.environment.target_list:
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = abs(node_rows - goal_rows) + abs(node_cols - goal_cols)
                    distance = new_distance if new_distance < distance else distance
        return distance

    def heuristic2(self, node):
        
        distance = 0

        for element in node.widget_centres:
            new_distance = 9999
            for target in self.environment.target_list:          
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = abs(node_rows - goal_rows) + abs(node_cols - goal_cols) if abs(node_rows - goal_rows) + abs(node_cols - goal_cols) < new_distance else new_distance
                    
            distance += new_distance
        return distance

    
   

    
    def heuristic3(self, node):
        distance = 0

        for element in node.widget_centres:
            distances = []
            for target in self.environment.target_list:          
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    distances.append(abs(node_rows - goal_rows) + abs(node_cols - goal_cols))             
            distance += sum(distances) / len(distances)
        
        return distance
        

    def heuristic4(self, node):
        distance = 0

        for element in node.widget_centres:
            new_distance = 9999
            for target in self.environment.target_list:          
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = abs(node_rows - goal_rows) + abs(node_cols - goal_cols) if abs(node_rows - goal_rows) + abs(node_cols - goal_cols) < new_distance else new_distance             
            distance += new_distance
        
        return distance / len(node.widget_centres)


    def heuristic6(self, node):  
        """
        Simple eucledian distance from closest
        """
        distance = 9999

        for element in node.widget_centres:
            for target in self.environment.target_list:          
                if element not in self.environment.target_list:
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = math.sqrt(abs(node_rows - goal_rows)**2 + abs(node_cols - goal_cols)**2)
                    distance = new_distance if new_distance < distance else distance
        return distance

    def heuristic7(self, node):
        """
        Eucledian distance for all widget centres to closest target added together
        """
        distance = 0

        for element in node.widget_centres:
            new_distance = 9999
            for target in self.environment.target_list:          
                    node_rows, node_cols = element
                    goal_rows, goal_cols = target
                    new_distance = math.sqrt((node_rows - goal_rows)**2 + (node_cols - goal_cols)**2) if math.sqrt((node_rows - goal_rows)**2 + (node_cols - goal_cols)**2) < new_distance else new_distance             
            distance += new_distance
        
        return distance


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
