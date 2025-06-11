#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

/**
 * 두 수의 합 (Two Sum) - C++
 * 배열에서 두 수를 더해서 target이 되는 인덱스를 찾는 문제
 */

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> numMap;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (numMap.find(complement) != numMap.end()) {
            return {numMap[complement], i};
        }
        numMap[nums[i]] = i;
    }
    return {};
}

void printVector(const std::vector<int>& vec) {
    std::cout << "[";
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i];
        if (i < vec.size() - 1) std::cout << ", ";
    }
    std::cout << "]";
}

void testTwoSum() {
    // 테스트 1
    std::vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    std::vector<int> result1 = twoSum(nums1, target1);
    std::cout << "Test 1: nums=";
    printVector(nums1);
    std::cout << ", target=" << target1 << std::endl;
    std::cout << "Result: ";
    printVector(result1);
    std::cout << " (Expected: [0, 1])" << std::endl;
    assert(result1.size() == 2 && result1[0] == 0 && result1[1] == 1);
    
    // 테스트 2
    std::vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    std::vector<int> result2 = twoSum(nums2, target2);
    std::cout << "Test 2: nums=";
    printVector(nums2);
    std::cout << ", target=" << target2 << std::endl;
    std::cout << "Result: ";
    printVector(result2);
    std::cout << " (Expected: [1, 2])" << std::endl;
    assert(result2.size() == 2 && result2[0] == 1 && result2[1] == 2);
    
    // 테스트 3
    std::vector<int> nums3 = {3, 3};
    int target3 = 6;
    std::vector<int> result3 = twoSum(nums3, target3);
    std::cout << "Test 3: nums=";
    printVector(nums3);
    std::cout << ", target=" << target3 << std::endl;
    std::cout << "Result: ";
    printVector(result3);
    std::cout << " (Expected: [0, 1])" << std::endl;
    assert(result3.size() == 2 && result3[0] == 0 && result3[1] == 1);
    
    std::cout << "✅ All C++ tests passed!" << std::endl;
}

int main() {
    testTwoSum();
    return 0;
} 