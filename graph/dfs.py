class Graph():

	# traverse graph through depth first search(iterative)
	def dfs_iter(self, graph, start):
		visited = set()
		stack = [start] 

		while stack:
			node = stack.pop()
			if node not in visited:
				print node
				visited.add(node)
				stack.extend(graph[node] - visited)

		return visited # list of visited nodes in the graph 

	# dfs recursive implementation
	def dfs_rec(self, graph, start, visited=None):
		if visited is None:
			visited = set()
		visited.add(start)
		for n in graph[start] - visited:
			self.dfs_rec(graph, n, visited)
		return visited
	

def main():
	graph = {'A': set(['B', 'C']),
	         'B': set(['A', 'D', 'E']),
	         'C': set(['A', 'F']),
	         'D': set(['B']),
	         'E': set(['B', 'F']),
	         'F': set(['C', 'E'])} 

	print Graph().dfs_iter(graph, 'A') 
	print Graph().dfs_rec(graph, 'A')


if __name__ == "__main__": 
	 main()














