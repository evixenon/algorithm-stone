# @before-stub-for-debug-begin
from python3problem146 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class DLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.moveToHead(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.moveToHead(self.cache[key])
            self.cache[key].value = value
        else:
            node = DLinkedNode(key, value)
            if self.size == self.capacity:
                self.removeTail()
            self.cache[key] = node
            self.addToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node):
        second = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = second
        second.prev = node
        self.cache[node.key] = node
        self.size += 1

    def removeTail(self):
        newTail = self.tail.prev.prev
        self.cache.pop(self.tail.prev.key)
        newTail.next = self.tail
        self.tail.prev = newTail
        self.size -= 1
    
    def removeNode(self, node):
        tmp = node.prev
        node.prev.next = node.next
        node.next.prev = tmp
        self.size -= 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

