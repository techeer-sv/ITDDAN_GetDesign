def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, prev_temp = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))

    return ans


def test_basic_case():
    """기본적인 온도 변화 패턴을 테스트합니다."""
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    result = dailyTemperatures(temperatures)
    assert result == expected, f"기대값: {expected}, 실제값: {result}"
    print("기본 케이스 테스트 통과")


def test_decreasing_temperatures():
    temperatures = [30, 29, 28, 27]
    expected = [0, 0, 0, 0]
    result = dailyTemperatures(temperatures)
    assert result == expected, f"기대값: {expected}, 실제값: {result}"
    print("감소하는 온도 테스트 통과")


def test_increasing_temperatures():
    temperatures = [30, 31, 32, 33]
    expected = [1, 1, 1, 0]
    result = dailyTemperatures(temperatures)
    assert result == expected, f"기대값: {expected}, 실제값: {result}"
    print("증가하는 온도 테스트 통과")


def test_same_temperatures():
    temperatures = [30, 30, 30, 31]
    expected = [3, 2, 1, 0]
    result = dailyTemperatures(temperatures)
    assert result == expected, f"기대값: {expected}, 실제값: {result}"
    print("동일 온도 테스트 통과")


def test_single_temperature():
    temperatures = [30]
    expected = [0]
    result = dailyTemperatures(temperatures)
    assert result == expected, f"기대값: {expected}, 실제값: {result}"
    print("단일 온도 테스트 통과")


def run_all_tests():
    print("테스트 시작...")
    print("-" * 30)

    test_functions = [
        test_basic_case,
        test_decreasing_temperatures,
        test_increasing_temperatures,
        test_same_temperatures,
        test_single_temperature,
    ]

    for test in test_functions:
        try:
            test()
        except AssertionError as e:
            print(f"{test.__name__} 실패: {str(e)}")
            return False

    print("-" * 30)
    print("모든 테스트가 성공적으로 완료되었습니다!")
    return True


if __name__ == "__main__":
    run_all_tests()
