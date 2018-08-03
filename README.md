# simple_graph

This directory contains a simple graph implementation that supports depth-first searching.

## Contents

- `simple_graph.py`
	A Graph class and functions for building a graph and searching through the graph.

## Usage

External users should define a graph within a dictionary containing key, value pairs
of each node's data to its children. This dictionary should then be passed to
simple_graph.build_graph, along with the data corresponding to the root node.
build_graph will return a complete Graph representation.

Here is an example of a call to build_graph with a sample user-defined graph and root node:

```
root_node = build_graph(
		{
		'a': ['b', 'c'],
	        'b': ['d', 'e', 'f'],
	        'c': ['g'],
	        'g': ['h']
	        },
	        'a')
```


