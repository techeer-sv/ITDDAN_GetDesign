# 백준 2252번 줄 세우기 - 위상정렬 알고리즘 사용
import sys
from collections import defaultdict, deque
from io import StringIO


def topo_sort(n: int, graph, in_degree):
    """
    Kahn 알고리즘을 이용해 위상정렬을 수행한다.
    """
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    result = []
    while q:
        cur = q.popleft()
        result.append(cur)
        for nxt in graph[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    return result


def _solve(input_str):

    sys.stdin = StringIO(input_str)

    try:
        n, m = map(int, sys.stdin.readline().split())
    except ValueError:
        return "Invalid input format"

    graph = defaultdict(list)

    in_degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        # 무엇에 연결되어 있는지 기록
        graph[a].append(b)
        # 진입 차수 기록
        in_degree[b] += 1
    order = topo_sort(n, graph, in_degree)
    return " ".join(map(str, order))


def _run_all_tests() -> None:
    """테이블 주도 테스트를 실행합니다."""
    test_cases = [
        {
            "name": "예제 입력 1",
            "input": "3 2\n1 3\n2 3",
            "expected_output": "1 2 3",
        },
        {
            "name": "예제 입력 2",
            "input": "4 2\n4 2\n3 1",
            "expected_output": "3 4 1 2",
        },
    ]

    """ 테스트 케이스를 순환하여 결과를 검증. """
    for case in test_cases:
        result = _solve(case["input"])
        assert result.replace(" ", "") == case["expected_output"].replace(
            " ", ""
        ), f"[{case['name']}] expected={case['expected_output']}, got={result}"
        print(f"{case['name']} - PASSED")


if __name__ == "__main__":
    _run_all_tests()
