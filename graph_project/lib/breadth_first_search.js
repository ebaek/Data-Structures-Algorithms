
// breadth first search at each level
// after searching through all the children, search again through all the children

function breadthFirstSearch(startingNode, targetVal) {
    let visited = new Set();

    let queue = [startingNode];

    while(queue.length) {
        // take out the node
        let node = queue.shift();
        // check to see if the node has been visited; if it has go onto the next node
        if(visited.has(node)) continue;
        // add the node to visited (set only maintains unique values)
        visited.add(node);

        // check if the node's value matches the target
        if(node.val === targetVal) return node;
        // push the neighbors onto the queue
        queue.push(...node.neighbors);
    }

    return null;
}

module.exports = {
    breadthFirstSearch
};