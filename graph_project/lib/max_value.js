function maxValue(node, visited=new Set()) {
    if(visited.has(node)) return -Infinity;

    visited.add(node);

    let maxNeighbors = node.neighbors.map( (neighbor) => maxValue(neighbor, visited));
    return Math.max(node.val, ...maxNeighbors);
}

module.exports = {
    maxValue
};