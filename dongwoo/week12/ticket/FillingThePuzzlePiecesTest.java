package dongwoo.week12.ticket;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class FillingThePuzzlePiecesTest {
    // 테스트 케이스를 위한 자료구조
    private record TestCase(String name, int[][] game_board, int[][] table, int expected, String description) {
    }

    // 테스트 실행 로직: 이제 테스트 케이스 리스트를 파라미터로 받습니다.
    public void runAllTests(List<TestCase> testCases) {
        System.out.println("테스트 시작...");
        System.out.println("----------------------------------------");

        boolean allTestsPassed = true;
        // 테스트할 solution 객체를 생성합니다.
        FillingThePuzzlePieces solver = new FillingThePuzzlePieces();

        for (int i = 0; i < testCases.size(); i++) {
            TestCase tc = testCases.get(i);

            int result = solver.solution(tc.game_board(), tc.table());

            if (Objects.equals(result, tc.expected())) {
                System.out.printf("[%d] %s: 테스트 통과 %n", i + 1, tc.name());
            } else {
                System.err.printf("[%d] %s: 테스트 실패 %n", i + 1, tc.name());
                System.err.printf("     - 설명: %s%n", tc.description());
                System.err.printf("     - 입력값: game_board=%s, table=%s%n", Arrays.deepToString(tc.game_board()), Arrays.deepToString(tc.table()));
                System.err.printf("     - 기대값: %d%n", tc.expected());
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
        // 테스트 케이스 데이터를 여기서 정의합니다.
        final List<TestCase> testCases = List.of(
                new TestCase(
                        "예제 케이스 1",
                        new int[][]{{1, 1, 0, 0, 1, 0}, {0, 0, 1, 0, 1, 0}, {0, 1, 1, 0, 0, 1}, {1, 1, 0, 1, 1, 1}, {1, 0, 0, 0, 1, 0}, {0, 1, 1, 1, 0, 0}},
                        new int[][]{{1, 0, 0, 1, 1, 0}, {1, 0, 1, 0, 1, 0}, {0, 1, 1, 0, 1, 1}, {0, 0, 1, 0, 0, 0}, {1, 1, 0, 1, 1, 0}, {0, 1, 0, 0, 0, 0}},
                        14,
                        "문제에 명시된 첫 번째 예시"
                ),
                new TestCase(
                        "예제 케이스 2",
                        new int[][]{{0, 0, 0}, {1, 1, 0}, {1, 1, 1}},
                        new int[][]{{1, 1, 1}, {1, 0, 0}, {0, 0, 0}},
                        0,
                        "문제에 명시된 두 번째 예시"
                )
        );

        // 테스트 클래스 인스턴스를 생성하고, 정의된 테스트 케이스를 '주입'하여 실행합니다.
        FillingThePuzzlePiecesTest tester = new FillingThePuzzlePiecesTest();
        tester.runAllTests(testCases);
    }
}
