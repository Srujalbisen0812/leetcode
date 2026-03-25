/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr
        .map(x => [fn(x), x])
        .sort((a, b) => a[0] - b[0])
        .map(x => x[1]);
};