package bupt_2017_9_26;

/**
 * Created by waiting on 2017/9/26.
 */
public class LongestMatPara {
    /**

     */
    public static int test1(char[] bras) {
        int[] prefix = tr(bras);
        int res = 0;
        for(int i = 0;i<prefix.length -1;i++) {
            for(int j = i +1;j<prefix.length;j++) {
                if(prefix[j] - prefix[i] == 0) {
                    if(bras[i] == '(' && !isRightMoreThanLeft(prefix,i,j))
                        res = Math.max(res,j - i);
                }
            }
        }
        return res;
    }

    public static int[] tr(char[] bra) {
        int[] res = new int[bra.length];
        for(int i =0;i<bra.length;i++) {
            res[i] = (bra[i] == '(') ? 1 : -1;
        }
        int[] res1 = new int[bra.length+1];
        for(int i = 1;i<res.length;i++) {
            res1[i] += res1[i-1] + res[i-1];
        }
        return res1;
    }

    public static void main(String[] args) {
        String bra = IO.readFile("bra.txt","utf-8");
        System.out.println(test1(bra.toCharArray()));
    }

    public static boolean isRightMoreThanLeft(int[] prefix,int st,int en) {
        for(int i = st +1;i<=en;i++) {
            if(prefix[i] - prefix[st] == -1)
                return true;
        }
        return false;
    }
}
