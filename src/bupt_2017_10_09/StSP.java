package bupt_2017_10_09;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

/**
 * Created by waiting on 2017/10/9.
 */
public class StSP {
    public static int stisp(String[] ws,String t) {
        Map<Character,Integer> map = new HashMap<>(),maps[] = new Map[ws.length];
        for(char ch:t.toCharArray())
            map.put(ch,map.getOrDefault(ch,0)+1);
        for(int i = 0;i<ws.length;i++) {
            maps[i] = new HashMap<>();
            for(char ch:ws[i].toCharArray()) {
                maps[i].put(ch,maps[i].getOrDefault(ch,0)+1);
            }
        }
        Queue<Status> q = new LinkedList<>();
        q.offer(new Status<Character, Integer>(0,map) );
        while(!q.isEmpty()) {
            Status cur = q.poll();
            if(cur.map.size() == 0)
                return cur.step;
            else {
                for(Map<Character,Integer> m:maps) {
                    Map<Character,Integer> copy = new HashMap<>(cur.map);
                    boolean flag = false;
                    for(Map.Entry<Character,Integer> me : m.entrySet()) {
                        Character key = me.getKey();
                        Integer val = me.getValue(),curVal = copy.get(key);
                        if(curVal != null) {
                            flag = true;
                            if(curVal > val)
                                copy.put(key,curVal - val);
                            else
                                copy.remove(key);

                        }
                    }
                    if(flag)
                        q.offer(new Status(cur.step+1,copy));
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String[] ws = {"with","example","science"};
        String t = "thehat";
        TimeStatistics.begin();
        System.out.println(stisp(ws,t));
        System.out.println(TimeStatistics.end());
    }
}



class Status<K,V> {
    int step;
    Map<K,V> map;

    public Status(int step, Map<K, V> map) {
        this.step = step;
        this.map = map;
    }
}