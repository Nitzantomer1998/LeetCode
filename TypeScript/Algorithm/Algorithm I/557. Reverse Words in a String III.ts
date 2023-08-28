/**
 * Reverses each word in a given string while keeping the word order intact.
 * @param {string} s - The input string containing words.
 * @returns {string} The string with reversed words.
 */
function reverseWords(s: string): string {
    const words: string[] = s.split(' ');

    for (let index = 0; index < words.length; index++)
        words[index] = words[index].split('').reverse().join('');

    return words.join(' ');
};
