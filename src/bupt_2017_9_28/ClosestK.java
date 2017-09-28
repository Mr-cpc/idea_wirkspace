package bupt_2017_9_28;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by waiting on 2017/9/28.
 */
public class ClosestK {

    public static List<Integer> closestK(int nums[],int k,int x) {
        List<Integer> res = new ArrayList<>(k);
        if(x <= nums[0]) {
            for(int i = 0;i<k;i++)
                res.add(nums[i]);
        }
        else {
            if(x >= nums[nums.length - 1]) {
                for(int i = 1;i<=k;i++)
                    res.add(nums[nums.length - i]);
                Collections.reverse(res);
            }
            else {
                int idx = closest(nums,x),i = idx - 1,j =  idx + 1,count = 1;
                res.add(nums[idx]);
                while(count < k && i >= 0 && j < nums.length) {
                    if(x - nums[i] <= nums[j] -x ) {
                        res.add(0,nums[i--]);
                    }
                    else {
                        res.add(res.size(),nums[j++]);
                    }
                    count++;
                }
                if(count >= k)
                    return res;
                else {
                    if(i < 0) {
                        while(count++ < k)
                            res.add(nums[j++]);
                    }
                    else {
                        while(count ++ < k)
                            res.add(0,nums[i--]);
                    }
                }
            }
        }
        return  res;
    }

    public static int closest(int nums[],int x) {
        for(int i = 0;i<nums.length - 1;i++) {
            if(nums[i] < x && nums[i+1] >= x)
                return nums[i+1] - x <= x - nums[i]? i+1:i;
        }
        return nums.length - 1;
    }

    public static void main(String[] args) {
        int a[] = {0,1,2,2,2,3,6,8,8,9};
        System.out.println(closest(a,0));
        System.out.println(closestK(a,5,9));
    }

}
