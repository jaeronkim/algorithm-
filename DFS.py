#DFS(deep first seaerch)->최단경로 찾기에 이용되는 알고리즘. 하나의 노드에서 시작하여 가능한 모든 방향으로 하나씩 나아가서 목표지점에 도착하면 종료하는 알고리즘

#구현에 필요한 요소->1.재귀 함수 2. 덱(선입 선출 방식의 자료구조)

#https://school.programmers.co.kr/learn/courses/30/lessons/159993->문제 링크

from collections import deque
# 해당 방향으로 가도 되는지 확인
#파라미터->(현재y,현재x,경계y,경계x,지도)
def is_valid_move(ny,nx,n,m,maps):
    return 0<=ny<n and 0<=nx<m and maps[ny][nx]!="X"
#왔던 곳인지 확인->이때 레버를 당겼을때(k=1)와 당기지 않았을 때(k=1)구분 
#파라미터->(현재y,현재x,레버 당김 여부,이동 횟수,방문여부를 확인하는 지도,이동할 곳을 저장하는 곳)
def  append_to_queue(ny,nx,k,time,visited,q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k]=True
        q.append((ny,nx,k,time+1))

def solution(maps):
    n,m=len(maps),len(maps[0])
    visited=[[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]#지도에서 방문한 곳을 적는 곳(레버 당김 여부를 구분)

#dy,dx를 통해 사방을 한번씩 확인
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    q=deque()#선입선출 알고리즘을 사용할 것이기에
    end_y,end_x=-1,-1

#시작 위치와 끝나는 위치 확인
    for i in range(n):
        for j in range(m):
            if maps[i][j]=="S":
                q.append((i,j,0,0))
                visited[i][j][0]=True
            elif maps[i][j]=='E':
                end_y,end_x=i,j

    while q:
        y,x,k,time=q.popleft()
        if y==end_y and x==end_x and k==1:#타겟지점,레버를 당긴 상태로 도착하면 끝
            return time

        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if not is_valid_move(ny,nx,n,m,maps):# 해당방향으로 못가면 다른 방향 확인
                continue
            if maps[ny][nx]=="L":#레버를 만나면 k=1로 전환
                append_to_queue(ny,nx,1,time,visited,q)
            else:#O를 만나면 해당 방향으로 진행
                append_to_queue(ny,nx,k,time,visited,q)
    return -1#다 돌았는데 타겟지점에 레버를 당긴 상태로 도착하지 않으면 반환

maps=["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]	

print(solution(maps))