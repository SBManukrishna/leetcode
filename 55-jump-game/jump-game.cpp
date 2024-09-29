class Solution {
public:
    vector<int> dp;
    int n;

    bool helper(vector<int>& nums, int index) {
        if(index >= n - 1)
            return true;
        
        if(dp[index] != -1)
            return dp[index];
    
        bool  res = false;

        for(int i = 1; i <= nums[index]; i++){
            res = helper(nums, index + i);
            dp[index] = res;
            if(res)
                break;
        }

        dp[index] = res;
        return dp[index];
    }

    bool canJump(vector<int>& nums) {
        n = nums.size();
        dp.resize(n, -1);

        return helper(nums, 0);
    }
};