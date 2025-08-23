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


# n, c = map(int, input().split())
# m = int(input())
# delivery_list = [list(map(int, input().split())) for _ in range(m)]

# result = solution(n, c, m, delivery_list)

# print(result)


def main():
    # 예시 테스트 케이스
    n, c, m = 4, 40, 6
    delivery_list = [
        [3, 4, 20],
        [1, 2, 10],
        [1, 3, 20],
        [1, 4, 30],
        [2, 3, 10],
        [2, 4, 20],
    ]

    # deque는 정렬이 불편하므로 list로 변환하여 사용
    result = solution(n, c, m, delivery_list)

    print(f"최종 배송된 박스 수: {result}")

    # 기대값 확인
    expected = 70
    if result == expected:
        print("정답입니다!")
    else:
        print(f"오답입니다. 기대값: {expected}, 결과: {result} ")


if __name__ == "__main__":
    main()
