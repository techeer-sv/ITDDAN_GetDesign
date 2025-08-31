from collections import deque
from typing import List


def solution(maps: List[List[int]]) -> int:
    """
    게임 맵 최단거리 문제 풀이 (BFS)

    - maps: n x m 크기의 게임 맵 (n, m은 1~100)
    - 0: 벽, 1: 통로
    - 시작점: (1,1) -> 인덱스로는 (0,0)
    - 도착점: (n,m) -> 인덱스로는 (n-1,m-1)
    - n과 m이 모두 1인 경우는 입력으로 주어지지 않음
    - 반환값: 최단거리, 도달 불가능하면 -1
    """
    N = len(maps)
    M = len(maps[0])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()

    # 시작점이 벽인 경우 도달 불가능
    if maps[0][0] == 0:
        return -1

    # 시작점을 방문 표시 및 거리 설정
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    # 도착점이 벽이거나 방문하지 못한 경우
    if maps[N - 1][M - 1] == 0 or maps[N - 1][M - 1] == 1:
        return -1

    return maps[N - 1][M - 1]


def _run_all_tests() -> None:
    """테이블 주도 테스트를 실행합니다."""

    # 각 케이스는 입력과 기대 결과를 함께 정의합니다.
    test_cases = [
        {
            "name": "기본 케이스 - 3x3 맵",
            "maps": [[1, 0, 1], [1, 0, 1], [1, 1, 1]],
            "expected": 5,
        },
        {
            "name": "도달 불가능한 케이스",
            "maps": [[1, 0, 0], [0, 0, 0], [0, 0, 1]],
            "expected": -1,
        },
        {
            "name": "직선 경로",
            "maps": [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
            "expected": 5,
        },
        {
            "name": "시작점이 벽인 케이스",
            "maps": [[0, 1], [1, 1]],
            "expected": -1,
        },
        {
            "name": "도착점이 벽인 케이스",
            "maps": [[1, 1], [1, 0]],
            "expected": -1,
        },
        {
            "name": "큰 맵 케이스",
            "maps": [
                [1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1],
            ],
            "expected": 9,
        },
        {
            "name": "모든 경로가 막힌 케이스",
            "maps": [[1, 0], [0, 1]],
            "expected": -1,
        },
    ]

    for case in test_cases:
        # maps가 수정되므로 테스트마다 새로 생성
        test_map = [row[:] for row in case["maps"]]
        result = solution(test_map)
        assert (
            result == case["expected"]
        ), f"[{case['name']}] expected={case['expected']}, got={result}"
        print(f"{case['name']} - PASSED")


if __name__ == "__main__":
    _run_all_tests()
