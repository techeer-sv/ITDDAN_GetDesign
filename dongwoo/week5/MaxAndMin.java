package dongwoo.week5;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MaxAndMin {
    public static String findMinAndMax(String s) {
        List<Integer> nums =
                Arrays.stream(s.split(" ")).map(Integer::parseInt).toList();
        int min = Collections.min(nums);
        int max = Collections.max(nums);
        return min + " " + max;
    }

    /**
     * 테스트 메서드
     */
    public static void testFindMinAndMax() {
        // 테스트 1: 양수와 음수 포함
        String input1 = "1 2 3 4 -5";
        String expected1 = "-5 4";
        String result1 = findMinAndMax(input1);
        System.out.println("Test 1 result: " + result1);
        assert result1.equals(expected1) : "Expected \"" + expected1 + "\", got \"" + result1 + "\"";

        // 테스트 2: 공백 여러 개 포함
        String input2 = "7 0 -2 9";
        String expected2 = "-2 9";
        String result2 = findMinAndMax(input2);
        System.out.println("Test 2 result: " + result2);
        assert result2.equals(expected2) : "Expected \"" + expected2 + "\", got \"" + result2 + "\"";

        // 테스트 3: 음수만
        String input3 = "-1 -2 -3";
        String expected3 = "-3 -1";
        String result3 = findMinAndMax(input3);
        System.out.println("Test 3 result: " + result3);
        assert result3.equals(expected3) : "Expected \"" + expected3 + "\", got \"" + result3 + "\"";

        // 테스트 4: 하나만 입력
        String input4 = "42";
        String expected4 = "42 42";
        String result4 = findMinAndMax(input4);
        System.out.println("Test 4 result: " + result4);
        assert result4.equals(expected4) : "Expected \"" + expected4 + "\", got \"" + result4 + "\"";
    }

    public static void main(String[] args) {
        testFindMinAndMax();
    }
}
