'''
x = num

num = int(input())
'''

'''
for x in range(0,11):
  if x > 1:
    for i in range(2, x):
      if (x % i) == 0:
        break
    else:
      print(x)
'''


for x in range(0,1001):
  if x > 1:
    for i in range(2, x):
      if (x % i) == 0:
        break
    else:
      print(x, end=" ")


'''
commentary for commit test
'''
