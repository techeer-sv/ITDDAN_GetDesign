package jungeun.week12;

public class FindKimTest {
    public static void main(String[] args) {
        FindKim findKim = new FindKim();
        int passCount = 0;
        int totalTests = 5;

        // Test 1: Kim이 첫 번째 위치에 있는 경우
        String[] seoul1 = { "Kim", "Park", "Lee" };
        String result1 = findKim.solution(seoul1);
        String expected1 = "김서방은 0에 있다";
        if (result1.equals(expected1)) {
            System.out.println("✓ Test 1 Passed: " + result1);
            passCount++;
        } else {
            System.out.println("✗ Test 1 Failed: Expected '" + expected1 + "', but got '" + result1 + "'");
        }

        // Test 2: Kim이 중간 위치에 있는 경우
        String[] seoul2 = { "Jane", "Kim", "Park" };
        String result2 = findKim.solution(seoul2);
        String expected2 = "김서방은 1에 있다";
        if (result2.equals(expected2)) {
            System.out.println("✓ Test 2 Passed: " + result2);
            passCount++;
        } else {
            System.out.println("✗ Test 2 Failed: Expected '" + expected2 + "', but got '" + result2 + "'");
        }

        // Test 3: Kim이 마지막 위치에 있는 경우
        String[] seoul3 = { "Jane", "Park", "Lee", "Kim" };
        String result3 = findKim.solution(seoul3);
        String expected3 = "김서방은 3에 있다";
        if (result3.equals(expected3)) {
            System.out.println("✓ Test 3 Passed: " + result3);
            passCount++;
        } else {
            System.out.println("✗ Test 3 Failed: Expected '" + expected3 + "', but got '" + result3 + "'");
        }

        // Test 4: 배열에 Kim만 있는 경우
        String[] seoul4 = { "Kim" };
        String result4 = findKim.solution(seoul4);
        String expected4 = "김서방은 0에 있다";
        if (result4.equals(expected4)) {
            System.out.println("✓ Test 4 Passed: " + result4);
            passCount++;
        } else {
            System.out.println("✗ Test 4 Failed: Expected '" + expected4 + "', but got '" + result4 + "'");
        }

        // Test 5: 긴 배열에서 Kim을 찾는 경우
        String[] seoul5 = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "Kim" };
        String result5 = findKim.solution(seoul5);
        String expected5 = "김서방은 9에 있다";
        if (result5.equals(expected5)) {
            System.out.println("✓ Test 5 Passed: " + result5);
            passCount++;
        } else {
            System.out.println("✗ Test 5 Failed: Expected '" + expected5 + "', but got '" + result5 + "'");
        }

        // 결과 요약
        System.out.println("\n========================================");
        System.out.println("Test Results: " + passCount + "/" + totalTests + " passed");
        if (passCount == totalTests) {
            System.out.println("All tests passed! ✓");
        } else {
            System.out.println((totalTests - passCount) + " test(s) failed.");
        }
        System.out.println("========================================");
    }
}
