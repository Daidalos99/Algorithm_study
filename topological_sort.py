import random

def Topological_sort2(V, R):
    visited = []   # 딕셔너리에서 한번 방문한 원소를 넣을 리스트
    for v in V:
        if v not in visited:  # V의 원소 v를 방문하지 않았을 경우 DFS 실행
            DFS(v, V, R, visited)


def DFS(v, V, R, visited): # v에 대한 깊이중심탐색
    visited.append(v)    # V의 원소v를 방문 리스트에 추가
    if v == '계란 넣기':    # '계란 넣기'의 경우 향하는 노드가 없으므로, 위상정렬2 결과리스트에 '계란 넣기'추가 후 DFS종료
        R.insert(0, v)  # 리스트의 맨 앞에 값 삽입
        return
    else:
        for x in V[v]:  # v가 향하는 모든 노드 x에 대해 x를 아직 방문하지 않았을 경우, 깊이중심탐색 재귀
            if x not in visited:
                DFS(x, V, R, visited)
        R.insert(0, v)  # 결과 추가


if __name__ == '__main__':
    R = []  # 위상정렬2 결과리스트


    # 그래프를 딕셔너리 형태로 구현
    graph = {'냄비에 물 붓기': ['점화'], '점화': ['수프 넣기', '라면 넣기', '계란 넣기'],
             '라면 봉지 뜯기': ['라면 넣기', '수프 넣기'], '라면 넣기': ['계란 넣기'], '수프 넣기': ['계란 넣기']}


    # 그래프 딕셔너리를 셔플 후 graph2에 저장
    key_list = list(graph)
    random.shuffle(key_list)
    graph2 = {}
    for key in key_list:
        graph2[key] = graph[key]


    Topological_sort2(graph, R)  # 위상정렬2 함수
    print(R)    # 결과 출력