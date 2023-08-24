function maxValue(valueA: number, valueB: number): number {
    return valueA > valueB ? valueA : valueB;
}

function lengthOfLongestSubstring(s: string): number {
    const stringLength: number = s.length;
    let longestSubstring: number = 0;
    
    let startPointer: number = 0;

    const characterMap: Map<string, number> = new Map();

    for (let endPointer: number = 0; endPointer < stringLength; endPointer++) {
        const currentChar: string = s[endPointer];

        if (characterMap.has(currentChar) && characterMap.get(currentChar) >= startPointer)
            startPointer = characterMap.get(currentChar) + 1;
    
        longestSubstring = maxValue(longestSubstring, endPointer - startPointer + 1);

        characterMap.set(currentChar, endPointer);
    }

    return longestSubstring;
};
