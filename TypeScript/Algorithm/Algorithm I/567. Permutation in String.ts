function checkInclusion(s1: string, s2: string): boolean {
    const sOneLength: number = s1.length;
    const sTwoLength: number = s2.length;

    const stringOneContent: number[] = new Array(26).fill(0);
    const stringTwoContent: number[] = new Array(26).fill(0);

    for (let index: number = 0; index < sOneLength; index++) {
        stringOneContent[s1.charCodeAt(index) - 97]++;
        stringTwoContent[s2.charCodeAt(index) - 97]++;
    }

    for (let index: number = sOneLength; index < sTwoLength; index++) {
        if (stringOneContent.every((count, i) => count === stringTwoContent[i]))
            return true;

        const charToAdd: number = s2.charCodeAt(index) - 97;
        const charToRemove: number = s2.charCodeAt(index - sOneLength) - 97;

        stringTwoContent[charToAdd]++;
        stringTwoContent[charToRemove]--;
    }

    return stringOneContent.every((count, i) => count === stringTwoContent[i]);
}
