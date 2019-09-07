// View the full problem and run the test cases at:
//  https://leetcode.com/problems/course-schedule/

function canFinish(numCourses, prerequisites) {
    
};

function depthFirst(node, graph, visited = new Set()) {
    if(visited.has(node)) return;

    visited.add(node);

    graph.neighbors.forEach( neighbor => depthFirst(neighbor, graph, visited));
    return true;
}; 
