class Graph():

	# traverse graph through breadth first search(iterative)
	def  bfs_iter(self, graph, start):
		visited = set()
		q = [start]
		while q:
			node = q.pop(0)
			if node not in visited:
				visited.add(node)
				print node
				q.extend(graph[node] - visited)

		return visited


	# bfs recursive implementation
	def bfs_rec(self, graph, start, visited=None):
		# yet to implement, tricky because we're using a queue.. 
		return "YOU STILL NEED TO IMPL BFS REC!!!"
	
	

def main():
	graph = {'A': set(['B', 'C']),
	         'B': set(['A', 'D', 'E']),
	         'C': set(['A', 'F']),
	         'D': set(['B']),
	         'E': set(['B', 'F']),
	         'F': set(['C', 'E'])} 

	print Graph().bfs_iter(graph, 'A') 
	print Graph().bfs_rec(graph, 'A')


if __name__ == "__main__": 
	 main()














