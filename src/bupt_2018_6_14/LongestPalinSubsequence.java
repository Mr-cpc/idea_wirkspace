package bupt_2018_6_14;

import java.util.Arrays;

/**
 * Created by waiting on 2018/6/14.
 */
public class LongestPalinSubsequence {
    public int longestPalinSubseq(String s) {
        int len = s.length();
        int[][] dp = new int[len][len];
        for (int i = 0;i < len;i++)
            dp[i][i] = 1;
        int i = 0,j = 1;
        while (j < len) {
            for (int k = 0;k < len - j;k++)
                dp[i + k][j + k] = s.charAt(i + k) == s.charAt(j + k) ?
                        dp[i + k + 1][j + k - 1] + 2 : Math.max(dp[i + k + 1][j + k],dp[i + k][j + k -1]);
            j++;
        }
        return dp[0][len-1];
    }

    public static void main(String[] args) {
        new LongestPalinSubsequence().longestPalinSubseq("adghbebja");
    }
}
