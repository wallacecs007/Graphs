"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()

        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex (dequeue from queue)
            currentVertex = queue.dequeue()

            # Check if the current vertex has not been visited:
            if currentVertex not in visited:
                # print the current vertex
                print(currentVertex)
                # Mark the current vertex as visited
                visited.add(currentVertex)
                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbors in self.get_neighbors(currentVertex):
                    queue.enqueue(neighbors)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex (pop from stack)
            currentVertex = stack.pop()
            # Check if the current vertex has not been visited:
            if currentVertex not in visited:
                # print the current vertex
                print(currentVertex)
                # Mark the current vertex as visited
                visited.add(currentVertex)
                # push up all the current vertex's neighbors (so we can visit them next
                for neighbors in self.get_neighbors(currentVertex):
                    stack.push(neighbors)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue({
            'currentVertex': starting_vertex,
            'path': [starting_vertex]
        })
        visited = set()

        while queue.size() > 0:
            currentItem = queue.dequeue()
            currentPath = currentItem['path']
            currentVertex = currentItem['currentVertex']

            if currentVertex not in visited:
                if currentVertex == destination_vertex:
                    return currentPath
                visited.add(currentVertex)

                for neighbor in self.get_neighbors(currentVertex):
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                    queue.enqueue({
                        'currentVertex': neighbor,
                        'path': newPath
                    })
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push({
            'currentVertex': starting_vertex,
            'path': [starting_vertex]
        })
        visited = set()

        while stack.size() > 0:
            currentItem = stack.pop()
            currentPath = currentItem['path']
            currentVertex = currentItem['currentVertex']

            if currentVertex not in visited:
                if currentVertex == destination_vertex:
                    return currentPath

                visited.add(currentVertex)

                for neighbor in self.get_neighbors(currentVertex):
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                    stack.push({
                        'currentVertex': neighbor,
                        'path': newPath
                    })
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
