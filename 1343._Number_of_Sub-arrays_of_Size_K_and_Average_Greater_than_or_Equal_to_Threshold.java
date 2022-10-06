class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int N = arr.length;
        int l = 0;
        int res = 0;
        int sums = 0;
        
        for(int r=0; r < N; r++){
            if ((r - l + 1) < k ){
                sums += arr[r];
                continue;
            }
            
            sums += arr[r];
            if ((sums / k) >= threshold){
                res += 1;
            }
            sums -= arr[l];
            l += 1;
        }
        return res;
    }
}
