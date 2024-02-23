import collections

DoubleEnded = collections.deque(["Mon","True","Wed"])

DoubleEnded.append("thu")

print("appended at right - ")
print(DoubleEnded)


DoubleEnded.appendleft("sun")
print ("Appended at right at left is - ")
print(DoubleEnded)

DoubleEnded.pop()


print ("Deleting from right - ")
print(DoubleEnded)
