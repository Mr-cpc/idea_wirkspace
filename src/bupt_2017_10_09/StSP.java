package bupt_2017_10_09;

import java.util.*;

/**
 * Created by waiting on 2017/10/9.
 */
public class StSP {
    public static int stisp(String[] ws, String t) {
        Map<Character, Integer> map = new HashMap<>(), maps[] = new Map[ws.length];
        for (char ch : t.toCharArray())
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        for (int i = 0; i < ws.length; i++) {
            maps[i] = new HashMap<>();
            for (char ch : ws[i].toCharArray()) {
                maps[i].put(ch, maps[i].getOrDefault(ch, 0) + 1);
            }
        }
        Queue<Status> q = new LinkedList<>();
        q.offer(new Status(0, map));
        while (!q.isEmpty()) {
            Status cur = q.poll();
            if (cur.map.size() == 0)
                return cur.step;
            else {
                Map<Character, Integer> m = findClosest(cur.map, maps);
//                    Map<Character,Integer> copy = new HashMap<>(cur.map);
                for (Map.Entry<Character, Integer> me : m.entrySet()) {
                    Character key = me.getKey();
                    Integer val = me.getValue(), curVal = cur.map.get(key);
                    if (curVal != null) {
                        if (curVal > val)
                            cur.map.put(key, curVal - val);
                        else
                            cur.map.remove(key);

                    }
                }
                q.offer(new Status(cur.step + 1, cur.map));
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String[] ws = {"with", "example", "science"};
        String t = "thehat";
        TimeStatistics.begin();
        System.out.println(stisp(ws, t));
        System.out.println(TimeStatistics.end());
    }

    public static Map<Character, Integer> findClosest(Map<Character, Integer> target, Map<Character, Integer>[] maps) {
        int num = 0, max = 0;
        Map<Character, Integer> ans = maps[0];
        for (Map<Character, Integer> m : maps) {
            num = 0;
            for (Map.Entry<Character, Integer> me : target.entrySet()) {
                if (m.get(me.getKey()) != null)
                    num += me.getValue() <= m.get(me.getKey()) ? me.getValue() : m.get(me.getKey());
            }
            if (num >= max) {
                ans = m;
                max = num;
            }

        }
        return ans;
    }

}


class Status {
    int step;
    Map<Character, Integer> map;

    public Status(int step, Map<Character, Integer> map) {
        this.step = step;
        this.map = map;
    }
}

class MyPriorityQueue<T> {
    PriorityQueue<T> q;

    public MyPriorityQueue(Comparator<T> comparator) {
        this.q = new PriorityQueue<T>(comparator);
    }

    public void setComparator(Comparator<T> comparator) {
        PriorityQueue<T> t = q;
        q = new PriorityQueue<T>(comparator);
        while (!t.isEmpty()) {
            q.add(t.poll());
        }
    }
}