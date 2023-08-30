function climbStairs(n: number): number {
    let previousClimb: number = 1;
    let currentClimb: number = 2;
    let nextClimb: number = 0;

    for (let currentStair: number = 2; currentStair < n; currentStair++) {
        nextClimb = currentClimb + previousClimb;

        previousClimb = currentClimb;
        currentClimb = nextClimb;
    }

    return n < 3 ? n : nextClimb;
};
