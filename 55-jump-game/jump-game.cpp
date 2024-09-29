class Solution {
private:
    int n;
    bool help(vector<int>& nums , vector<int>& dp , int i) {
        // base case
        if(i == n-1)    return true;
        if(i >= n)  return false;
        // memoization case
        if(dp[i] != -1) return dp[i];
        // calling recursion
        int maxJump = nums[i];
        for(int jump = 1; jump <= maxJump; jump++) {
            if(help(nums , dp , i + jump))
                return dp[i] = 1;
        }
        return dp[i] = 0;
    }
public:
    bool canJump(vector<int>& nums) {
        // using recursion and memoization
        n = nums.size();
        vector<int> dp(n , -1);
        return help(nums , dp , 0);
    }
};