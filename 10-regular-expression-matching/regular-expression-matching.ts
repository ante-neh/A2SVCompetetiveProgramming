function isMatch(s: string, p: string): boolean {
  const memo:boolean[][] = []

  function isMatchDp(i:number, j:number):boolean{
      if(getMemo(i, j) !== undefined){
          return getMemo(i, j)
      }

      if(i < s.length && j === p.length){ 
          return setMemo(i, j, false)
          }

      if(i === s.length && j === p.length) {
          return setMemo(i, j, true)
        }

    if(p[j + 1] === "*"){
        if(matchFirstChar(i, j)){
            return setMemo(i, j, isMatchDp(i + 1, j) || isMatchDp(i, j + 2))
        }

        return setMemo(i, j, isMatchDp(i, j + 2))
    }

    if(matchFirstChar(i, j)){
        return setMemo(i, j, isMatchDp(i + 1,  j + 1))
    }


    return setMemo(i, j, false)

  }

  function getMemo(i:number, j:number):boolean{
      return memo?.[i]?.[j]
  }


  function setMemo(i:number, j:number, val:boolean):boolean{
      if(memo[i] === undefined){
          memo[i] = []
      }
      memo[i][j] = val
      return val
  }

  function matchFirstChar(i:number, j:number):boolean{
      if(s[i] === undefined) return false
      if(p[j] === ".") return true

      return s[i] === p[j]
  }

  return isMatchDp(0, 0)
}