"""
전화번호부 접두사 확인 문제

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
예시: 구조대(119)는 지영석(1195524421)의 접두사

제한사항:
- phone_book의 길이는 1 이상 1,000,000 이하
- 각 전화번호의 길이는 1 이상 20 이하
- 같은 전화번호가 중복해서 들어있지 않음

해결 방법:
정렬 후 인접한 번호 비교

점두어가 되는 문자열은 정렬했을 때 앞쪽에 위치하게 됨
=> 바로 옆 번호만 비교하면 됨

startswith(): 어떤 문자열이 특정 접두사로 시작하는지 확인

시간 복잡도: O(nlogn)
- 정렬: O(nlogn)
- 비교: O(n)
"""


def solution(phone_book):
    # 전화번호 정렬
    phone_book.sort()  # O(nlogn)

    # 인접한 두 번호 비교
    for i in range(len(phone_book) - 1):  # O(n)
        # 현재 번호가 다음 번호의 접두사인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


def test_solution() -> None:
    """solution 함수의 테스트를 실행합니다."""

    # 테스트 1: 기본 케이스 - 접두사가 있는 경우
    phone_book = ["119", "97674223", "1195524421"]
    result = solution(phone_book)
    expected = False  # 119가 1195524421의 접두사
    print(f"테스트 1 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 2: 접두사가 없는 경우
    phone_book = ["123", "456", "789"]
    result = solution(phone_book)
    expected = True  # 접두사 관계 없음
    print(f"테스트 2 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 3: 한 자리 번호가 다른 번호의 접두사인 경우
    phone_book = ["12", "123", "1235", "567", "88"]
    result = solution(phone_book)
    expected = False  # 12가 123의 접두사, 123이 1235의 접두사
    print(f"테스트 3 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 4: 단일 번호
    phone_book = ["123"]
    result = solution(phone_book)
    expected = True  # 비교할 다른 번호가 없음
    print(f"테스트 4 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 5: 같은 길이의 번호들
    phone_book = ["123", "456", "789", "012"]
    result = solution(phone_book)
    expected = True  # 같은 길이는 접두사 관계가 될 수 없음
    print(f"테스트 5 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 6: 복잡한 케이스
    phone_book = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    result = solution(phone_book)
    expected = False  # 1이 10의 접두사
    print(f"테스트 6 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    # 테스트 7: 정렬 후 접두사가 뒤에 오는 경우
    phone_book = ["123", "1234", "12345", "567", "5678"]
    result = solution(phone_book)
    expected = False  # 123이 1234의 접두사, 1234가 12345의 접두사, 567이 5678의 접두사
    print(f"테스트 7 - phone_book: {phone_book}")
    print(f"결과: {result}, 기대값: {expected}")
    assert result == expected, f"기대값 {expected}, 실제값 {result}"

    print("✅ 모든 테스트 케이스 통과!")


if __name__ == "__main__":
    test_solution()
