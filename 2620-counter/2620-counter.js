/**
 * @param {number} n
 * @return {Function} counter
 */

var createCounter = function(n) {
    let cnt = 0;
    return function() {

        let answer = n+cnt;
        cnt += 1
        return answer
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */