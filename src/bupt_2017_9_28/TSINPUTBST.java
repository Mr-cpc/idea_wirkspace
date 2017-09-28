package bupt_2017_9_28;

import sun.reflect.generics.tree.Tree;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * Created by waiting on 2017/9/28.
 */
public class TSINPUTBST {
    public static boolean ex(TreeNode root,int k) {
        Stack<TreeNode> stack = new Stack<>();
        if(root == null)
            return false;
        List<Integer> list = new LinkedList<>();

        while(root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            list.add(root.val);
            root = root.right;
        }

        return ts(list.toArray(new Integer[list.size()]), k);
    }

    private static boolean ts(Integer[] arr,int k) {
        int i = 0,j = arr.length -1,sum = 0;
        while(i < j) {
            sum = arr[i] + arr[j];
            if(sum == k)
                return  true;
            else {
                if(sum < k)
                    i++;
                else
                    j++;
            }
        }
        return false;
    }
}
























class TreeNode {
    int val;
    TreeNode left,right;

    public TreeNode(int val) {
        this.val = val;
    }
}
