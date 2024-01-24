function isMatch(s: string, p: string): boolean {
    const memo:boolean[][] = []

    function dp(i:number, j:number):boolean{
        if(memo[i] && memo[i][j] !== undefined){
            return memo[i][j]
        }

        if(j === p.length){
            return i === s.length
        }

        const firstMatch = i < s.length && (p[j] === s[i] || p[j] === '?')

        if(p[j] === '*'){
            const matchEmpty = dp(i, j + 1)
            const matchOne = i < s.length && dp(i + 1, j)
            memo[i] = memo[i] || []
            memo[i][j] = matchEmpty || matchOne
        }else{
            memo[i] = memo[i] || []
            memo[i][j] = firstMatch && dp(i + 1, j + 1)
        }

        return memo[i][j]
    }

    return dp(0, 0)
};