# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:


N = int(input())
target = N+1

# 소수 상근수를 저장해놓을 리스트
prime_list = []

# 루프를 도는 visited 저장용
visited = set()

# 소수 상근수로 들어오는 visited를 저장해놓는 리스트
happy_visited = set()

prime_set = set(i for i in range(2, target))
for check in range(2, target):
    current = int(check)
    if current not in prime_set:
        continue
    else:
        # 이번 차수를 위한 임시 visited인 semi_visited를 만든다.
        semi_visited = set()

        # 초기 세팅으로 next_num과 num_list를 만들어준다.
        next_num = int(check)
        num_list = list(str(next_num))

        # while 문을 돌면서 현재 수가 소수 상근수 인지 체크해준다.
        while True:
            next_num = 0
            for numbers in num_list:
                next_num += int(numbers)**2

            # 1로 가면 소수 상근수다.
            # 그리고 1로 접근했던 visited와 같은 수가 있다면 결국 1로 간다.
            if next_num == 1 or next_num in happy_visited:
                happy_visited |= semi_visited
                prime_list.append(check)
                break

            # 루프를 돌면 소수 상근수가 될 수 없다
            # 마찬가지로 루프를 도는 visited에 해당하는 수가 있다면 루프를 돈다.
            elif next_num in semi_visited or next_num in visited:
                visited |= semi_visited
                break

            # 다음 차수를 위해서 semi_visited에 현재 숫자를 넣어주고 num_list를 만들어준다.
            semi_visited.add(next_num)
            num_list = list(str(next_num))

        # 다음 소수를 찾는 로직이다.
        while current < target:
            # 현재 수의 배수를 prime_set 에서 찾아서 지워준다.
            current += check
            if current in prime_set:
                prime_set.remove(current)

# 소수 상근수 리스트를 순회하면서 목표 수보다 작으면 프린트 한다.
for printing in prime_list:
    if printing <= N:
        print(printing)
    else:
        break
