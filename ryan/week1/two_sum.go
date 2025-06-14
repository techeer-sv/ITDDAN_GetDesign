package main

import (
	"fmt"
	"reflect"
)

/**
 * 두 수의 합 (Two Sum) - Go
 * 배열에서 두 수를 더해서 target이 되는 인덱스를 찾는 문제
 */

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if index, exists := numMap[complement]; exists {
			return []int{index, i}
		}
		numMap[num] = i
	}
	return []int{}
}

func testTwoSum() {
	// 테스트 1
	nums1 := []int{2, 7, 11, 15}
	target1 := 9
	result1 := twoSum(nums1, target1)
	fmt.Printf("Test 1: nums=%v, target=%d\n", nums1, target1)
	fmt.Printf("Result: %v (Expected: [0 1])\n", result1)
	if !reflect.DeepEqual(result1, []int{0, 1}) {
		panic(fmt.Sprintf("Expected [0 1], got %v", result1))
	}

	// 테스트 2
	nums2 := []int{3, 2, 4}
	target2 := 6
	result2 := twoSum(nums2, target2)
	fmt.Printf("Test 2: nums=%v, target=%d\n", nums2, target2)
	fmt.Printf("Result: %v (Expected: [1 2])\n", result2)
	if !reflect.DeepEqual(result2, []int{1, 2}) {
		panic(fmt.Sprintf("Expected [1 2], got %v", result2))
	}

	// 테스트 3
	nums3 := []int{3, 3}
	target3 := 6
	result3 := twoSum(nums3, target3)
	fmt.Printf("Test 3: nums=%v, target=%d\n", nums3, target3)
	fmt.Printf("Result: %v (Expected: [0 1])\n", result3)
	if !reflect.DeepEqual(result3, []int{0, 1}) {
		panic(fmt.Sprintf("Expected [0 1], got %v", result3))
	}

	fmt.Println("✅ All Go tests passed!")
}

func main() {
	testTwoSum()
}