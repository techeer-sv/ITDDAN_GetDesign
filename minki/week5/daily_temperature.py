def _is_warmer_day_exists(stack, current_temp):
    """현재 온도가 스택의 최상단 온도보다 높은지 확인합니다."""
    return stack and stack[-1][1] < current_temp


def daily_temperatures(temperatures):
    """각 날짜별로 더 따뜻한 날씨가 오기까지 기다려야 하는 일수를 계산합니다.

    Args:
        temperatures: 일별 온도를 담은 리스트

    Returns:
        각 날짜별로 더 따뜻한 날씨가 오기까지 기다려야 하는 일수를 담은 리스트
        더 따뜻한 날이 없는 경우 0을 반환
    """
    # 결과를 저장할 리스트 초기화 (기본값 0)
    ans = [0] * len(temperatures)
    # (날짜, 온도)를 저장할 스택
    stack = []

    # 현재 날짜와 온도를 순회
    for cur_day, cur_temp in enumerate(temperatures):
        # 스택에 있는 이전 날짜의 온도가 현재 온도보다 낮다면 계속 처리
        while _is_warmer_day_exists(stack, cur_temp):
            prev_day, prev_temp = stack.pop()
            # 더 따뜻한 날을 찾았으므로, 해당 날짜까지의 대기 일수를 계산
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))

    return ans


def run_all_tests():
    """Table Driven Test 방식으로 모든 테스트 케이스를 실행합니다."""
    print("테스트 시작...")
    print("-" * 30)
    # 테스트 케이스 테이블 정의
    test_cases = [
        {
            "name": "기본 케이스",
            "input": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0],
            "description": "기본적인 온도 변화 패턴",
        },
        {
            "name": "감소하는 온도",
            "input": [30, 29, 28, 27],
            "expected": [0, 0, 0, 0],
            "description": "연속해서 감소하는 온도 패턴",
        },
        {
            "name": "증가하는 온도",
            "input": [30, 31, 32, 33],
            "expected": [1, 1, 1, 0],
            "description": "연속해서 증가하는 온도 패턴",
        },
        {
            "name": "동일 온도",
            "input": [30, 30, 30, 31],
            "expected": [3, 2, 1, 0],
            "description": "연속된 동일 온도 후 상승하는 패턴",
        },
        {
            "name": "단일 온도",
            "input": [30],
            "expected": [0],
            "description": "하나의 온도만 있는 경우",
        },
    ]

    # 각 테스트 케이스 실행
    for test_case in test_cases:
        try:
            result = daily_temperatures(test_case["input"])
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
