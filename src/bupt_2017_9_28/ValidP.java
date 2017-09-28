package bupt_2017_9_28;

/**
 * Created by waiting on 2017/9/28.
 */
public class ValidP {
    public static boolean va(String str) {
        char[] cc = str.toCharArray();
        StringBuilder sb = new StringBuilder();
        for(char c:cc) {
            if(Character.isLetterOrDigit(c))
                sb.append(c);
        }
        return isPalin(sb.toString().toCharArray());
    }

    private static boolean isPalin(char[] chars) {
        int mid = chars.length / 2,dif = 0;
        for (int i = 0; i <= mid; i++) {
            if(Character.isLetter(chars[i])) {
                if(Character.isLetter(chars[chars.length - 1- i])) {
                    dif = Math.abs((int)(chars[i] - chars[chars.length - 1- i]));
                    if(dif != 32 && dif != 0)
                        return false;
                }
                else
                    return false;
            }
            else {
                if(Character.isLetter(chars[chars.length - 1- i]))
                    return false;
                else {
                    if(chars[i] != chars[chars.length - 1 - i])
                        return false;
                }
            }
        }
        return true;
    }

    public static boolean isChar(char c) {
        return Character.isLowerCase(c) || Character.isUpperCase(c);
    }

    public static void main(String[] args) {
        System.out.println(va("\"7Ci`rd,9X;;r9,dX`iC7\""));
    }
}
