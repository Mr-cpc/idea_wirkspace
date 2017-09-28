package bupt_2017_9_28;

/**
 * Created by waiting on 2017/9/28.
 */
public class ValidPa2 {
    //搞错了，下面这个方法是针对限制为只能修改一个字符使得串回文，而不是删除一个字符的
    public static boolean va2(String str) {
        int len = str.length();
        StringBuilder sb = new StringBuilder(2 * len + 1).append('*');
        for (char ch : str.toCharArray()) {
            sb.append(ch).append('*');
        }
        char[] chars = sb.toString().toCharArray();
        int mid = (chars.length - 1) >> 1,i = 1,allowChangeTime = 1;
        while(i <= len) {
            if(chars[mid-i] != chars[mid + i]) {
                allowChangeTime--;
                if(allowChangeTime < 0)
                    return false;
            }
            ++i;
        }
        return true;
    }


    //
    public static boolean va3(String s,int i, int j,int modifyTime) {
        if(modifyTime >1 || i >= j)
            return false;
        if(s.charAt(i) == s.charAt(j))
            return va3(s,i+1,j-1,modifyTime);
        else {
            return va3(s,i+1,j,modifyTime+1) || va3(s,i,j-1,modifyTime +1);
        }
    }
    public static void main(String[] args) {
        String s = "abca";
        System.out.println(va3(s,0,s.length() - 1,0));
    }
}
