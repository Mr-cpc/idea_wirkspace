package bupt_2017_9_28;

/**
 * Created by waiting on 2017/9/28.
 */
public class ValidPa2 {
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

    public static void main(String[] args) {
        System.out.println(va2("abca"));
    }
}
