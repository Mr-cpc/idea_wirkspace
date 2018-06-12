package bupt_2018_6_12;

import java.util.Arrays;
import java.util.LinkedList;

/**
 * Created by waiting on 2018/6/12.
 */
public class NextElement {
    public int[] findNext(int[] A, int n) {
        LinkedList<Integer> stk = new LinkedList<>();
        int[] ans = new int[n];
        Arrays.fill(ans,-1);
        stk.push(0);
        for (int i = 1; i < n;i++) {
            while (!stk.isEmpty() && A[i] > A[stk.peek()]) {
                ans[stk.pop()] = A[i];
            }
            stk.push(i);
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new NextElement().findNext(new int[]{ 2, 5, 3, 7, 1, 2, 8 },7)));
    }
}
