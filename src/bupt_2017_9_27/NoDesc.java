package bupt_2017_9_27;

/**
 * Created by waiting on 2017/9/27.
 */
public class NoDesc {
    public static boolean oneModify(int nums[]) {
        if(nums.length == 0 || nums.length == 1 || nums.length == 2)
            return true;
        int minMax = nums[0],time = 0,copy[] = new int[nums.length+1];
        for(int i = 1;i<copy.length;i++)
            copy[i] = nums[i-1];
        copy[0] = copy[1];
        for(int i = 2;i<copy.length;i++) {
            if(copy[i] >= copy[i-1])
                continue;
            else {
                if(copy[i] >= copy[i-2]) {
                    if(time != 0)
                        return false;
                    copy[i-1] = copy[i-2];
                    time++;
                }
                else {
                    if(time != 0)
                        return false;
                    copy[i] = copy[i-1];
                    time++;
                }
            }
        }
        return true;
    }


    public static void main(String[] args) {
        int a[] = {3,4,2,3};
        System.out.println(oneModify(a));
    }
}
