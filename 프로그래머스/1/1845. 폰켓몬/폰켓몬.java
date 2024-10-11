import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> set = new HashSet<Integer>();
		for(int i : nums)
			set.add(i);
        int num_set = set.size();
        int N = (nums.length)/2;
            
        if(N > num_set){
            return num_set;
        }else{
            return N;
        }
    }
}
