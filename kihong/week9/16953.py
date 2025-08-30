# 백준16593

"""
기본 아이디어
1) while a != b and a<b:
        if b가 2로 나누어떨어진다면:
            b를 2로 나누고, count += 1
        else b의 1의 자리수가 1이라면:
            b를 b의 10의 자리 숫자로 변경.
        else 그것도 아니라면
            break
    return a와 b가 같지 않다면 -1 , 같다면 count +1
2) 시간 복잡도 : log(b)이다. 왜나하면 b의 크기가 절반씩 지속적으로 떨어지는 if문과 정수 크기만큼 크기가 줄어드는 if문이 있기 때문입니다.
"""


def solve(a, b):
    count = 0
    while a != b and a < b:
        if b % 2 == 0:
            b = b // 2
            count += 1
        elif b % 10 == 1:
            b = (b - 1) // 10
            count += 1
        else:
            break
    return count + 1 if a == b else -1


def main():
    cases = [
        {"a": 2, "b": 162, "expected": 5},
        {"a": 4, "b": 42, "expected": -1},
        {"a": 100, "b": 40021, "expected": 5},
    ]
    for i, tc in enumerate(cases, 1):
        result = solve(tc["a"], tc["b"])
        assert tc["expected"] == result, (
            f"[{i}] 실패: " f"expected={tc['expected']}, actual_result={result}, "
        )
        print(f"test [{i}] 성공")


if __name__ == "__main__":
    main()
