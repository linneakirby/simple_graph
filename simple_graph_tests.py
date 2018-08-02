#Tests for simple_graph.py

import collections
import unittest

import simple_graph

class GraphTest(unittest.TestCase):

	def test_minimal_graph_construction_root_data(self):
		root_node = simple_graph.build_graph(
			{
			'a': ['b'],
			'b': ['c']
			},
			'a')

		self.assertEqual(
			root_node.get_data(), "a")

	def test_minimal_graph_construction_root_children(self):
		root_node = simple_graph.build_graph(
			{
			'a': ['b'],
			'b': ['c']
			},
			'a')

		children_values = []
		for child in root_node.children():
			children_values.append(child.get_data())
			
		self.assertEqual(
				children_values, ['b'])

	def test_graph_construction_root_data(self):
		root_node = simple_graph.build_graph(
			{
			'a': ['b', 'c'],
	        'b': ['d', 'e', 'f'],
	        'c': ['g'],
	        'g': ['h']
	        },
	        'a')

		self.assertEqual(
			root_node.get_data(), "a")

	def test_graph_construction_root_children(self):
		root_node = simple_graph.build_graph(
			{
			'a': ['b', 'c'],
	        'b': ['d', 'e', 'f'],
	        'c': ['g'],
	        'g': ['h']
	        },
	        'a')
		
		children_values = []
		for child in root_node.children():
			children_values.append(child.get_data())
			
		self.assertEqual(
				children_values, ['b', 'c'])


if __name__ == '__main__':
  unittest.main()