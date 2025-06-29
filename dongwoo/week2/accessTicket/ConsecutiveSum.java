package dongwoo.week2.accessTicket;
/**
 * 연속된 자연수의 합으로 표현 - Java (프로그래머스: 숫자의 표현)
 * 자연수 n을 연속된 자연수의 합으로 표현하는 방법의 수 반환
 */
public class ConsecutiveSum {

    public static int countConsecutiveSumWays(int n) {
        int answer = 0;
        for (int k = 1; (k * (k - 1)) / 2 < n; k++) {
            int t = n - (k * (k - 1)) / 2;
            if (t % k == 0) {
                answer++;
            }
        }
        return answer;
    }

    public static void testCountConsecutiveSumWays() {
        // 테스트 1
        int n1 = 15;
        int expected1 = 4; // 1+2+3+4+5, 4+5+6, 7+8, 15
        int result1 = countConsecutiveSumWays(n1);
        System.out.println("Test 1 result: " + result1);
        assert result1 == expected1 : "Expected " + expected1 + ", got " + result1;

        // 테스트 2
        int n2 = 10;
        int expected2 = 2; // 1+2+3+4, 10
        int result2 = countConsecutiveSumWays(n2);
        System.out.println("Test 2 result: " + result2);
        assert result2 == expected2 : "Expected " + expected2 + ", got " + result2;

        // 테스트 3
        int n3 = 1;
        int expected3 = 1; // 1
        int result3 = countConsecutiveSumWays(n3);
        System.out.println("Test 3 result: " + result3);
        assert result3 == expected3 : "Expected " + expected3 + ", got " + result3;

        // 테스트 4
        int n4 = 9;
        int expected4 = 3; // 2+3+4, 4+5, 9
        int result4 = countConsecutiveSumWays(n4);
        System.out.println("Test 4 result: " + result4);
        assert result4 == expected4 : "Expected " + expected4 + ", got " + result4;

        System.out.println("All tests passed for ConsecutiveSum!");
    }

    public static void main(String[] args) {
        testCountConsecutiveSumWays();
    }
}
