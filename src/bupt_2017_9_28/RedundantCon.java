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
            if(canBeToplog(new ArrayList<>(gra) ,g.length))
                return g[i];
            gra.add(tmp);
        }
        return g[0];
    }
    //
    private static boolean canBeToplog(List<List<Integer>> gra,int num) {
        Set<Integer> set = new HashSet<>();
        while(set.size() != num) {
            Map<Integer,Integer> deg = calDeg(gra);
            Integer nod = hasOneDegNod(deg);
            if(nod == null) {
                if(set.size() != num)
                    return false;
            }
            else {
                set.add(nod);
                if(set.size() == num -1)
                    return true;
                remove(gra,nod);
            }
        }
        return true;
    }

    private static void remove(List<List<Integer>> gra, Integer nod) {
        for(int i = 0;i<gra.size();i++) {
            if(gra.get(i).get(0) == nod || gra.get(i).get(1) == nod)
                gra.remove(i);
        }
    }

    private static Integer hasOneDegNod(Map<Integer,Integer> map) {
        for(Map.Entry<Integer,Integer> me :map.entrySet()) {
            if(me.getValue() == 1)
                return me.getKey();
        }
        return null;
    }
    private static Map<Integer,Integer> calDeg(List<List<Integer>> gra) {
        Map<Integer,Integer> deg = new LinkedHashMap<>(gra.size() + 1);
        for(int i = 0,size = gra.size();i<size;i++) {
            int edge1 = gra.get(i).get(0),edge2 = gra.get(i).get(1);
            deg.put(edge1,deg.getOrDefault(edge1,0)+1);
            deg.put(edge2,deg.getOrDefault(edge2,0)+1);
        }
        return deg;
    }
    private static List<Integer> arrayToList(int[] arr) {
        List<Integer> list = new ArrayList<>(arr.length);
        for(int i:arr)
            list.add(i);
        return list;
    }

    public static void main(String[] args) {
        int[][] g = {{1,2},{2,3},{3,4},{1,4},{1,5}};
        int gg[][] = {{1,2},{2,3},{3,4},{1,5}};
        List<List<Integer>> list = new LinkedList<>();
        for(int[] arr:gg)
            list.add(arrayToList(arr));
        System.out.println(canBeToplog(list,5));
//        System.out.println(Arrays.toString(redundantCon(g)));
    }


}
