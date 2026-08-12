'''
create class called node
intialize it with key, val
intialize them
intialize two pointers for the prev and the next and set them to null

'''
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        '''
        intialize the capacity to keep up with it
        

        intialize our cache which will be a dictionary that will allow us to map our keys to nodes

        intialize our dummy nodes as our left and right that has the value of 0,0

        intialize our left next to right , right to our left since left = LRU and right = MRU
        '''
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    '''
    create our helper function that is call remove and it takes in self, node this removes the LRU 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    '''

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    '''
    create another helper function that is call insert which takes in self, node that inserts at right
    prev, nxt = self.right.prev, self.right
    prev.next = nxt.prev = node
    node.next, node.prev = nxt, prev
    '''

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        '''
        if key in our cache:
            remove our cache[key].val

        .val
        insert our cache[key].val
        return our cache[key].val

        return -1

        '''
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        '''
        if key in our cache:
            remove this from our list
            create new node with the key, value that will be put as the cache[key]
            take this node and insert into our list

        if length of our cache > our capacity that we intialize earlier
            remove this from our linked list
            delete this from our cache
            lru is always going to be our left node
        '''
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:

# obj = LRUCache(capacity)

# param_1 = obj.get(key)

# obj.put(key,value)

# U - o(1) constant time
'''
initialize the LRU Cache with a positive int which is called capacity

two things need to happen:
class get will take the int called key and return the value of key if it exists else return -1

class put will take in the current key, current val must update the key if it exist else add this pair to the cache
if the cache length go over the capacity then we pop the first index of the cache
ex: 1,2,3,4,5,6

How to keep track of the item that would need to be evicted? (put)

- Keep the items in order where the LRU is the first index
- Create an doubly linkedlist
  keep the map in align with the linkedlist which constant time since it is pointing to a node instead of having to traverse through the entire list
'''

End
End