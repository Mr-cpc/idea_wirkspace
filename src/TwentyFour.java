import sun.org.mozilla.javascript.internal.ast.ForInLoop;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by waiting on 2017/9/26.
 */
public class TwentyFour {
    /**
     * 　(1) 将4个整数放入数组中
     　　(2) 在数组中取两个数字的排列，共有 P(4,2) 种排列。对每一个排列，
     　　(2.1) 对 + - * / 每一个运算符，
     　　(2.1.1) 根据此排列的两个数字和运算符，计算结果
     　　(2.1.2) 改表数组：将此排列的两个数字从数组中去除掉，将 2.1.1 计算的结果放入数组中
     　　(2.1.3) 对新的数组，重复步骤 2
     　　(2.1.4) 恢复数组：将此排列的两个数字加入数组中，将 2.1.1 计算的结果从数组中去除掉
     * @return
     */
    public static boolean tf(int[] num) {
        List<Integer> nums = new ArrayList<>(num.length);
        for(int i:num)
            nums.add(i);
        //从4个数中取2个的排列
        List<List<Integer>> perms = two_perm(nums);

        for(List<Integer> res:perms) {
            remove(nums,res);
            List<Integer> ans = operation(res);
            for (Integer i : ans) {
                nums.add(i);
                List<List<Integer>> perms3 = two_perm(nums);
                for (List<Integer> res3 : perms3) {
                    remove(nums,res3);
                    List<Integer> ans3 = operation(res3);
                    for (Integer i2 : ans3) {
                        nums.add(i2);
                        List<List<Integer>> perms2 = two_perm(nums);
                        for (List<Integer> res2 : perms2) {
                            remove(nums,res2);
                            List<Integer> ans1 = operation(res2);
                            for (Integer finalAns : ans1)
                                if (finalAns == 24)
                                    return true;
                            add(nums,res2);
                        }
                        nums.remove(i2);
                    }
                    add(nums,res3);
                }
                nums.remove(i);
            }
            add(nums,res);
        }
        return false;
    }

    private static <E>void add(List<E> master, List<E> slave) {
        for(E e:slave)
            master.add(e);
    }

    public static <E>void remove(List<E> master,List<E> slave) {
        for(E e:slave)
            master.remove(e);
    }
    private static List<Integer> operation(List<Integer> operators) {
        List<Integer> res = new LinkedList<>();
        res.add(operators.get(0) + operators.get(1));
        res.add(operators.get(0) - operators.get(1));
        res.add(operators.get(0) * operators.get(1));
        if(operators.get(1) != 0)
            res.add(operators.get(0) / operators.get(1));
        return res;
    }
    /**
     *
     * @param nums
     * @param res
     * @param cur
     * @param n
     */
    public static void perm(List<Integer> nums,List<List<Integer>> res,List<Integer> cur,int n) {
        if(n == 0) {
            res.add(cur);
            return ;
        }
        List<Integer> copy = new ArrayList<>(nums);
        for(int i:nums) {
            cur.add(i);
            copy.remove(new Integer(i));
            perm(copy,res,new ArrayList<Integer>(cur),n-1);
            cur.remove(new Integer(i));
            copy.add(i);
        }
    }

    private static List<List<Integer>> two_perm(List<Integer> nums) {
        int size = nums.size();
        List<List<Integer>> res = new ArrayList<>(size*(size-1));
        perm(nums,res,new LinkedList<Integer>(),2);
        return res;
    }
    public static void main(String[] args) {
        List<List<Integer>> perms = new ArrayList<>();
        List<Integer> nums = Arrays.asList(new Integer[]{5,7,8,4});
//        perm(nums,perms,new ArrayList<Integer>(),1);
        System.out.println(tf(new int[]{5,7,12,4}));
//        System.out.println(perms.size());
    }













}
