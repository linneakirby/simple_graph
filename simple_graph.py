"""
Linnea Kirby
RC Application Round 3
1 August 2018

"Depth-first searcher"
"""

class Graph(object):
	"""A simple implementation of a Graph."""
	def __init__(self, data, parent=None, children=None):
		self._data = data

		#must be a list of Graph objects
		if not children:
			self._children = []
		else:
			self._children = children

		#must be a Graph object
		self._parent = parent
	
	def __str__(self):
		children_list = []
		if len(self._children) > 0:
			for child in self._children:
				children_list.append(child.get_data())
		return str({self.get_data() : str(children_list)})

	# def __eq__(self, other):
	# 	pass

	def get_data(self):
		return self._data

	def children(self):
		return self._children

	def parent(self):
		return self._parent

	def add_parent(self, parent):
		self._parent = parent

	def add_child(self, new_child):
		"""adds a Graph object as the right-most child and defines self as parent of new_child"""
		self._children.append(new_child)
		new_child.add_parent(self)

	def add_children(self, new_children):
		"""adds Graph objects as the right-most children and defines self as parent of each child"""
		for new_child in new_children:
			self.add_child(new_child)

	def look_deep_for(self, target_value):
		"""depth-first search for target_value"""
		
		#recursively look through left-most children all the way down
		if (self._data == target_value):
			return self

		else:
			for child in self._children:
				if child is not None:
					#print("looking in child ", child.data)
					child.look_deep_for(target_value)
				else:
					return

	def look_broadly_for(self, target_value):
		"""breadth-first search for target_value"""
		pass


def build_graph(structure, root_value):
	"""defines a graph from a given structure and root node value"""
	root = Graph(root_value)
	existing_nodes = {root_value : root}

	for parent_value, children_values in structure.items():
		#get parent
		if(parent_value in existing_nodes):
			parent = existing_nodes.get(parent_value)
		else:
			parent = Graph(parent_value)
			existing_nodes[parent_value] = parent

		#get child
		for child_value in children_values:
			if(child_value in existing_nodes):
				child = existing_nodes.get(child_value)
			else:
				child = Graph(child_value)
				existing_nodes[child_value] = child

			#add connections between parent and child
			parent.add_child(child)

	return root


#create a Graph from given input and traverse it in the manner specified
#default: depth-first
def main():
	root_node = build_graph(
			{
			'a': ['b', 'c'],
	        'b': ['d', 'e', 'f'],
	        'c': ['g'],
	        'g': ['h']
	        },
	        'a')

	print(str(root_node))


if __name__ == "__main__":
	main()