def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
    """
    Finding all the possible paths from node 0 to node n - 1, and return it

    :param graph: Matrix that every row is a node and every column is the node neighbors
    :return: All the possible paths from node 0 to node n - 1

    Time Complexity: o(|E| + |V|)
    Space Complexity: o(|E| + |V|)
    """
    # List storing the possible paths for reaching to the last node
    solution_paths = []

    # Assisting function to make the DFS calls
    def finding_path(current_node: int, current_path: list[int]) -> None:
        """
        Recursive function for finding the possible paths from the current node using DFS Algorithm

        :param current_node: Integer representing a node
        :param current_path: List representing the current path that we made
        :return: Nothing, everything happening in place
        """
        # if current node == len(graph) - 1, means we have reach to the target, so add the current path to the solution
        if current_node == len(graph) - 1:
            solution_paths.append(current_path)
            return

        # if we haven't reached to the solution yet, make a DFS call for every possible path from the current node
        for next_node in graph[current_node]:
            finding_path(next_node, current_path + [next_node])

    # Making the first DFS call, that will create all the possible path to the target, and update the solution path
    finding_path(0, [0])

    # Returning all the paths that lead us to target
    return solution_paths
