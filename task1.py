from queue import Queue
import random
import time

q = Queue()

def generate_request():
    request = f'REQ-{random.randint(1, 999999)}'
    q.put(request)

def process_request():
    if not q.empty():
        req = q.get()
        print(f"Request {req} is resolved")
    else:
        print("The queue is empty")

def main():
    while True:
        print(q.queue)
        time.sleep(random.randint(1, 3))
        generate_request()

        if random.randint(0,1):
            process_request()


if __name__ == '__main__':
    main()