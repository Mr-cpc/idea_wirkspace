package bupt_2017_9_27;

/**
 * Created by waiting on 2017/9/27.
 */
public class MaxTr {
    public static TreeNode maxTr(int[] nums) {
        return reConstruct(nums,0,nums.length -1);
    }

    public static TreeNode reConstruct(int[] nums,int start,int end) {
        if(start == end)
            return new TreeNode(nums[start]);
        if(start > end)
            return null;
        int idx = findMax(nums,start,end);
        TreeNode t = new TreeNode(nums[idx]);
        t.l = reConstruct(nums,start,idx-1);
        t.r = reConstruct(nums,idx +1,end);
        return t;
    }
    private static int findMax(int[] nums,int start,int end) {
        int idx = start,max = Integer.MIN_VALUE;
        for (int i = start; i < end; i++) {
            if (nums[i] > max) {
                max = nums[i];
                idx = i;
            }
        }
        return idx;
    }
    public static void trav(TreeNode t) {
        if(t != null) {
            System.out.println(t.val);
            trav(t.l);
            trav(t.r);
        }
    }

    public static void main(String[] args) {
        int[] a = {3,2,1,6,0,5};
        TreeNode t = maxTr(a);
        trav(t);
    }


















    private static class TreeNode {
        int val;

        public TreeNode(int val) {
            this.val = val;
        }

        TreeNode l,r;
    }
}
