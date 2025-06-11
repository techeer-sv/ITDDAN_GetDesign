import java.util.*;

/**
 * 두 수의 합 (Two Sum) - Java
 * 배열에서 두 수를 더해서 target이 되는 인덱스를 찾는 문제
 */
public class TwoSum {
    
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i};
            }
            numMap.put(nums[i], i);
        }
        return new int[]{};
    }
    
    public static void testTwoSum() {
        // 테스트 1
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] result1 = twoSum(nums1, target1);
        System.out.println("Test 1: nums=" + Arrays.toString(nums1) + ", target=" + target1);
        System.out.println("Result: " + Arrays.toString(result1) + " (Expected: [0, 1])");
        assert Arrays.equals(result1, new int[]{0, 1}) : "Expected [0, 1], got " + Arrays.toString(result1);
        
        // 테스트 2
        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        int[] result2 = twoSum(nums2, target2);
        System.out.println("Test 2: nums=" + Arrays.toString(nums2) + ", target=" + target2);
        System.out.println("Result: " + Arrays.toString(result2) + " (Expected: [1, 2])");
        assert Arrays.equals(result2, new int[]{1, 2}) : "Expected [1, 2], got " + Arrays.toString(result2);
        
        // 테스트 3
        int[] nums3 = {3, 3};
        int target3 = 6;
        int[] result3 = twoSum(nums3, target3);
        System.out.println("Test 3: nums=" + Arrays.toString(nums3) + ", target=" + target3);
        System.out.println("Result: " + Arrays.toString(result3) + " (Expected: [0, 1])");
        assert Arrays.equals(result3, new int[]{0, 1}) : "Expected [0, 1], got " + Arrays.toString(result3);
        
        System.out.println("✅ All Java tests passed!");
    }
    
    public static void main(String[] args) {
        testTwoSum();
    }
} 