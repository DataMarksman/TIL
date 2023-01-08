# PRG.

# 설계 의도: 최대한 적은 횟수만큼 보자.

# 로직의 Main 개념: 데큐
# [Tip!] 손님이 가장 많이 있을 수 있는 시간은, 새로운 손님이 들어올 때 뿐이다.

# 개선점:

# 연산 효율화를 위해 데큐를 사용하자. pop을 하기 위한 연산이 O(1) 이다.
# [Tip!] 빅오 연산(시간) 효율화에 대해 알아보자
from collections import deque


def solution(menu, order, k):
    answer = 0

    # 남아있는 손님들 명단을 저장해 놓을 데큐 리스트이다.
    left_order = deque()

    # 손님이 가장 많이 있을 수 있는 시간은 손님이 들어올 때 뿐이고, 이후 점차 감소하므로 손님 수만큼만 탐색하면 된다.

    # 자, 장사를 시작하겠습니다.
    for turn in range(len(order)):

        # 손님 리스트에, 이번에 들어온 손님에게 드릴 메뉴를 위해 걸리는 시간을 넣어줍니다.
        left_order.append(menu[order[turn]])

        # 지금 방금 오신 손님도, 메뉴가 만들어질 때 까지는 기다리셔야 하므로, 들어오셨을 때, 대기 인원을 체크해줍니다.
        answer = max(len(left_order), answer)

        # 매 턴, 즉 다음 손님이 오시기 전까지 k 만큼의 시간이 주어집니다.
        time = int(k)

        # 아직 손님이 남아계시고, 시간도 있다면 계속 진행할 반복문을 설정해줍니다.
        while left_order:
            # 지금 가장 앞에서 대기하고 계신 손님을 불러옵니다.
            pick = left_order.popleft()

            # 손님의 메뉴가 만들어질 때까지 남은 시간을 계산하고
            if pick > time:
                # 메뉴를 만들기 위해 남은 시간이, 현재 주어진 시간보다 크다면,
                # 메뉴 시간에서 주어진 시간을 차감하고 다시 Q에 넣어준다음
                # break 로 반복문을 깨고 다음 턴으로 넘어갑니다.
                pick -= time
                left_order.appendleft(pick)
                break

            # 이번 메뉴를 만들기 위해 남은 시간이 주어진 시간과 같다면, 그냥 break 해줍니다.
            elif pick == time:
                break

            # 주어진 시간동안 이번 메뉴를 다 만들었다면 반복문으로 돌아가서 다음 메뉴를 준비합니다.
            else:
                time -= pick

    return answer