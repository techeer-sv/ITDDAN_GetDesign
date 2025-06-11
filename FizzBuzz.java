import java.util.*;

/**
 * FizzBuzz - Java
 * 1부터 n까지 숫자를 출력하되:
 * - 3의 배수면 "Fizz"
 * - 5의 배수면 "Buzz"  
 * - 15의 배수면 "FizzBuzz"
 */
public class FizzBuzz {
    
    public static List<String> fizzbuzz(int n) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(String.valueOf(i));
            }
        }
        return result;
    }
    
    public static void testFizzBuzz() {
        // 테스트 1
        List<String> result = fizzbuzz(15);
        List<String> expected = Arrays.asList("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz");
        System.out.println("FizzBuzz(15): " + result);
        assert result.equals(expected) : "Expected " + expected + ", got " + result;
        
        // 테스트 2
        List<String> result2 = fizzbuzz(5);
        List<String> expected2 = Arrays.asList("1", "2", "Fizz", "4", "Buzz");
        System.out.println("FizzBuzz(5): " + result2);
        assert result2.equals(expected2) : "Expected " + expected2 + ", got " + result2;
        
        System.out.println("✅ All Java FizzBuzz tests passed!");
    }
    
    public static void main(String[] args) {
        testFizzBuzz();
    }
} 