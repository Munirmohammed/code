class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        std::vector<int> res; // Specify the type of elements as int
        if (root == nullptr) {
            return res;
        }

        std::vector<TreeNode*> queue; // Specify the type of elements as TreeNode*
        queue.push_back(root);

        while (!queue.empty()) {
            int maxVal = INT_MIN;
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.erase(queue.begin());

                maxVal = std::max(maxVal, node->val);

                if (node->left != nullptr) {
                    queue.push_back(node->left);
                }

                if (node->right != nullptr) {
                    queue.push_back(node->right);
                }
            }

            res.push_back(maxVal);
        }

        return res;
    }
};
