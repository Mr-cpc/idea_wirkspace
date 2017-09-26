/**
 * Created by waiting on 2017/9/26.
 */
public class LongContigious {
    public static int test1(int nums[]) {
        if(nums.length == 0 )
            return 0;
        int res = 1,tmp = 1;
        for(int i = 1;i<nums.length;i++) {
            if(nums[i-1] < nums[i])
                tmp++;
            else {
                res = Math.max(tmp,res);
                tmp = 1;
            }
        }
        return Math.max(tmp,res);
    }

    public static void main(String[] args) {
        int a[] = {3,2,5,8,6,88,99,999};
        System.out.println(LongContigious.test1(a));
    }
}
