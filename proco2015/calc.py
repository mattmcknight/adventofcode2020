z = int(input())
texts = []
for y in range(z):
    texts.append(input())
sum = 0
n = len(texts)-1
while n >= 0:
    if texts[n].strip() == '+':
        sum += 1
    elif texts[n].strip() == '-':
        sum -= 1
    else:
        n -= int(texts[n].strip().split(" ")[1])
    n -= 1
print(sum)




