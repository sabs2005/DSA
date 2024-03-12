**Data Structures and Algorithms**
(Udacity nanodegree course)

****Project 1:****

  The tasks in this project test Python knowledge. 
  All task files have details of the tasks within the file itself.

****Project 2:****

  **Problem1:**

    Fle recursion
    For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

  **Problem2:**

    Active directory:
    In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
    Write a function that provides an efficient look up of whether the user is in a group.

  **Problem 3:**

    Blockchain:
    Use your knowledge of linked lists and hashing to create a blockchain implementation.
    We can break the blockchain down into three main parts.
    First is the information hash:
    We do this for the information we want to store in the blockchain such as transaction time, data, and information like the previous chain.
    The next main component is the block on the blockchain:
    Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!

  **Problem 4:**

    Huffman coding:
    Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data.
    Phase I - Build the Huffman Tree
    A Huffman tree is built in a bottom-up approach.
    1.	First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.
    (Unique) Character	Frequency
    A	7
    B	3
    C	7
    D	2
    E	6
    2.	Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list preserves the order of elements in which they are appended.
    We would need our list to work as a priority queue, where a node that has lower frequency should have a higher priority to be popped-out. 
    3.	Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
    4.	Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.
    5.	Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present the building of a Huffman tree.
    6.	For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman tree for our example:
    
    Phase II - Generate the Encoded Data
    7.	Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.
    | (Unique) Character | Frequency | Huffman Code | |:-------------:|:-------------:| | D | 2 | 000 | | B | 3 | 001 | | E | 6 | 01 | | A | 7 | 10 | | C | 7 | 11 |
    Points to Notice
    •	Notice that the whole code for any character is not a prefix of any other code. 
    •	Notice that the binary code is shorter for the more frequent character, and vice-versa.
    •	The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
    •	Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.
    This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101
    B. Huffman Decoding
    Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:
    1.	Declare a blank decoded string
    2.	Pick a bit from the encoded data, traversing from left to right.
    3.	Start traversing the Huffman tree from the root.
    •	If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
    •	If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
    4.	Repeat steps #2 and #3 until the encoded data is completely traversed.

  **Problem5 :**

    Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1,     2] and B = [3, 4] is [1, 2, 3, 4].
    The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].
    You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and           perform your own run time analysis on the code.


****Project3:****

  **Problem1:**

    Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
    For example if the given number is 16, then the answer would be 4.
    If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
    The expected time complexity is O(log(n))

  **Problem2:**

    You are given a sorted array which is rotated at some random pivot point.
    Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
    Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

  **Problem3:**

    Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the         numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
    for e.g. [1, 2, 3, 4, 5]
    The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

  **Problem4:**

    Dutch National Flag Problem
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
    Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

  **Problem 5:**

    Building a Trie in Python
    Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like       predictive text or autocomplete features on mobile phones or web search.
    Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:
    •	A Trie class that contains the root node (empty string)
    •	A TrieNode class that exposes the general functionality of the Trie, like inserting a word or Finding Suffixes
    •	Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will           return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to            receive ["un", "unction", "actory"] back from node.suffixes().
    •	finding the node which represents a prefix.


****Project 4:****

    In this project, you will build a route-planning algorithm like the one used in Google Maps to calculate the shortest path between two points on a map.
    In this project you will use A* search to implement a "Google-maps" style route planning algorithm.
    These Map objects have two properties you will want to use to implement A* search: intersections and roads
    Intersections
    The intersections are represented as a dictionary.
    The roads property is a list where, if i is an intersection, roads[i] contains a list of the intersections that intersection i connects to.
    The map is a network of roads which spans 40 different intersections (labeled 0 through 39).
    •	start - The "start" node for the search algorithm.
    •	goal - The "goal" node.
    •	path - An array of integers which corresponds to a valid sequence of intersection visits on the map.
    •	The algorithm you write will be responsible for generating a path . In fact, when called with the same map, start and goal, as above your algorithm should produce the path [5, 16, 37, 12, 34]
    •	> shortest_path(map_40, 5, 34)
    •	[5, 16, 37, 12, 34]
    use an admissible heuristic to direct search efforts towards the goal
