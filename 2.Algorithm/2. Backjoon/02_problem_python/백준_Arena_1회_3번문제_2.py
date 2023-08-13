# # BOJ.
# # 설계 의도: 조건에 맞는 실행
# # 개선점:
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def find_double(start, end, queue):
    if not queue:
        return "NO"
    elif queue and start > 0:
        pick = queue.popleft()
        if pick > 0:
            return "YES"
        elif pick == 0:
            flag = True
        else:
            flag = False
        while queue:
            pick = queue.popleft()
            if pick > 0:
                if flag:
                    return "YES"
                else:
                    flag = True
            elif pick == 0:
                pass
            else:
                flag = False
        return "NO"
    elif queue and end > 0:
        pick = queue.pop()
        if pick > 0:
            return "YES"
        elif pick == 0:
            flag = True
        else:
            flag = False
        while queue:
            pick = queue.pop()
            if pick > 0:
                if flag:
                    return "YES"
                else:
                    flag = True
            elif pick == 0:
                pass
            else:
                flag = False
        return "NO"



def angle_cut(start, end, queue):
    if not queue:
        return "NO"





def solution():
    N = int(input())
    num_list = deque(list(map(int, input().split())))
    if N == 1:
        if num_list.pop() > 0:
            return "YES"
        else:
            return "NO"
    else:
        start = num_list.popleft()
        end = num_list.pop()
        while num_list and start != 0 and end != 0:
            if num_list and start == 0:
                start = num_list.popleft()
            if num_list and end == 0:
                end = num_list.pop()
        if start * end == 0:
            return "YES" if start + end > 0 else "NO"

        if start > 0 and end > 0:
            return "YES"

        elif start * end < 0:
            return find_double(start, end, num_list)

        else:
            return angle_cut(start, end, num_list)


T = int(input())
for solve in range(T):
    print(solution())
