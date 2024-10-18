/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(!root)
            return {};

        vector<vector<int>> res;
        queue<TreeNode*> q;
        q.push(root);
        res.push_back({root->val});
        bool isEven = false;

        while(!q.empty()){
            queue<TreeNode*> q1;
            vector<int> ans;

            while(!q.empty()) {
                TreeNode* node = q.front();
                cout<<node->val<<" ";
                if(node->left) {
                    q1.push(node->left);
                    ans.push_back(node->left->val);
                }
                
                if(node->right){
                    q1.push(node->right);
                    ans.push_back(node->right->val);
                }
                
                q.pop();
            }

            if(!isEven) {
                reverse(ans.begin(), ans.end());
                isEven = true;
            }
            else 
                isEven = false;
            
            if(!q1.empty()) {
                res.push_back(ans);
                q = q1;
            }
        }

        return res;
    }
}; 