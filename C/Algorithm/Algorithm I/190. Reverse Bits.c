uint32_t reverseBits(uint32_t n) {
    int result = 0;
    
    for (int index = 31; index > 0; index--) {
        result = (result + (n & 1)) * 2;
        n >>= 1;
    }

    result = (result + (n & 1));
    return result;
}
