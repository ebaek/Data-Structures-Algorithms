var canFinish = function (numCourses, arr) {
    const graph = {};
    let preReq = true;

    for (let i = 0; i < arr.length; i++) {
        if (!graph[arr[i][0]]) graph[arr[i][0]] = [];
        graph[arr[i][0]].push(arr[i][1]);
    }

    flagged = new Set();
    const memo = {};

    const graphArr = Object.keys(graph);
    for (let i = 0; i < graphArr.length; i++) {
        if (dfs(graph, graphArr[i], flagged, memo) === false) {
            return false;
        }
    }

    return preReq;
};

var dfs = function (graph, classSelect, flagged, memo = {}) {
    if (graph[classSelect] === undefined) return true;
    if (flagged.has(classSelect)) return false;
    if (classSelect in memo) { return memo[classSelect] }

    let pre = true;
    flagged.add(classSelect);

    for (let i = 0; i < graph[classSelect].length; i++) {
        let copy = new Set(flagged);
        const req = graph[classSelect][i];

        const test = dfs(graph, req, copy, memo);
        if (!test) return false;
    }
    memo[classSelect] = true;
    return memo[classSelect];
}