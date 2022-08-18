case = int(input()) # 전체 케이스 선언 
for i in range(case): # 전체 케이스 만큼 돌리기
    count = int(input()) # 케이스 별 요소 수 선언
    for j in range(count):
       future_list = list(map(int,input().split()))
       answer_list = []
       while_con = True
       while while_con == True:
              answer_stack = int(0)
              max_num = max(future_list)
              max_po = future_list.index(max_num)
              answer_list = future_list[:int(max_po)]
              if answer_list == future_list[0]:
                     while_con = False
              else:
                     del future_list[:int(max_po)]
                     answer_list





       print(f'#{i+1}')


