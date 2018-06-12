package bupt_2018_6_12;

import java.util.Arrays;
import java.util.LinkedList;

/**
 * Created by waiting on 2018/6/12.
 */
public class NextElement2 {
    public int[] findNext(int[] A, int n) {
        LinkedList<Integer> stk = new LinkedList<>();
        LinkedList<Integer> tmp = new LinkedList<>();
        int[] ans = new int[n];
        Arrays.fill(ans,-1);
        stk.push(A[n-1]);
        for (int i = n - 2;i>=0;i--) {
            if (stk.peek() > A[i]) {
                ans[i] = stk.peek();
                stk.push(A[i]);
            }
            else {
                while (!stk.isEmpty() && stk.peek() <= A[i])
                    tmp.push(stk.pop());
                if (!stk.isEmpty())
                    ans[i] = stk.peek();
                else
                    ans[i] = -1;
                stk.push(A[i]);
                while (!tmp.isEmpty())
                    stk.push(tmp.pop());
            }
        }
        return ans;
    }
}
