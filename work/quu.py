queue = []

def enqueue(*data):
    queue.extend(data)
    print(queue)

def dequeue():
    if len(queue) <= 0:
        print("Empty queue")
    else:
        queue.pop(0)

def peek():
    if len(queue) <= 0:
        print("Empty queue")
    else:
        print(f"front of queue {queue[0]}")



enqueue(8,9,10)
dequeue()
peek()
print(queue)