def _can_afford(budget, cost):
    """예산이 해당 비용을 감당할 수 있는지 확인합니다."""
    return budget - cost >= 0


def budget_solution(d, budget):
    """최대 몇 개의 부서를 지원할 수 있는지 계산합니다.
    Args:
        d: 각 부서별 신청 금액 리스트
        budget: 총 예산
    Returns:
        지원 가능한 부서의 최대 개수
    """
    answer = 0
    d.sort()
    for cost in d:
        # 예산이 남아있는지 확인
        if _can_afford(budget, cost):
            answer += 1
            budget -= cost
        else:
            break
    return answer


def run_all_tests():
    """Table Driven Test 방식으로 budget_solution 테스트 케이스를 실행합니다."""
    print("테스트 시작...")
    print("-" * 30)

    test_cases = [
        {
            "name": "기본 케이스",
            "input": {"d": [1, 3, 2, 5, 4], "budget": 9},
            "expected": 3,
            "description": "예산 내에서 최대한 많은 부서를 지원하는 기본 케이스",
        },
        {
            "name": "모든 부서 지원 가능",
            "input": {"d": [2, 2, 2, 2], "budget": 10},
            "expected": 4,
            "description": "모든 부서를 예산 내에서 지원 가능",
        },
        {
            "name": "한 부서도 지원 불가",
            "input": {"d": [10, 20, 30], "budget": 5},
            "expected": 0,
            "description": "예산이 너무 적어 한 부서도 지원 불가",
        },
        {
            "name": "예산과 동일한 부서 비용",
            "input": {"d": [5, 10, 15], "budget": 10},
            "expected": 1,
            "description": "예산과 정확히 일치하는 부서만 지원 가능",
        },
        {
            "name": "부서가 하나",
            "input": {"d": [7], "budget": 7},
            "expected": 1,
            "description": "부서가 하나이고 예산이 딱 맞는 경우",
        },
        {
            "name": "부서가 하나, 예산 부족",
            "input": {"d": [8], "budget": 7},
            "expected": 0,
            "description": "부서가 하나지만 예산이 부족한 경우",
        },
    ]

    for test_case in test_cases:
        try:
            result = budget_solution(**test_case["input"])
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
