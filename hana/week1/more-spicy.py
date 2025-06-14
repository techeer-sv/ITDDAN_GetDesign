"""
프로그래머스 42626. 더 맵게 - Python

Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 구하기

- 제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

시간 복잡도 O(n logn)
"""

import heapq


def solution(scoville: list[int], K: int) -> int:
    """스코빌 지수를 K 이상으로 만들기 위한 최소 섞는 횟수를 반환합니다.

    Args:
        scoville (list[int]): 음식의 스코빌 지수 배열
        K (int): 목표 스코빌 지수

    Returns:
        int: 최소 섞는 횟수, 불가능한 경우 -1
    """
    heapq.heapify(scoville)  # 최소힙 구조로 오름차순 정렬 O(n)
    answer = 0
    while len(scoville) >= 2 and scoville[0] < K:  # 최악의 경우 n-1번
        first = heapq.heappop(scoville)  # O(log n)
        second = heapq.heappop(scoville)  # O(log n)
        new_score = first + second * 2  # 1, 2번째로 맵지 않은 원소 꺼내서 섞기

        heapq.heappush(scoville, new_score)  # 최소힙 원소 추가 O(log n)
        answer += 1

    if scoville[0] < K:
        return -1  # 한 개 남아서 K 이상으로 만들 수 없음

    return answer


def test_solution() -> None:
    """solution 함수의 테스트를 실행합니다."""
    # 테스트 1: 기본 케이스
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    result = solution(scoville, K)
    expected = 2
    print(f"테스트 1 - 입력: {scoville}, K: {K}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 2: 불가능한 케이스
    scoville = [1, 1, 1]
    K = 10
    result = solution(scoville, K)
    expected = -1
    print(f"테스트 2 - 입력: {scoville}, K: {K}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 3: 이미 K 이상인 케이스
    scoville = [7, 8, 9]
    K = 5
    result = solution(scoville, K)
    expected = 0
    print(f"테스트 3 - 입력: {scoville}, K: {K}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    print("✅ 모든 테스트 케이스 통과!")


if __name__ == "__main__":
    test_solution()

