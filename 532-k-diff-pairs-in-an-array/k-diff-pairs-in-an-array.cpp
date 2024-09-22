class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        vector<int> v;
        unordered_map<int, int> mp, unique;
        int counter = 0;

        if(k == 0) {
            for(int it: nums)
                unique[it]++;
            
            for(auto it: unique)
                if(it.second > 1)
                    counter++;
            
            return counter;
        }
        for(int it: nums)
            unique[it] = 1;
        
        for(int i = 0; i < nums.size(); i++)
            if(unique[nums[i]] == 1)
                unique[nums[i]] = 0;
            else    
                nums[i] = -1e9;

        for(int it: nums)
            if(it != -1e9)
                v.push_back(it);

        for(int it: v) {
            int  above = it + k, below = it - k;

            if(mp.find(above) != mp.end())
                counter++;
            if(mp.find(below) != mp.end())
                counter++;
            
            mp[it]++;
        }

        return counter;
    }
};