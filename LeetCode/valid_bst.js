// 98. Validate Binary Search Tree

var isValidBST = function(root) {
    if(!root) return true;
    
    function helper(min, max, root) {
        if(!root) return true;
        
        if(min !== null && min >= root.val || max !== null && max <= root.val) return false;
        
        return helper(min, root.val, root.left) && helper(root.val, max, root.right);
    }
    
    return helper(null, null, root);
};