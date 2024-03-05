import sys

class Node:
    def __init__(self, ch, f):
        self.character = ch
        self.frequency = f
        self.left_bit = None
        self.right_bit = None
        self.left = None
        self.right = None

def get_ch_freq_map(message):
    """returns a dictionary of characters and their frequency of occurance in the message."""
    ch_freq_map = {}
    for ch in message: #O(n)
        if ch not in ch_freq_map.keys():
            ch_freq_map[ch] = 1
        else:
            ch_freq_map[ch] += 1
    return ch_freq_map

def create_node_list(ch_freq_map):
    """creates a list of nodes from the sorted items of the ch_freq_map."""
    sorted_ch_freq_map = sorted(ch_freq_map.items(), key=lambda x:x[1]) #O(nlogn)
    nodes_list = []
    for k, v in sorted_ch_freq_map:
        nodes_list.append(Node(k, v))
    return nodes_list
def insert_node_in_node_list(nodes_list, new_node):
    """Inserts the new node in the nodes list based on its frequency and returns the resorted nodes_list."""
    cn = new_node
    node_inserted = False
    for index, node in enumerate(nodes_list):
        if cn.frequency < nodes_list[index].frequency:
            nodes_list.insert(index, cn)
            node_inserted = True
            return nodes_list
    if not node_inserted:
        nodes_list.append(cn)
        return nodes_list

def create_huffman_tree(nodes_list):
    """Creates the huffman tree and assigns the left and right bits(0 and1)
     to the respective nodes. Returns the root node of the tree"""
    if len(nodes_list) == 1 :
        return nodes_list[0]
    while len(nodes_list)>1:
        node1 = nodes_list.pop(0)
        node2 = nodes_list.pop(0)
        new_node = Node("", node1.frequency + node2.frequency)
        new_node.left = node1
        new_node.right = node2
        new_node.left_bit = 0
        new_node.right_bit = 1
        nodes_list = insert_node_in_node_list(nodes_list, new_node) #O(n)
    nodes_list[0].left_bit = 0
    nodes_list[0].right_bit = 1
    return nodes_list.pop(0)
def create_ch_bit_map(node,ch_code, ch_bit_map):
    """Returns a mapping of each character to its bit combo."""
    if node.left == None and node.right == None:
        ch_bit_map[node.character] = ch_code
        return

    create_ch_bit_map(node.left, ch_code + str(node.left_bit), ch_bit_map)
    create_ch_bit_map(node.right, ch_code + str(node.right_bit), ch_bit_map)
    return ch_bit_map

def create_code(tree_root, message):
    """Uses the ch_bit_map to encode the message and return the encoded message."""
    ch_bit_map = create_ch_bit_map(tree_root, "", {})
    code = ''
    for ch in message:
        code += ch_bit_map[ch]
    return code

def huffman_encoding(message):
    """Calls all the necessary methods to create the encoded message
    and returns the tree root and encoded message."""
    ch_freq_map = get_ch_freq_map(message)
    nodes_list = create_node_list(ch_freq_map)
    tree_root = create_huffman_tree(nodes_list)
    coded_msg = create_code(tree_root, message)
    return coded_msg, tree_root

def huffman_decoding(encoded_data, root):
    """decodes the message by traversing the tree."""
    decoded_msg = ""
    cn = root
    for num in encoded_data: #O(n)
        if num == '0':
            cn = cn.left
        else:
            cn = cn.right
        if not cn.left and not cn.right:
            decoded_msg += cn.character
            cn = root
    return decoded_msg

if __name__ == "__main__":
    codes = {}

    def test_function(test_case):
        if len(test_case) <= 1 :
            print(f"Invalid message. Cannot create a tree with {len(test_case)} characters.")
            return

        print ("The size of the data is: {}\n".format(sys.getsizeof(test_case)))
        print ("The content of the data is: {}\n".format(test_case))

        encoded_data, tree = huffman_encoding(test_case)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

    test_case_0 = "The bird is the word"
    test_case_1 = ""
    test_case_2 = "i"
    test_case_3 = "ab"
    test_case_4 = "This project has been very veryveryveryveryveryveryvery lonnnnnnnnnnnnnnnnnnnnnnnnnnn" \
                  "gggggggggggggggggggggggggggggggggggggggg. Hope its good enough to paaaaaaaaaaaaaaa" \
                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas111111111" \
                  "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    test_function(test_case_0)
    # output:
    # The size of the data is: 69
    # The content of the data is: The bird is the word
    # The size of the encoded data is: 36
    # The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010
    # The size of the decoded data is: 69
    # The content of the encoded data is: The bird is the word
    test_function(test_case_1)
    # output:
    # Invalid message. Cannot create a tree with 0 characters.
    test_function(test_case_2)
    # output:
    # Invalid message. Cannot create a tree with 1 characters.
    test_function(test_case_3)
    # output
    # The size of the data is: 51
    # The content of the data is: ab
    # The size of the encoded data is: 28
    # The content of the encoded data is: 01
    # The size of the decoded data is: 51
    # The content of the encoded data is: ab
    test_function(test_case_4)
#     output
# The size of the data is: 372
# The content of the data is: This project has been very veryveryveryveryveryveryvery lonnnnnnnnnnnnnnnnnnnnnnnnnnngggggggggggggggggggggggggggggggggggggggg. Hope its good enough to paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas111111111!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  The size of the encoded data is: 168
# The content of the encoded data is: 001001000011110000001100100011100001111100101000010010010111101001001100000001110000111101000100011100001001111110111101111111100000101110100101000111110000010111010010100011000101110100101000110001011101001010001100010111010010100011000101110100101000110001011101001010001100010111010010100011111000011100000001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110001110011110000111010000010011111111011110000000110000000010001110011000001000010011101111100111011111000010000010110001111011100000000000011110000111111010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010100010000011000110001100011000110001100011000110001100101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
# The size of the decoded data is: 372
# The content of the encoded data is: This project has been very veryveryveryveryveryveryvery lonnnnnnnnnnnnnnnnnnnnnnnnnnngggggggggggggggggggggggggggggggggggggggg. Hope its good enough to paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas111111111!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
