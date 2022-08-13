# import sys
# sys.stdin = open("sample_input.txt", "r")


first_box = list(map(int, input().split()))
second_box = list(map(int, input().split()))
third_box = list(map(int, input().split()))
fourth_box = list(map(int, input().split()))
board = [[0]*101 for _ in range(101)]
for dx in range(first_box)