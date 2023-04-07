# 산타의 선물 공장 2

import math
import sys
input = sys.stdin.readline

q = int(input())
n_list = []

# 공장 설립
def one():
    n = int(cmd[1])
    m = int(cmd[2])

    global n_list
    n_list = [[] for _ in range(n+1)] # 벨트

    for i in range(3, len(cmd)):
        n_list[cmd[i]].append(i-2)

# 물건 모두 옮기기
def two():   
    if len(n_list[m_src]) == 0:
        pass
    else:
        n_list[m_dst] = n_list[m_src] + n_list[m_dst]
        n_list[m_src] = []

    print(len(n_list[m_dst]))   # m_dst의 선물의 총 수를 출력

# 앞 물건만 교체하기
def three():
    if len(n_list[m_src]) == 0 and len(n_list[m_dst]) == 0:
        pass
    elif len(n_list[m_src]) == 0:
        n_list[m_src].append(n_list[m_dst].pop(0))
    elif len(n_list[m_dst]) == 0:
        n_list[m_dst].append(n_list[m_src].pop(0))
    else:
    # m_src 가장 앞에 있는 선물과 m_dst 가장 앞에 있는 선물을 저장소에 저장 후 교체
        store = [n_list[m_src][0], n_list[m_dst][0]]
        m_src[0] = store[1]
        m_dst[0] = store[0]           

    print(len(n_list[m_dst]))

# 물건 나누기
def four():
    if len(n_list[m_src]) == 0:
        pass
    else:
        store = []
        for i in range(math.floor(len(n_list[m_src])/2)):
            store.append(n_list[m_src].pop(i))
        n_list[m_dst] = store + n_list[m_dst]

    print(len(n_list[m_dst]))

def five():
    for i in n_list:
        # p_num index 찾기
        if p_num in i:
            p_num_index = i.index(p_num)
        
            if p_num_index == 0:    # 앞 선물이 없는 경우
                a = -1
            else:
                a = i[p_num_index-1]
            
            if p_num_index == len(i) - 1:   # 뒤 선물이 없는 경우
                b = -1
            else:
                b = i[p_num_index+1]
    
    print(a + 2 * b)

def six():
    c = len(n_list[b_num])

    if c == 0:
        a = -1
        b = -1
    else:
        a = n_list[b_num][0]
        b = n_list[b_num][-1]
    
    print(a + 2*b + 3*c)

for _ in range(q):
    cmd = list(map(int, input().split()))   

    # 공장 설립
    if cmd[0] == 100:
        one()
        
    # 물건 모두 옮기기
    elif cmd[0] == 200:
        m_src = cmd[1]
        m_dst = cmd[2]
        two()
        
    # 앞 물건만 교체하기
    elif cmd[0] == 300:
        m_src = cmd[1]
        m_dst = cmd[2]
        three()

    # 물건 나누기
    elif cmd[0] == 400:
        m_src = cmd[1]
        m_dst = cmd[2]
        four()
          
    # 선물 정보 얻기
    elif cmd[0] == 500:
        p_num = cmd[1]
        five()
           
    # 벨트 정보 얻기
    elif cmd[0] == 600:
        b_num = cmd[1]
        six()
