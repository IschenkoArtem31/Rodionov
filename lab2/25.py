import hazelcast

map_name = "distributed-map"

def tasks_three_five():
    client = hazelcast.HazelcastClient(
    cluster_name="my-cluster",
    cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703",
    ],
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)
    key = 0
    counter = 0
    map = client.get_map("distributed-map").blocking()
    for i in range(1000):
       	key+=1
        counter+=1
        map.put(key, counter)

def sixth_task_no_locks():
    client = hazelcast.HazelcastClient(
    cluster_name="my-cluster",
    cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703",
    ],
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)
    key = "No Locks"
    #counter = 0
    map = client.get_map("distributed-map").blocking()
    #map.put(key, counter)
    if (map.contains_key(key) is False):
        map.put(key,0)
    for i in range(1000):
        counter = map.get(key)
        counter += 1
        map.put(key, counter)
    print(map.get(key))

def sixth_task_pessimistic():
	client = hazelcast.HazelcastClient(
    cluster_name="my-cluster",
    cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703",
    ],
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)
	key = "Pessimistic"
	map = client.get_map("distributed-map").blocking()
	if (map.contains_key(key) is False):
		map.put(key,0)
	for i in range(1000):
		map.lock(key)
		try:
			value = map.get(key)
			value += 1
			map.put(key, value)
			#print(map.get(key))
		finally:
			map.unlock(key)
	print(map.get(key))

def sixth_task_optimistic():
    client = hazelcast.HazelcastClient(
    cluster_name="my-cluster",
    cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703",
    ],
    lifecycle_listeners=[
        lambda state: print("Lifecycle event >>>", state),
    ]
)
    key = "Optimistic"
    map = client.get_map("distributed-map").blocking()
    if (map.contains_key(key) is False):
        map.put(key,0)
    loop = True
    for i in range(1000):
        while loop is not False:
            oldValue = map.get(key)
            newValue = oldValue
            newValue += 1
            if (map.replace_if_same(key, oldValue, newValue)): 
                break
    print(map.get(key))

if __name__ == "__main__":
	
	tasks_three_five()
	sixth_task_no_locks()
	sixth_task_pessimistic()
	sixth_task_optimistic()
