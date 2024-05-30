import hazelcast

queue_name = "my-bounded-queue"

hz = hazelcast.HazelcastClient(
    cluster_name="my-cluster",
    cluster_members=[
         "127.0.0.1:5701",
        "127.0.0.1:5702"
    ],
)
queue = hz.get_queue(queue_name).blocking()
'''
for i in range(100):
    queue.put(i)
    print("I am " + str(i))
queue.put(-1)
print("Dissmissed")

'''
while True:
    item = queue.take()
    print("You are " + str(item))
    if (item == -1):
        queue.put(-1)
        break

