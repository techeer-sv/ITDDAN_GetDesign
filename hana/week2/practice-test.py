"""
프로그래머스 42840. 모의고사 - Python

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성하기

- 제한 사항
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

시간 복잡도 O(n)
"""


def solution(answers):
    # 찍는 방식 정의
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_score = b_score = c_score = 0

    # 채점하기
    for index, item in enumerate(answers):  # O(n)
        if item == a[index % 5]:
            a_score += 1
        if item == b[index % 8]:
            b_score += 1
        if item == c[index % 10]:
            c_score += 1

    # 최고 점수 구하기
    scores = [a_score, b_score, c_score]
    max_score = max(scores)  # 고정 리스트기 때문에 O(1)

    # 최고 점수를 받은 사람 찾기
    answer = []
    for index, item in enumerate(scores):
        if item == max_score:
            answer.append(index + 1)

    return answer


def test_solution() -> None:
    """solution 함수의 테스트를 실행합니다."""
    # 테스트 1: 기본 케이스 - 1번이 가장 많이 맞힌 경우
    answers = [1, 2, 3, 4, 5]
    result = solution(answers)
    expected = [1]
    print(f"테스트 1 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 2: 예제 케이스
    answers = [1, 3, 2, 4, 2]
    result = solution(answers)
    expected = [1, 2, 3]
    print(f"테스트 2 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 3: 2번이 가장 많이 맞힌 경우
    answers = [2, 1, 2, 3, 2, 4, 2, 5]
    result = solution(answers)
    expected = [2]
    print(f"테스트 3 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 4: 3번이 가장 많이 맞힌 경우
    answers = [1, 3, 1, 3, 1]
    result = solution(answers)
    expected = [3]
    print(f"테스트 4 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 5: 1번이 가장 많이 맞힌 경우
    answers = [1, 2, 5, 5, 5]
    result = solution(answers)
    expected = [1]
    print(f"테스트 5 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 6: 3번이 가장 많이 맞힌 경우 (패턴 완전 일치)
    answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = solution(answers)
    expected = [3]
    print(f"테스트 6 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 7: 긴 배열 테스트 (패턴 반복)
    answers = [1, 2, 3, 4, 5] * 3  # 15개 문제
    result = solution(answers)
    expected = [1]
    print(f"테스트 7 - 입력: {answers}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    print("✅ 모든 테스트 케이스 통과!")


if __name__ == "__main__":
    test_solution()
