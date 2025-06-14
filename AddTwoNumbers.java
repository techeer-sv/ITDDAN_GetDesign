import java.util.Arrays;

public class AddTwoNumbers {

     // Definition for singly-linked list.
      public static class ListNode {
          int val;
          ListNode next;
          ListNode(int val) { this.val = val; }
     }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode cur = head;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int x = 0, y = 0;
            if (l1 != null) {
                x = l1.val;
            }
            if (l2 != null) {
                y = l2.val;
            }
            int sum = x + y + carry;
            carry = sum / 10;
            cur.next = new ListNode(sum % 10);
            cur = cur.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        return head.next;
    }

    private static ListNode toList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int n : arr) {
            curr.next = new ListNode(n);
            curr = curr.next;
        }
        return dummy.next;
    }

    private static int[] toArray(ListNode node) {
        int[] temp = new int[100];
        int idx = 0;
        while (node != null) {
            temp[idx++] = node.val;
            node = node.next;
        }
        return Arrays.copyOf(temp, idx);
    }

    public static void testAddTwoNumbers() {
        AddTwoNumbers solver = new AddTwoNumbers();

        assertTest(solver, new int[]{2,4,3}, new int[]{5,6,4}, new int[]{7,0,8});
        assertTest(solver, new int[]{0}, new int[]{0}, new int[]{0});
        assertTest(solver, new int[]{9,9,9,9,9,9,9}, new int[]{9,9,9,9}, new int[]{8,9,9,9,0,0,0,1});

        System.out.println("All addTwoNumbers tests passed!");
    }

    private static void assertTest(AddTwoNumbers solver, int[] input1, int[] input2, int[] expected) {
        ListNode l1 = toList(input1);
        ListNode l2 = toList(input2);
        ListNode resultNode = solver.addTwoNumbers(l1, l2);
        int[] result = toArray(resultNode);

        System.out.println("Input1: " + Arrays.toString(input1));
        System.out.println("Input2: " + Arrays.toString(input2));
        System.out.println("Output : " + Arrays.toString(result));
        System.out.println("Expect : " + Arrays.toString(expected));
        System.out.println();

        assert Arrays.equals(result, expected) : "Expected " + Arrays.toString(expected) + ", but got " + Arrays.toString(result);
    }

    public static void main(String[] args) {
        testAddTwoNumbers();
    }
}
