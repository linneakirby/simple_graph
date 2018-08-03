"""
Linnea Kirby
RC Application Round 3
3 August 2018

Tests for simple_graph.py

"""

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

	def test_None_data(self):
		with self.assertRaises(ValueError):
			simple_graph.build_graph(
				{
				'a': ['b'],
				'b': [None]
				},
				'a')

	def test_equality(self):
		a = simple_graph.Graph("a")
		a2 = simple_graph.Graph("a")
		b = simple_graph.Graph("b")

		a.add_child(b)
		a2.add_child(b)

		self.assertEqual(a, a2)

	def test_inequality(self):
		a = simple_graph.Graph("a")
		a2 = simple_graph.Graph("a")
		b = simple_graph.Graph("b")
		c = simple_graph.Graph("c")

		a.add_child(b)
		a2.add_child(c)

		self.assertNotEqual(a, a2)

	def test_look_deep_for_existing_node(self):
		d = HoldenCaulfield()
		g = HoldenCaulfield()

		self.assertIsNot(d, g)

		root_node = simple_graph.build_graph(
			{
			'a': ['b', 'c'],
	        'b': [d, 'e', 'f'],
	        'c': [g],
	        'g': ['h']
	        },
	        'a')

		target_node = simple_graph.look_deep_for(root_node, HoldenCaulfield())

		self.assertIs(
			target_node.get_data(), d)

	def test_look_deep_for_nonexistent_node(self):

		root_node = simple_graph.build_graph(
			{
			'a': ['b', 'c'],
	        'b': ['d', 'e', 'f'],
	        'c': ['g'],
	        'g': ['h']
	        },
	        'a')

		self.assertIsNone(
			simple_graph.look_deep_for(root_node, 'z'))

class HoldenCaulfield(object):
	def __eq__(self, other):
		return isinstance(other, type(self))

	def __hash__(self):
		return hash(id(self))

	def __ne__(self, other):
		return not self == other


if __name__ == '__main__':
  unittest.main()