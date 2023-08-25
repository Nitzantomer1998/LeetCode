/**
 * Reverses an array of characters in-place.
 * @param {string[]} s - The array of characters to be reversed.
 * @returns {void}
 */
function reverseString(s: string[]): void {
    const stringLength: number = s.length;

    for (let index: number = 0; index < stringLength / 2; index++) {
        const tempChar: string = s[index];

        s[index] = s[stringLength - index - 1];
        s[stringLength - index - 1] = tempChar;
    }
};
