package main

import (
	"fmt"
	"reflect"
	"strconv"
)

/**
 * FizzBuzz - Go
 * 1부터 n까지 숫자를 출력하되:
 * - 3의 배수면 "Fizz"
 * - 5의 배수면 "Buzz"
 * - 15의 배수면 "FizzBuzz"
 */

func fizzbuzz(n int) []string {
	result := make([]string, 0, n)
	for i := 1; i <= n; i++ {
		temp := ""
		if i%3 == 0 {
			temp += "Fizz"
		}
		if i%5 == 0 {
			temp += "Buzz"
		}
		if temp == "" {
			temp = strconv.Itoa(i)
		}
		result = append(result, temp)
	}
	return result
}

func testFizzBuzz() {
	// 테스트 1
	result := fizzbuzz(15)
	expected := []string{"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"}
	fmt.Printf("FizzBuzz(15): %v\n", result)
	if !reflect.DeepEqual(result, expected) {
		panic(fmt.Sprintf("Expected %v, got %v", expected, result))
	}

	// 테스트 2
	result2 := fizzbuzz(5)
	expected2 := []string{"1", "2", "Fizz", "4", "Buzz"}
	fmt.Printf("FizzBuzz(5): %v\n", result2)
	if !reflect.DeepEqual(result2, expected2) {
		panic(fmt.Sprintf("Expected %v, got %v", expected2, result2))
	}

	fmt.Println("✅ All Go FizzBuzz tests passed!")
}

func main() {
	testFizzBuzz()
}