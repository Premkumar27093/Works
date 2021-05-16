n = input()
p = int(input())
new2 = []
total = 0
i = 0
tup = n.split(",")
tup.sort(reverse=True)
for i in range(0, p):
    sum_ = int(tup[i])
    total = total + sum_
print(total)
