package dongwoo.week8.ticket;

import java.util.List;
import java.util.Objects;

public class LongJump {

    public long solution(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;

        long prev2 = 1; // n-2 번째 값
        long prev1 = 2; // n-1 번째 값
        long current = 0;

        // ways(i) = ways(i-1) + ways(i-2)
        for (int i = 3; i <= n; i++) {
            current = (prev1 + prev2) % 1234567;
            prev2 = prev1;
            prev1 = current;
        }

        return current;
    }

    private record TestCase(String name, int input, long expected, String description) {

    }

    public void runAllTests() {
        System.out.println("테스트 시작...");
        System.out.println("----------------------------------------");

        final List<TestCase> testCases = List.of(
                new TestCase("기본 케이스 1", 3, 3L, "3칸을 뛰는 방법의 수"),
                new TestCase("기본 케이스 2", 4, 5L, "문제에 명시된 4칸 예시"),
                new TestCase("작은 입력값 1", 1, 1L, "1칸을 뛰는 방법의 수"),
                new TestCase("작은 입력값 2", 2, 2L, "2칸을 뛰는 방법의 수"),
                new TestCase("조금 큰 입력값", 10, 89L, "10칸을 뛰는 방법의 수")
        );

        boolean allTestsPassed = true;

        for (int i = 0; i < testCases.size(); i++) {
            TestCase tc = testCases.get(i);
            long result = solution(tc.input);

            if (Objects.equals(result, tc.expected)) {
                System.out.printf("[%d] %s: 테스트 통과 %n", i + 1, tc.name);
            } else {
                System.err.printf("[%d] %s: 테스트 실패 %n", i + 1, tc.name);
                System.err.printf("     - 설명: %s%n", tc.description);
                System.err.printf("     - 입력값: %d%n", tc.input);
                System.err.printf("     - 기대값: %d%n", tc.expected);
                System.err.printf("     - 실제값: %d%n", result);
                allTestsPassed = false;
            }
        }

        System.out.println("----------------------------------------");
        if (allTestsPassed) {
            System.out.println("모든 테스트가 성공적으로 완료되었습니다!");
        } else {
            System.out.println("일부 테스트가 실패했습니다.");
        }
    }

    public static void main(String[] args) {
        LongJump lj = new LongJump();
        lj.runAllTests();
    }
}
