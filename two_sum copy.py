"""
두 수의 합 (Two Sum) - Python
배열에서 두 수를 더해서 target이 되는 인덱스를 찾는 문제
"""

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# 테스트 케이스
def test_two_sum():
    # 테스트 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1} (Expected: [0, 1])")
    assert result1 == [0, 1], f"Expected [0, 1], got {result1}"
    
    # 테스트 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Result: {result2} (Expected: [1, 2])")
    assert result2 == [1, 2], f"Expected [1, 2], got {result2}"
    
    # 테스트 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Result: {result3} (Expected: [0, 1])")
    assert result3 == [0, 1], f"Expected [0, 1], got {result3}"
    
    print("✅ All Python tests passed!")

if __name__ == "__main__":
    test_two_sum() 