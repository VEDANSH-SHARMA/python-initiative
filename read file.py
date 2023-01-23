numbers=[ ]
with open(r"C:\Users\vedan\Desktop\Priority_Important\SAC\Lulu\pycode\file.txt") as f:
    group=[]
    for line in f:
        if line=="\n":
            numbers.append(group)
            group = []
        else:
            group.append(int(line.rstrip()))
            # append the last group because if line == "\n" will not be True for
            # the last group
    numbers.append(group)
print(numbers)

# or using map

with open(r"C:\Users\vedan\Desktop\Priority_Important\SAC\Lulu\pycode\file.txt") as f:
  nums = [list(map(int, (line.split()))) for line in f.read().rstrip().split("\n\n")]

print(nums)

oldlist=['a','b','c']
newlist = []

# for loop
for word in oldlist:
    newlist.append(word.upper())
print(newlist)

#map
newlist_1 = list(map(str.upper, oldlist))
print(newlist_1)

#List comprehension
newlist_2 = [s.upper() for s in oldlist]
print(newlist_2)