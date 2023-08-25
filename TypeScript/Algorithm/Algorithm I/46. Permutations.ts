function permute(nums: number[]): number[][] {
    const numsLength: number = nums.length;
    const permutatedArray: number[][] = [[nums[0]]];

    for (let index: number = 1; index < numsLength; index++) {
        permutatedArray.forEach(item => {
            const currentLength: number = item.push(nums[index]);

            for (let j = currentLength - 1; j > 0; j--) {
                item = item.slice();
                item[j] = item[j - 1];
                item[j - 1] = nums[index];
                permutatedArray.push(item);
            }
        });
    }
    
    return permutatedArray;
};
