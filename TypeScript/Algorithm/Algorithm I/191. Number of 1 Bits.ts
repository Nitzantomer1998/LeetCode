function hammingWeight(n: number): number {
    let oneBitCounter: number = 0;

    for (let _: number = 0; _ < 32; _++) {
        oneBitCounter += n & 1;
        n >>= 1;
    }

    return oneBitCounter;
};
