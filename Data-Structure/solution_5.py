import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

# Method 0
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp

def get_utc_time():
      utc = datetime.datetime.utcnow()
      return utc.strftime("%d/%m/%Y %H:%M:%S")

# Method 1
block0 = Block(get_utc_time(), "Some Information", 0)
block1 = Block(get_utc_time(), "Another Information", block0)
block2 = Block(get_utc_time(), "Some more Information", block1)

print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)

temp = LinkedList()
temp.append(get_utc_time(), "Some Information")
temp.append(get_utc_time(), "Another Information")
print(temp.last.data)
print(temp.last.previous_hash.data)
