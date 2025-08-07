from collections import deque


def get_stock_price(prices):
    answer = []
    prices = deque(prices)
    while prices:
        count = 0
        price = prices.popleft()
        for p in prices:
            count += 1
            if price > p:
                break
        answer.append(count)
    return answer


def run_all_tests():
    """Table Driven Test 방식으로 get_stock_price 테스트 케이스를 실행합니다."""
    print("테스트 시작...")
    print("-" * 30)

    test_cases = [
        {
            "name": "기본 케이스",
            "input": {"prices": [1, 2, 3, 2, 3]},
            "expected": [4, 3, 1, 1, 0],
            "description": "주가가 오르거나 유지되다가 떨어질 때까지의 시간",
        },
        {
            "name": "계속 상승하는 경우",
            "input": {"prices": [1, 2, 3, 4, 5]},
            "expected": [4, 3, 2, 1, 0],
            "description": "끝까지 주가가 오르는 경우",
        },
        {
            "name": "계속 하락하는 경우",
            "input": {"prices": [5, 4, 3, 2, 1]},
            "expected": [1, 1, 1, 1, 0],
            "description": "즉시 하락하는 경우",
        },
        {
            "name": "모두 같은 가격",
            "input": {"prices": [3, 3, 3, 3]},
            "expected": [3, 2, 1, 0],
            "description": "주가가 동일하게 유지되는 경우",
        },
        {
            "name": "하나만 있는 경우",
            "input": {"prices": [5]},
            "expected": [0],
            "description": "리스트에 한 개의 값만 존재할 때",
        },
    ]

    for test_case in test_cases:
        try:
            result = get_stock_price(**test_case["input"])
            assert result == test_case["expected"], (
                f"{test_case['name']} 실패\n"
                f"입력값: {test_case['input']}\n"
                f"기대값: {test_case['expected']}\n"
                f"실제값: {result}"
            )
            print(f"{test_case['name']} 테스트 통과")
        except AssertionError as e:
            print(f"테스트 실패: {str(e)}")
            return False

    print("-" * 30)
    print("모든 테스트가 성공적으로 완료되었습니다!")
    return True


if __name__ == "__main__":
    run_all_tests()
