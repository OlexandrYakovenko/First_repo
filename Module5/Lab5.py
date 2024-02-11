from collections import deque
# dq1=deque([1])
# dq1.append(2)
# dq1.extend([3,4,5])
# dq1.appendleft(2)
# dq1.extendleft([3,4,5])
# print(dq1)
# # print(dq1.index(3))

# print(dq1.pop()) #<==
# print(dq1.popleft())
# print(dq1.popleft())
# print(dq1)
# # print(dq1.index(3))
# # print(dq1.count(3))
# dq1.remove(1)
# print(dq1)
# dq1.rotate(3)
# print(dq1)
# dq1.clear()
# print(dq1)

dq2=deque(['a',2,3,'lemon',5,6,7,8,9])
print(dq2)
dq2.rotate(-4)
print(dq2)


