/**
 * FizzBuzz - JavaScript
 * 1부터 n까지 숫자를 출력하되:
 * - 3의 배수면 "Fizz"
 * - 5의 배수면 "Buzz"  
 * - 15의 배수면 "FizzBuzz"
 */

function fizzbuzz(n) {
    const result = [];
    for (let i = 1; i <= n; i++) {
        if (i % 15 === 0) {
            result.push("FizzBuzz");
        } else if (i % 3 === 0) {
            result.push("Fizz");
        } else if (i % 5 === 0) {
            result.push("Buzz");
        } else {
            result.push(i.toString());
        }
    }
    return result;
}

function testFizzBuzz() {
    // 테스트 1
    const result = fizzbuzz(15);
    const expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"];
    console.log(`FizzBuzz(15): ${JSON.stringify(result)}`);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Expected ${JSON.stringify(expected)}, got ${JSON.stringify(result)}`);
    
    // 테스트 2
    const result2 = fizzbuzz(5);
    const expected2 = ["1", "2", "Fizz", "4", "Buzz"];
    console.log(`FizzBuzz(5): ${JSON.stringify(result2)}`);
    console.assert(JSON.stringify(result2) === JSON.stringify(expected2), `Expected ${JSON.stringify(expected2)}, got ${JSON.stringify(result2)}`);
    
    console.log("✅ All JavaScript FizzBuzz tests passed!");
}

// 실행
testFizzBuzz(); 