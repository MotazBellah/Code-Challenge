import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        string = self.data + ":" + str(self.timestamp) + ":" + str(self.previous_hash)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class BlockChain:
    def __init__(self):
        self.latest_block = None

    def add_block(self, data):
        prev_hash = self.latest_block.value.hash if self.latest_block else None
        block = Block(datetime.now(), data, prev_hash)
        node = Node(block, self.latest_block)
        self.latest_block = node

    def verify_blockchain(self):
        p = self.latest_block
        while p:
            expected_hash = p.value.calc_hash()
            if p.value.hash != expected_hash:
                return False
            if p.next:
                if p.value.previous_hash != p.next.value.hash:
                    return False
            p = p.next
        return True


def make_block(data):
    from datetime import datetime

    return Block(datetime.now(), data)


def test_blockchain(blockchain):
    print(blockchain.verify_blockchain())


def test_blockchain1():
    global blockchain1
    blockchain1 = BlockChain()
    blockchain1.add_block('b11')
    test_blockchain(blockchain1)


def test_blockchain1b():
    blockchain1.latest_block.value.data = 'corrupted'
    test_blockchain(blockchain1)


def test_blockchain2():
    global blockchain2
    blockchain2 = BlockChain()
    blockchain2.add_block('b21')
    blockchain2.add_block('b22')
    test_blockchain(blockchain2)


def test_blockchain2b():
    test_blockchain(blockchain2)


def test_blockchain3():
    blockchain3 = BlockChain()
    test_blockchain(blockchain3)


if __name__ == '__main__':
    test_blockchain1()
    # True

    test_blockchain1b()
    # False

    test_blockchain2()
    # True

    blockchain2.latest_block.next.value.timestamp = datetime.now()
    test_blockchain2b()
    # False

    test_blockchain3()
    # True
