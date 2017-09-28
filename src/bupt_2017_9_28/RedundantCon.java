package bupt_2017_9_28;

import java.util.*;

/**
 * Created by waiting on 2017/9/28.
 */
public class RedundantCon {
    public static int[] redundantCon(int[][] g) {
        List<List<Integer>> gra = new ArrayList<>(g.length);
        for(int[] i:g)
            gra.add(arrayToList(i));
        for(int i = g.length -1;i >= 0;i--) {
            List<Integer> tmp = gra.remove(i);
            if(canBeToplog(gra))
                return g[i];
            gra.add(tmp);
        }
        return g[0];
    }

    private static boolean canBeToplog(List<List<Integer>> gra) {
        Map<Integer,Integer> deg = new LinkedHashMap<>(gra.size() + 1);
        for(int i = 0,size = gra.size();i<size;i++) {
            int edge1 = gra.get(i).get(0),edge2 = gra.get(i).get(1);
            deg.put(edge1,deg.getOrDefault(edge1,0)+1);
            deg.put(edge2,deg.getOrDefault(edge2,0)+1);
        }
        int countDegsEquals1 = 0;
        for(Map.Entry<Integer, Integer> me :deg.entrySet()) {
            int no = me.getKey(),degs = me.getValue();
            if(degs == 0)
                return false;
            else {
                if(degs == 1)
                    countDegsEquals1++;
            }
        }
        return countDegsEquals1 == 2;
    }

    private static List<Integer> arrayToList(int[] arr) {
        List<Integer> list = new ArrayList<>(arr.length);
        for(int i:arr)
            list.add(i);
        return list;
    }

    public static void main(String[] args) {
        int[][] g = {{1,2},{2,3},{3,4},{1,4},{1,5}};
        System.out.println(Arrays.toString(redundantCon(g)));
    }

}
