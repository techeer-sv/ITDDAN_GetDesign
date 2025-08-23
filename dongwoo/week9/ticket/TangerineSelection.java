package dongwoo.week9.ticket;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public class TangerineSelection {

    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> countBySize = new HashMap<>();
        for (int size : tangerine) {
            countBySize.put(size, countBySize.getOrDefault(size, 0) + 1);
        }

        List<Integer> counts = new ArrayList<>(countBySize.values());
        counts.sort(Collections.reverseOrder());

        int answer = 0;
        int remainTangs = k;

        for (int count : counts) {
            answer++;
            remainTangs -= count;
            if (remainTangs <= 0) {
                break;
            }
        }

        return answer;
    }

    private record TestCase(String name, int k, int[] tangerine, int expected, String description) {
    }

    public void runAllTests() {
        System.out.println("테스트 시작...");
        System.out.println("----------------------------------------");

        final List<TestCase> testCases = List.of(
                new TestCase("예제 케이스 1", 6, new int[]{1, 3, 2, 5, 4, 5, 2, 3}, 3, "문제에 명시된 예시"),
                new TestCase("케이스 2", 4, new int[]{1, 3, 2, 5, 4, 5, 2, 3}, 2, "가장 개수가 많은 귤 종류로만 4개 선택"),
                new TestCase("케이스 3", 2, new int[]{1, 1, 1, 1, 2, 2, 3, 3, 4, 5}, 1, "한 종류의 귤로만 2개 선택 가능"),
                new TestCase("케이스 4", 10, new int[]{1, 1, 1, 2, 2, 3, 3, 3, 3, 4}, 4, "모든 종류를 다 합쳐야 10개 가능")
        );

        boolean allTestsPassed = true;

        for (int i = 0; i < testCases.size(); i++) {
            TestCase tc = testCases.get(i);
            int result = solution(tc.k(), tc.tangerine());

            if (Objects.equals(result, tc.expected())) {
                System.out.printf("[%d] %s: 테스트 통과 %n", i + 1, tc.name());
            } else {
                System.err.printf("[%d] %s: 테스트 실패 %n", i + 1, tc.name());
                System.err.printf("     - 설명: %s%n", tc.description());
                System.err.printf("     - 입력값: k=%d, tangerine=%s%n", tc.k(), java.util.Arrays.toString(tc.tangerine()));
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
        TangerineSelection ts = new TangerineSelection();
        ts.runAllTests();
    }
}
