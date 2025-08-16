# 백준 2252번 줄 세우기 - 위상정렬 알고리즘 사용
from collections import deque, defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 무엇에 연결되어 있는지 기록
    graph[a].append(b)
    # 진입 차수 기록
    in_degree[b] += 1

q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
result = []
while q:
    idx = q.popleft()
    result.append(idx)
    for next_item in graph[idx]:
        in_degree[next_item] -= 1  # 해당 노드에서 나가는 간선 제거
        if in_degree[next_item] == 0:
            q.append(next_item)
print(*result)
