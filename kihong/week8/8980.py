"""
8980. 택배
https://www.acmicpc.net/problem/8980

"""


def solution(n, c, m, delivery_list):
    # 도착 지점 기준으로 오름차순 정렬 (도착 지점이 같으면 출발 지점 기준)
    delivery_list.sort(key=lambda x: (x[1], x[0]))

    # 각 구간에 실려 있는 박스 수를 저장하는 배열
    truck = [0] * (n + 1)
    total_delivered = 0

    for start, end, boxes in delivery_list:
        # 현재 트럭에 실을 수 있는 최대 용량 계산
        max_load = c
        # start에서 end까지 갈 때 담을 수 있는 최대 용량 계산
        for i in range(start, end):
            max_load = min(max_load, c - truck[i])

        # 실제로 실을 수 있는 박스 수 (요청된 박스 수와 남은 용량 중 작은 값)
        load_count = min(boxes, max_load)

        # 트럭에 박스 싣기(start에서 end까지 갈 때 가지고 있을 박스 기록)
        for i in range(start, end):
            truck[i] += load_count

        total_delivered += load_count

    return total_delivered


def main():
    # 예시 테스트 케이스
    cases = [
        {
            "name": "test case 1",
            "n": 4,
            "c": 40,
            "m": 6,
            "delivery_list": [
                [3, 4, 20],
                [1, 2, 10],
                [1, 3, 20],
                [1, 4, 30],
                [2, 3, 10],
                [2, 4, 20],
            ],
            "expected": 70,
        },
        {
            "name": "test case 2",
            "n": 6,
            "c": 60,
            "m": 5,
            "delivery_list": [
                [1, 2, 30],
                [2, 5, 70],
                [5, 6, 60],
                [3, 4, 40],
                [1, 6, 40],
            ],
            "expected": 150,
        },
    ]
    for i, tc in enumerate(cases, 1):
        delivery_copy = [row[:] for row in tc["delivery_list"]]
        actual_result = solution(tc["n"], tc["c"], tc["m"], delivery_copy)
        assert actual_result == tc["expected"], (
            f"[{i}] {tc['name']} 실패: "
            f"expected={tc['expected']}, actual_result={actual_result}, "
            f"input=(n={tc['n']}, c={tc['c']}, m={tc['m']})"
        )
        print(f"[{i}] {tc['name']} 성공")


if __name__ == "__main__":
    main()
