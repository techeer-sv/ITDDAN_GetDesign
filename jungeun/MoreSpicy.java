package jungeun;

import java.util.PriorityQueue;

/**
 * 더 맵게 - Java(프로그래머스 42626)
 * 모든 음식의 스코빌 지수가 k 이상이 되도록 섞는 최소 횟수 구하기
 * - PriorityQueue(최소 힙) 사용
 */
public class MoreSpicy {

    public static int makeMoreSpicy(int[] scoville, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) {
            pq.offer(s);
        }

        int count = 0;
        while (pq.size() > 1 && pq.peek() < k) {
            int first = pq.poll();
            int second = pq.poll();
            int mixed = first + (second * 2);
            pq.offer(mixed);
            count++;
        }

        return pq.peek() >= k ? count : -1;
    }

    public static void testMakeMoreSpicy() {
        // 테스트 1
        int[] scoville1 = { 1, 2, 3, 9, 10, 12 };
        int k1 = 7;
        int expected1 = 2;
        int result1 = makeMoreSpicy(scoville1, k1);
        System.out.println("Test 1 result: " + result1);
        assert result1 == expected1 : "Expected " + expected1 + ", got " + result1;

        // 테스트 2
        int[] scoville2 = { 1, 1, 1 };
        int k2 = 10;
        int expected2 = -1;
        int result2 = makeMoreSpicy(scoville2, k2);
        System.out.println("Test 2 result: " + result2);
        assert result2 == expected2 : "Expected " + expected2 + ", got " + result2;

        System.out.println("✅ All tests passed for MoreSpicy!");
    }

    public static void main(String[] args) {
        testMakeMoreSpicy();
    }
}
