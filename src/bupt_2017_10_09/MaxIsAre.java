package bupt_2017_10_09;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/**
 * Created by waiting on 2017/10/9.
 */
public class MaxIsAre {
    public static int maxIsA(int[][] bo) {
        int res = 0,curMax = 0;
        Set<Point> set = new HashSet<>();
        Queue<Point> q = new LinkedList<>();
        for(int i = 0;i<bo.length;i++) {
            for(int j = 0;j<bo[0].length;j++) {
                if(bo[i][j] == 0)
                    continue;
                Point p = new Point(i,j);
                if(!set.contains(p)) {
                    q.offer(p);
                    curMax = 0;
                    while(!q.isEmpty()) {
                        Point cur = q.poll();
                        if(set.contains(cur))
                            continue;
                        curMax++;
                        set.add(cur);
                        int[] xx = {cur.x -1,cur.x + 1},yy = {cur.y-1,cur.y+1};
                        for(int x:xx) {
                            if(x >= 0 && x < bo.length && bo[x][cur.y] == 1) {
                                Point next = new Point(x,cur.y);
                                if(!set.contains(next))
                                    q.offer(next);
                            }
                        }
                        for(int y:yy) {
                            if(y >= 0 && y < bo[0].length && bo[cur.x][y] == 1) {
                                Point next = new Point(cur.x,y);
                                if(!set.contains(next))
                                    q.offer(next);
                            }
                        }
                    }
                    res = Math.max(res,curMax);
                }

            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[][] bo = {{1,0,0},{1,1,1},{1,1,1}};
        System.out.println(maxIsA(bo));
    }

}

class Point {
    int x,y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Point point = (Point) o;

        if (x != point.x) return false;
        return y == point.y;
    }

    @Override
    public int hashCode() {
        int result = x;
        result = 31 * result + y;
        return result;
    }

}