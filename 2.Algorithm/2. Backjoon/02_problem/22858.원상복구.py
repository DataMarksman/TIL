# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

N, k = map(int, input().split())
cards = list(map(int, input().split()))
shuffle_idx = list(map(int, input().split()))

def shuffle(deck):
    new_deck = [0]*len(deck)
    for new_idx in range(len(shuffle_idx)):
        idx = shuffle_idx[new_idx] - 1
        new_deck[idx] = deck[new_idx]
    return new_deck

for repeat in range(k):
    cards = shuffle(cards)

print(*cards)