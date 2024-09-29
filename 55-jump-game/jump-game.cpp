class Solution {
public:
    vector<int> dp;
    int n;

    bool helper(vector<int>& nums, int index) {
        if(index == n - 1)
            return true;
        
        if(nums[index] == 0)
            return false;
        
        if(dp[index] != -1)
            return dp[index];
    
        for(int i = 1; i <= nums[index]; i++)
            if(helper(nums, index + i))
                return dp[index] = true;

        return dp[index] = false;
    }

    bool canJump(vector<int>& nums) {
        n = nums.size();
        dp.resize(n, -1);

        return helper(nums, 0);
    }
};