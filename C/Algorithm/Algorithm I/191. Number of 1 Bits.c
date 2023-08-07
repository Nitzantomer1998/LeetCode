int hammingWeight(uint32_t n) {
    int oneCounter = 0;

    for (int index = 32; index > 0; index--) {
        if (n & 1)
            oneCounter++;

        n >>= 1;
    }

    return oneCounter;
}
