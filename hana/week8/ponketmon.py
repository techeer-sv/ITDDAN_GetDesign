"""
폰켓몬 문제

당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다.
홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.

홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다.
따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다.

N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때,
N/2마리의 폰켓몬을 선택하는 방법 중 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아
그때의 폰켓몬 종류 번호의 개수를 return 해주세요.

제한사항:
- nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
- nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
- 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.

시간 복잡도: O(N) - set()
공간 복잡도: O(N) - set()에 최대 N개의 원소 저장
"""


def solution(nums):
    """
    1. 가져갈 수 있는 폰켓몬의 개수 계산 (N/2)
    2. 고유한 폰켓몬 종류의 개수 계산 (set 사용)
    3. 두 값 중 작은 값이 정답
        - select_count개만 가져갈 수 있음
        - unique_count개 종류가 있다면, 최대 unique_count개 종류를 가질 수 있음
        - 둘 중 작은 값이 실제로 가질 수 있는 최대 종류의 개수
    """
    # 가져갈 수 있는 폰켓몬의 개수 (N/2)
    select_count = len(nums) // 2

    # 폰켓몬 종류의 개수 (중복 제거)
    unique_count = len(set(nums))

    # 가져갈 수 있는 폰켓몬의 개수와 고유한 폰켓몬 종류의 개수 중 작은 값이 정답
    return min(select_count, unique_count)


def test_solution() -> None:
    """solution 함수의 테스트를 실행합니다."""

    # 테스트 케이스 테이블
    test_cases = [
        {
            "nums": [3, 1, 2, 3],
            "expected": 2,
            "description": "기본 예시 케이스 - 4마리 중 2마리 선택, 최대 2종류",
        },
        {
            "nums": [3, 3, 3, 2, 2, 4],
            "expected": 3,
            "description": "6마리 중 3마리 선택, 최대 3종류",
        },
        {
            "nums": [3, 3, 3, 2, 2, 2],
            "expected": 2,
            "description": "6마리 중 3마리 선택, 최대 2종류 (고유 종류가 2개뿐)",
        },
        {
            "nums": [1, 2, 3, 4, 5, 6],
            "expected": 3,
            "description": "6마리 중 3마리 선택, 최대 3종류 (모든 종류가 다름)",
        },
        {
            "nums": [1, 1],
            "expected": 1,
            "description": "2마리 중 1마리 선택, 최대 1종류",
        },
        {
            "nums": [1, 2, 3, 4],
            "expected": 2,
            "description": "4마리 중 2마리 선택, 최대 2종류",
        },
        {
            "nums": [1, 1, 1, 1, 1, 1],
            "expected": 1,
            "description": "6마리 중 3마리 선택, 최대 1종류 (모든 종류가 동일)",
        },
        {
            "nums": [1, 2, 3, 4, 5, 6, 7, 8],
            "expected": 4,
            "description": "8마리 중 4마리 선택, 최대 4종류",
        },
    ]

    # 테스트 실행
    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        result = solution(nums)

        print(f"테스트 {i} - {description}")
        print(f"  입력: {nums}")
        print(f"  결과: {result}, 기대값: {expected}")

        assert result == expected, f"기대값 {expected}, 실제값 {result}"
        print("  통과\n")

    print("모든 테스트 케이스 통과!")


if __name__ == "__main__":
    test_solution()
