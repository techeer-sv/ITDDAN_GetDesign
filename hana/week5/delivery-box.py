"""
택배 상자 꺼내기 문제

1 ~ n의 번호가 있는 택배 상자가 창고에 있습니다. 당신은 택배 상자들을 다음과 같이 정리했습니다.

왼쪽에서 오른쪽으로 가면서 1번 상자부터 번호 순서대로 택배 상자를 한 개씩 놓습니다.
가로로 택배 상자를 w개 놓았다면 이번에는 오른쪽에서 왼쪽으로 가면서 그 위층에 택배 상자를 한 개씩 놓습니다.
그 층에 상자를 w개 놓아 가장 왼쪽으로 돌아왔다면 또다시 왼쪽에서 오른쪽으로 가면서 그 위층에 상자를 놓습니다.
이러한 방식으로 n개의 택배 상자를 모두 놓을 때까지 한 층에 w개씩 상자를 쌓습니다.

택배 상자 A를 꺼내려면 먼저 A 위에 있는 다른 모든 상자를 꺼내야 A를 꺼낼 수 있습니다.

제한사항:
- 2 ≤ n ≤ 100
- 1 ≤ w ≤ 10
- 1 ≤ num ≤ n

시간 복잡도: O(총 층 수)
"""


def solution(n, w, num):
    """
    층이 홀수면 왼->오
    짝수면 오->왼
    인덱스는 모두 0부터 시작
    """

    row = (num - 1) // w  # 0-indexed 행 번호
    col = (num - 1) % w  # 기본 열 번호

    # 짝수번째 줄은 좌 → 우, 홀수번째 줄은 우 → 좌
    if row % 2 == 1:
        col = w - 1 - col

    # 총 몇 층이 있는지
    total_rows = (n - 1) // w + 1

    count = 1  # 꺼내려는 상자 포함

    for r in range(row + 1, total_rows):
        # 해당 행이 마지막 행일 경우 남은 개수만큼만 상자가 있음
        boxes_in_row = w if (r + 1) * w <= n else n - r * w

        # 지그재그 정렬에 따라 현재 행의 열 계산
        if r % 2 == 0:
            # 왼→오 방향
            if col < boxes_in_row:
                count += 1
        else:
            # 오→왼 방향
            if (w - 1 - col) < boxes_in_row:
                count += 1

    return count


def test_solution() -> None:
    """solution 함수의 테스트를 실행합니다."""

    # 테스트 1: 기본 케이스 - 첫 번째 층의 첫 번째 상자
    # n=6, w=3인 경우: 1층(1,2,3), 2층(6,5,4)
    # 1번 상자를 꺼내려면 6번과 1번을 꺼내야 함 = 2개
    n, w, num = 6, 3, 1
    result = solution(n, w, num)
    expected = 2  # 1번, 6번 상자
    print(f"테스트 1 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 2: 예시 케이스 - w=6, n=22, num=8 (8번 상자 위에 17번, 20번이 있음)
    n, w, num = 22, 6, 8
    result = solution(n, w, num)
    expected = 3  # 8번, 17번, 20번 상자
    print(f"테스트 2 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 3: 첫 번째 층 마지막 상자
    # n=10, w=5인 경우: 1층(1,2,3,4,5), 2층(10,9,8,7,6)
    # 5번 상자를 꺼내려면 6번과 5번을 꺼내야 함 = 2개
    n, w, num = 10, 5, 5
    result = solution(n, w, num)
    expected = 2  # 5번, 6번 상자
    print(f"테스트 3 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 4: 두 번째 층 첫 번째 상자 (오른쪽에서 시작)
    # n=10, w=5인 경우: 1층(1,2,3,4,5), 2층(10,9,8,7,6)
    # 6번 상자는 최상층이므로 1개만
    n, w, num = 10, 5, 6
    result = solution(n, w, num)
    expected = 1  # 6번 상자만
    print(f"테스트 4 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 5: 마지막 층의 마지막 상자
    n, w, num = 10, 3, 10
    result = solution(n, w, num)
    expected = 1  # 10번 상자만 (최상단)
    print(f"테스트 5 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 6: w=1인 경우 (세로로만 쌓임)
    # n=5, w=1인 경우: 1층(1), 2층(2), 3층(3), 4층(4), 5층(5)
    # 3번 상자를 꺼내려면 5번, 4번, 3번을 꺼내야 함 = 3개
    n, w, num = 5, 1, 3
    result = solution(n, w, num)
    expected = 3  # 3번, 4번, 5번 상자
    print(f"테스트 6 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 7: 정확히 한 층만 있는 경우
    n, w, num = 3, 5, 2
    result = solution(n, w, num)
    expected = 1  # 2번 상자만
    print(f"테스트 7 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 8: 복잡한 케이스
    # n=15, w=4인 경우: 1층(1,2,3,4), 2층(8,7,6,5), 3층(9,10,11,12), 4층(15,14,13)
    # 7번 상자를 꺼내려면 14번, 10번, 7번을 꺼내야 함 = 3개
    n, w, num = 15, 4, 7
    result = solution(n, w, num)
    expected = 3  # 7번, 10번, 14번 상자
    print(f"테스트 8 - n={n}, w={w}, num={num}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    print("✅ 모든 테스트 케이스 통과!")


if __name__ == "__main__":
    test_solution()
