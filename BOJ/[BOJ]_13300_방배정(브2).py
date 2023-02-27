'''
1. 학년별 인덱스에 따른 빈 방 만들어 주기
2. 학년과 반 인덱스가 같다면 해당 리스트에 성별 정보 넣어주기
3. 방별 리스트를 순회하면서 최대 배정 인원에 따라 방 늘리기
4. 만약 최대 배정 인원에 나누어 떨어지면 그 몫을, 아니라면 몫 + 1
'''
N,K = map(int,input().split()) # 학생 수, 최대 배정 인원
room = [[] for _ in range(7)]   # 학년 별 인덱스에 따른 방 생성

for _ in range(N):
    S, Y = map(int,input().split()) # 성별, 학년
    for i in range(7):
        if i == Y:
            room[i].append(S)   # 학년 별로 한 반에 넣기

girl, boy, cnt = 0,0,0

for lst in room:
    # 여학생 방 세기
    girl = lst.count(0)
    cnt += girl//K + 1 if girl%K else girl//K

    # 남학생 방 세기
    boy = lst.count(1)
    cnt += boy//K + 1 if boy%K else boy//K

print(cnt)






