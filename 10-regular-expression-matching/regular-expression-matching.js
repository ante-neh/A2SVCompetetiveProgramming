/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const memo = []
    function isMatch(i, j){
        if (memo[i] && memo[i][j] !== undefined){
            return memo[i][j]
        }

        if(j === p.length){
            return i === s.length
        }

        if(p[j + 1] === '*'){
            if(matchFirstChar(i, j)){
                return setMemo(i, j, isMatch(i + 1, j) || setMemo(i, j, isMatch(i, j + 2)))
            }

            return setMemo(i, j, isMatch(i, j + 2))
        }

        if(matchFirstChar(i, j)){
            return setMemo(i, j, isMatch(i + 1, j + 1))
        }

        return setMemo(i, j, false)
    }

    function setMemo(i, j, val){
        if(memo[i] === undefined){
            memo[i] = []
        }

        memo[i][j] = val
        return val
    }

    function matchFirstChar(i, j){
        if(s[i] === undefined){
            return false
        }
        if(p[j] === '.'){
            return true
        }

        return s[i] === p[j]
    }

    return isMatch(0, 0)
};