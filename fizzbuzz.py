"""
FizzBuzz - Python
1부터 n까지 숫자를 출력하되:
- 3의 배수면 "Fizz"
- 5의 배수면 "Buzz"  
- 15의 배수면 "FizzBuzz"
"""


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def test_fizzbuzz():
    # 테스트 1
    result = fizzbuzz(15)
    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
    print(f"FizzBuzz(15): {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    # 테스트 2
    result = fizzbuzz(5)
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    print(f"FizzBuzz(5): {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✅ All Python FizzBuzz tests passed!")


if __name__ == "__main__":
    test_fizzbuzz()
