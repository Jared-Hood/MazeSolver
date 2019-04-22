from collections import deque

class Queue(object):
    def __init__(self):
        self.queue = []

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

    def print(self):
        for c in self.queue:
            print(c,end='')
        print('\n')

        # for inserting an element in the queue

    def insert(self, data):
        self.queue.append(data)

        # for popping an element based on Priority

    def delete(self):
        ret = self.queue[0]
        newQ = []
        for a in range(1,len(self.queue)):
            newQ.append(self.queue[a])

        self.queue = []
        for c in newQ:
            self.queue.append(c)
        return ret
