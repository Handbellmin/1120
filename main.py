import sys

input = sys.stdin.readline

str1, str2 = input().split(' ')
str2 = str2.rstrip()
d = len(str2) - len(str1)
cnt = 0
m = 999999
n = 0
while 1:
  for i in range(len(str1)):
    if str1[i] != str2[n:len(str2) - d + n][i]:
      cnt += 1
  if cnt < m:
    m = cnt
  cnt = 0
  n += 1
  if n > d:
    break
print(m)
