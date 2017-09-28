package bupt_2017_9_28;

/**
 * Created by waiting on 2017/9/28.
 */
public class ValidP {
    public static boolean va(String str) {
        StringBuilder sb = new StringBuilder(str.trim());
        for(int i = 0;i<sb.length();i++) {
            if(!Character.isLetter(sb.charAt(i)))
                sb.deleteCharAt(i);
        }
        return isPalin(sb.toString().toCharArray());
    }

    private static boolean isPalin(char[] chars) {
        int mid = chars.length / 2,dif = 0;
        for (int i = 0; i <= mid; i++) {
            dif = Math.abs((int)(chars[i] - chars[chars.length - 1- i]));
            if(dif != 32 && dif != 0)
                return false;
        }
        return true;
    }

    public static boolean isChar(char c) {
        return Character.isLowerCase(c) || Character.isUpperCase(c);
    }

    public static void main(String[] args) {
        System.out.println(va("0P"));
    }
}
