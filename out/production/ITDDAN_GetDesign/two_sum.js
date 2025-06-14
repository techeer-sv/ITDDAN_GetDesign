/**
 * 두 수의 합 (Two Sum) - JavaScript
 * 배열에서 두 수를 더해서 target이 되는 인덱스를 찾는 문제
 */

function twoSum(nums, target) {
    const numMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (numMap.has(complement)) {
            return [numMap.get(complement), i];
        }
        numMap.set(nums[i], i);
    }
    return [];
}

function testTwoSum() {
    // 테스트 1
    const nums1 = [2, 7, 11, 15];
    const target1 = 9;
    const result1 = twoSum(nums1, target1);
    console.log(`Test 1: nums=[${nums1}], target=${target1}`);
    console.log(`Result: [${result1}] (Expected: [0, 1])`);
    console.assert(JSON.stringify(result1) === JSON.stringify([0, 1]), `Expected [0, 1], got [${result1}]`);
    
    // 테스트 2
    const nums2 = [3, 2, 4];
    const target2 = 6;
    const result2 = twoSum(nums2, target2);
    console.log(`Test 2: nums=[${nums2}], target=${target2}`);
    console.log(`Result: [${result2}] (Expected: [1, 2])`);
    console.assert(JSON.stringify(result2) === JSON.stringify([1, 2]), `Expected [1, 2], got [${result2}]`);
    
    // 테스트 3
    const nums3 = [3, 3];
    const target3 = 6;
    const result3 = twoSum(nums3, target3);
    console.log(`Test 3: nums=[${nums3}], target=${target3}`);
    console.log(`Result: [${result3}] (Expected: [0, 1])`);
    console.assert(JSON.stringify(result3) === JSON.stringify([0, 1]), `Expected [0, 1], got [${result3}]`);
    
    console.log("✅ All JavaScript tests passed!");
}

// 실행
testTwoSum(); 