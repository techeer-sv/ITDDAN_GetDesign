package dongwoo.week6.ticket;

public class NLeastCommonMultiples {

    public static int getLCM(int[] arr) {
        int result = arr[0];

        for (int i = 1; i < arr.length; i++) {
            result = lcm(result, arr[i]);
        }

        return result;
    }

    private static int lcm(int a, int b) {
        int original = a * b;

        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }

        return original / a; // 여기서 a는 GCD
    }

    /**
     * 테스트 메서드
     */
    public static void testGetLCM() {
        // 테스트 1
        int[] input1 = {2, 6, 8, 14};
        int expected1 = 168;
        int result1 = getLCM(input1);
        System.out.println("Test 1 result: " + result1);
        assert result1 == expected1 : "Expected " + expected1 + ", got " + result1;

        // 테스트 2
        int[] input2 = {1, 2, 3};
        int expected2 = 6;
        int result2 = getLCM(input2);
        System.out.println("Test 2 result: " + result2);
        assert result2 == expected2 : "Expected " + expected2 + ", got " + result2;

        // 테스트 3
        int[] input3 = {5, 7, 11};
        int expected3 = 385;
        int result3 = getLCM(input3);
        System.out.println("Test 3 result: " + result3);
        assert result3 == expected3 : "Expected " + expected3 + ", got " + result3;

        // 테스트 4: 하나만 입력
        int[] input4 = {42};
        int expected4 = 42;
        int result4 = getLCM(input4);
        System.out.println("Test 4 result: " + result4);
        assert result4 == expected4 : "Expected " + expected4 + ", got " + result4;
    }

    public static void main(String[] args) {
        testGetLCM();
    }
}
