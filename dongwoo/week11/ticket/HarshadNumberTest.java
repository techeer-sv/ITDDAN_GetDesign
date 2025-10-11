package dongwoo.week11.ticket;

import java.util.List;
import java.util.Objects;

public class HarshadNumberTest {
    // 테스트 케이스를 위한 자료구조 (Record)
    private record TestCase(String name, int input, boolean expected, String description) {
    }

    // 테스트 실행 로직: 테스트 케이스 리스트를 파라미터로 받습니다.
    public void runAllTests(List<TestCase> testCases) {
        System.out.println("하샤드 수 테스트 시작...");
        System.out.println("----------------------------------------");

        boolean allTestsPassed = true;
        // 테스트할 solution 객체를 생성합니다.
        HarshadNumber harshadNumber = new HarshadNumber();

        for (int i = 0; i < testCases.size(); i++) {
            TestCase tc = testCases.get(i);

            // solution 메서드를 호출하여 실제 결과를 얻습니다.
            boolean result = harshadNumber.solution(tc.input());

            // 기대값과 실제값을 비교합니다.
            if (Objects.equals(result, tc.expected())) {
                System.out.printf("[%d] %s: 테스트 통과 %n", i + 1, tc.name());
            } else {
                System.err.printf("[%d] %s: 테스트 실패 %n", i + 1, tc.name());
                System.err.printf("     - 설명: %s%n", tc.description());
                System.err.printf("     - 입력값: %d%n", tc.input());
                System.err.printf("     - 기대값: %b%n", tc.expected());
                System.err.printf("     - 실제값: %b%n", result);
                allTestsPassed = false;
            }
        }

        System.out.println("----------------------------------------");
        if (allTestsPassed) {
            System.out.println("🎉 모든 테스트가 성공적으로 완료되었습니다!");
        } else {
            System.out.println("❗️ 일부 테스트가 실패했습니다.");
        }
    }

    public static void main(String[] args) {
        // 테스트 케이스 데이터를 여기서 정의합니다.
        final List<TestCase> testCases = List.of(
                new TestCase(
                        "예제 케이스 1",
                        10,
                        true,
                        "10의 자릿수 합은 1. 10은 1로 나누어 떨어집니다."
                ),
                new TestCase(
                        "예제 케이스 2",
                        12,
                        true,
                        "12의 자릿수 합은 3. 12는 3으로 나누어 떨어집니다."
                ),
                new TestCase(
                        "예제 케이스 3",
                        11,
                        false,
                        "11의 자릿수 합은 2. 11은 2로 나누어 떨어지지 않습니다."
                ),
                new TestCase(
                        "예제 케이스 4",
                        13,
                        false,
                        "13의 자릿수 합은 4. 13은 4로 나누어 떨어지지 않습니다."
                ),
                new TestCase(
                        "한 자릿수 케이스",
                        8,
                        true,
                        "한 자릿수 숫자는 항상 하샤드 수입니다."
                ),
                new TestCase(
                        "큰 숫자 케이스",
                        1729,
                        true,
                        "1729의 자릿수 합은 19. 1729는 19로 나누어 떨어집니다 (1729 = 19 * 91)."
                )
        );

        // 테스트 클래스 인스턴스를 생성하고, 정의된 테스트 케이스를 '주입'하여 실행합니다.
        HarshadNumberTest tester = new HarshadNumberTest();
        tester.runAllTests(testCases);
    }
}
