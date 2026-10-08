var twoSum = function(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const required = target - nums[i];
        if (map.has(required)) {
            return [map.get(required), i];
        }
        map.set(nums[i], i);
    }
};
