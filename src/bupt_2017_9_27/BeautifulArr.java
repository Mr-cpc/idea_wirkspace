package bupt_2017_9_27;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by waiting on 2017/9/27.
 */
public class BeautifulArr {
    public static List<Integer> beautiful(int n,int k) {
        List<Integer> res = new ArrayList<>(n);
        int i = 1,j = n,count = 0,flag = 0;
        //规定奇数加小的，偶数加大的
        while(count++ < k) {
            if(isOdd(flag++))
                res.add(i++);
            else
                res.add(j--);
        }
        //如果刚才加的是j，也就是大的
        int rem = n-k;
        if(isOdd(flag)) {
            while(rem-- > 0)
                res.add(j--);
        }
        else {
            while(rem-- > 0)
                res.add(i++);
        }
        return res;
    }
    private static boolean isOdd(int num) {
        return (num & 0x1) == 1;
    }


    public static void main(String[] args) {
        System.out.println(beautiful(2,1));
    }
}
