import hashlib
from datetime import date

def calc_hash(data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = date.today()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.next = None

    def __str__(self):
        return str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.hash)

class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data, previous_hash):
        if self.head == None:
            self.head = Block(data, 0)
            return

        cn = self.head
        while cn.next: #O(n)
            cn = cn.next
        cn.next = Block(data, cn.hash)
    def to_list(self):
        list = []
        block = self.head
        while block: #O(n)
            list.append(block)
            block = block.next
        return list

    def __str__(self):
        return str(self.head)+str(self.head.next)

blockchain = BlockChain()
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
blockchain.append('Some data', None)
print("Testcase1:")
print(*blockchain.to_list(), sep ='\n')
print()
#Output:
# Testcase1:
# 2024-01-19Some data01fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef6

## Test Case 2
blockchain.append('some more data', calc_hash('Some data'))
print("Testcase2:")
print(*blockchain.to_list(), sep ='\n')
print()
# Output:
# Testcase2:
# 2024-01-19Some data01fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef6
# 2024-01-19some more data1fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef62eada558913786e380693fae11c031d2cf6996c76294e78401a50f5f7c386532

## Test Case 3
blockchain.append('', calc_hash('Some more data'))
print("Testcase3:")
print(*blockchain.to_list(), sep ='\n')
print()
# output:
# Testcase3:
# 2024-01-19Some data01fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef6
# 2024-01-19some more data1fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef62eada558913786e380693fae11c031d2cf6996c76294e78401a50f5f7c386532
# 2024-01-192eada558913786e380693fae11c031d2cf6996c76294e78401a50f5f7c386532e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Test Case 4
blockchain.append('Last bit of data', calc_hash(''))
print("Testcase4:")
print(*blockchain.to_list(), sep ='\n')
print()
# Output:
# Testcase4:
# 2024-01-19Some data01fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef6
# 2024-01-19some more data1fe638b478f8f0b2c2aab3dbfd3f05d6dfe2191cd7b4482241fe58567e37aef62eada558913786e380693fae11c031d2cf6996c76294e78401a50f5f7c386532
# 2024-01-192eada558913786e380693fae11c031d2cf6996c76294e78401a50f5f7c386532e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
# 2024-01-19Last bit of datae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855de1242db68d9da9fa2b0ad717276615c596214ee945773c53c4951f51a0b8143
