import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  stick_len, ants = map(int, input().split())

  max_time = []
  min_time = []
  for _ in range(ants):
    loc = int(input())
    min_time.append(min(loc, stick_len - loc))
    max_time.append(max(loc, stick_len - loc))

  print(max(min_time), max(max_time))
