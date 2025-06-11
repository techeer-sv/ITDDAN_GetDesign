#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/**
 * 두 수의 합 (Two Sum) - C
 * 배열에서 두 수를 더해서 target이 되는 인덱스를 찾는 문제
 */

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // 간단한 브루트 포스 방식 (O(n^2))
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                int* result = (int*)malloc(2 * sizeof(int));
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

void printArray(int* arr, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]");
}

void testTwoSum() {
    int returnSize;
    
    // 테스트 1
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int* result1 = twoSum(nums1, 4, target1, &returnSize);
    printf("Test 1: nums=");
    printArray(nums1, 4);
    printf(", target=%d\n", target1);
    printf("Result: ");
    printArray(result1, returnSize);
    printf(" (Expected: [0, 1])\n");
    assert(returnSize == 2 && result1[0] == 0 && result1[1] == 1);
    free(result1);
    
    // 테스트 2
    int nums2[] = {3, 2, 4};
    int target2 = 6;
    int* result2 = twoSum(nums2, 3, target2, &returnSize);
    printf("Test 2: nums=");
    printArray(nums2, 3);
    printf(", target=%d\n", target2);
    printf("Result: ");
    printArray(result2, returnSize);
    printf(" (Expected: [1, 2])\n");
    assert(returnSize == 2 && result2[0] == 1 && result2[1] == 2);
    free(result2);
    
    // 테스트 3
    int nums3[] = {3, 3};
    int target3 = 6;
    int* result3 = twoSum(nums3, 2, target3, &returnSize);
    printf("Test 3: nums=");
    printArray(nums3, 2);
    printf(", target=%d\n", target3);
    printf("Result: ");
    printArray(result3, returnSize);
    printf(" (Expected: [0, 1])\n");
    assert(returnSize == 2 && result3[0] == 0 && result3[1] == 1);
    free(result3);
    
    printf("✅ All C tests passed!\n");
}

int main() {
    testTwoSum();
    return 0;
} 