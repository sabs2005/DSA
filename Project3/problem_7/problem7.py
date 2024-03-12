## A RouteTrie will store our routes and their associated handlers
import collections
class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # time and space complexity: O(n) n is num of items in path_list
        current_node = self.root
        for part in (path_list):
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        # time complexity:O(n) n is num of keys under root
        # space complexity:O(1) no extra space used
        current_node = self.root
        for part in path_list:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None
        return current_node.handler

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, part, handler):
        # Insert the node as before
        self.children[part] = RouteTrieNode(handler)

## The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
        self.MyRouter = RouteTrie(handler)
        self.MyRouter.root.handler = handler

    def add_handler(self, path, handler):
    # Add a handler for a path
    # You will need to split the path and pass the pass parts   # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.MyRouter.insert(path_list,handler)

    def lookup(self, path):
        path_list = self.split_path(path)
        if path == '/':
            handler = self.MyRouter.root.handler
        elif not path_list:
            handler = 'not found handler'
        else:
            handler = self.MyRouter.find(path_list)
            if handler == None:
                handler = 'not found handler'
        return handler

    def split_path(self, path):
        # time complexity:O(n) n is number of elements in path
        # space complexity:O(1) no extra space used
        path_list = path.split('/')
        if path_list[-1] == '':
            return path_list[1:-1]
        return path.split('/')[1:]

## Here are some test cases and expected outputs you can use to test your implementation
## create the router and add a route
print('Uda test------''\n')
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print('Test1------''\n')
router = Router("root handler")
router.add_handler("/sn/test1", "test1 handler")  # add a route
router.add_handler("/sn/test2", "test2 handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/sn")) # should print 'not found handler'
print(router.lookup("/sn/test1")) # should print 'test1 handler'
print(router.lookup("/sn/test2")) # should print 'test2 handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'


print('Test2------''\n')
router = Router("root handler")
router.add_handler("/this/is/test1", "test1 handler")  # add a route
router.add_handler("/this/is not/test1", "not test1 handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/this/is")) # should print 'not found handler'
print(router.lookup("/this/is not/")) # should print 'test1 handler'
print(router.lookup("/this/is/test1")) # should print 'test2 handler'
print(router.lookup("/this/is not/test1")) # should print 'not test1 handler'
print(router.lookup("")) # should print 'not found handler'

# expected outputs
# Uda test------
#
# root handler
# not found handler
# about handler
# about handler
# not found handler
# Test1------
#
# root handler
# not found handler
# test1 handler
# test2 handler
# not found handler
# Test2------
#
# root handler
# not found handler
# not found handler
# test1 handler
# not test1 handler
# not found handler