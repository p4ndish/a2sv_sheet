class Solution {
    public int longestSubarray(int[] nums) {
        int k = 0;
        int res = 0;
        int l = 0;
        
        for(int r=0; r<nums.length; r++){
            if (nums[r] == 0){
                k += 1;
            }
            if (k == 2){
                res = Math.max(res, (r-l)-1);
                while (nums[l] != 0 && l <= r){
                    l += 1;
                }
                k = 1;
                l += 1;
                
            }
            res = Math.max(res, (r-l));
        }
        return res;
    }
}
