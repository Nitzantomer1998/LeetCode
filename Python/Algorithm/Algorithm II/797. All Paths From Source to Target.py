def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
    
    solution_paths = []

    def finding_path(current_node: int, current_path: list[int]) -> None:
        
        if current_node == len(graph) - 1:
            solution_paths.append(current_path)
            return

        for next_node in graph[current_node]:
            finding_path(next_node, current_path + [next_node])

    finding_path(0, [0])

    return solution_paths
