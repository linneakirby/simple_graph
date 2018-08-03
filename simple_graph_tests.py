"""
Linnea Kirby
RC Application Round 3
1 August 2018

Tests for simple_graph.py

"""

import collections
import unittest

import simple_graph

class GraphTest(unittest.TestCase):

	@unittest.SkipTest
	def test_equality(self):
		a = simple_graph.Graph("a")
		b = simple_graph.Graph("a")

		self.assertEqual(a, b)

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

	def test_look_deep_for(self):
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

class HoldenCaulfield(object):
	def __eq__(self, other):
		return isinstance(other, type(self))

	def __hash__(self):
		return hash(id(self))


if __name__ == '__main__':
  unittest.main()