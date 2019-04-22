import Queue

q = Queue.PriorityQueue()
q.insert(1)
q.insert(2)
q.insert(3)
q.print()
a = q.delete()
print(a)
q.print()