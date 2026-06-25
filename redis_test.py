import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# r.set("name2", "test2")
# vl = r.get("name2")
# print(vl)

##########################################
# r.lpush("list1", "a", "b", "c")
# r.rpush("list1", "x")
#
# list1 = r.lrange("list1", 0, -1)
# for val in list1:
#    print(val)
#
###########################################

r.hset("hash1", "a1", "a1")
r.hset("hash1", "a2", "a2")
r.hset("hash1", "a3", "a3")

hash1 = r.hgetall("hash1")

print(hash1)

print(r.hlen("hash1"))


r.close()
