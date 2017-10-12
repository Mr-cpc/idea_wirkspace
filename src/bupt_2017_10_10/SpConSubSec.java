package bupt_2017_10_10;

import java.util.Map;
import java.util.TreeMap;

/**
 * Created by waiting on 2017/10/10.
 */
public class SpConSubSec {
    public static boolean cansp(int[] nums) {
        Map<Integer,Integer> map = new TreeMap<>();
        for(int i:nums)
            map.put(i,map.getOrDefault(i,0)+1);

        return true;
    }
}
