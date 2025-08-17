from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Number of Islands 문제 풀이 (BFS)

    - 입력 `grid`는 '1'은 땅, '0'은 물을 의미합니다.
    - 네 방향(상/하/좌/우)으로만 연결된 땅을 하나의 섬으로 계산합니다.
    - 방문한 땅은 '0'으로 마킹하여 재방문을 방지합니다. (입력 그리드를 변경합니다)
    """

    if not grid or not grid[0]:
        return 0

    n_rows = len(grid)
    n_cols = len(grid[0])

    # 네 방향 이동 벡터
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def _can_visit(x: int, y: int) -> bool:
        """그리드 범위 내이고, 아직 방문하지 않은 땅('1')인지 확인합니다."""
        return 0 <= x < n_rows and 0 <= y < n_cols and grid[x][y] == "1"

    def _bfs(start_x: int, start_y: int) -> None:
        # 시작 지점을 즉시 방문 처리하여 중복 방문을 방지합니다.
        grid[start_x][start_y] = "0"
        queue = deque([(start_x, start_y)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if _can_visit(nx, ny):
                    # 방문 표시를 큐에 넣는 시점에 수행하여 중복 삽입을 방지합니다.
                    grid[nx][ny] = "0"
                    queue.append((nx, ny))

    islands = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == "1":
                _bfs(row, col)
                islands += 1

    return islands


def _run_all_tests() -> None:
    """테이블 주도 테스트를 실행합니다."""
    import copy

    # 각 케이스는 입력과 기대 결과를 함께 정의합니다.
    test_cases = [
        {
            "name": "빈 그리드",
            "grid": [],
            "expected": 0,
        },
        {
            "name": "모두 물",
            "grid": [list("000"), list("000"), list("000")],
            "expected": 0,
        },
        {
            "name": "단일 섬",
            "grid": [list("111"), list("010"), list("111")],
            "expected": 1,
        },
        {
            "name": "세 개의 섬",
            "grid": [list("11000"), list("11000"), list("00100"), list("00011")],
            "expected": 3,
        },
        {
            "name": "단일 셀 섬",
            "grid": [list("0"), list("1")],
            "expected": 1,
        },
    ]

    for case in test_cases:
        # 입력 변형을 피하기 위해 깊은 복사 사용
        grid_copy = copy.deepcopy(case["grid"]) if case["grid"] else []
        result = num_islands(grid_copy)
        assert (
            result == case["expected"]
        ), f"[{case['name']}] expected={case['expected']}, got={result}"
        print(f"{case['name']} - PASSED")


if __name__ == "__main__":
    _run_all_tests()
