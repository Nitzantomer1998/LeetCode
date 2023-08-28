function reverseWords(s: string): string {
    const words: string[] = s.split(' ');

    for (let index = 0; index < words.length; index++)
        words[index] = words[index].split('').reverse().join('');

    return words.join(' ');
};
