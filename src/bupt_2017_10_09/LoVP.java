package bupt_2017_10_09;

import bupt_2017_9_26.IO;

import java.awt.*;
import java.io.IOException;
import java.util.Stack;

/**
 * Created by waiting on 2017/10/9.
 */
public class LoVP {
    public static int lovp(String pa) {
        int res = 0,cur = 0;
        Stack<Character> s = new Stack<>();
        for(char c:pa.toCharArray() ) {
            if(isL(c))
                s.push(c);
            else {
                if(s.isEmpty()) {
                    res = Math.max(res,cur);
                    cur = 0;
                }
                else {
                    s.pop();
                    cur += 2;
                }
                res = Math.max(cur,res);
            }
        }
        return res;
    }


    public static void main(String[] args) throws IOException {
        System.out.println(lovp(IO.readFile("bra.txt")));
    }


    private static boolean isL(char c) {
        return c == '(';
    }
    private static boolean isR(char c) {
        return c == ')';
    }
}
