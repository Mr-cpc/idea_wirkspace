package bupt_2017_10_09;

/**
 * Created by waiting on 2017/10/9.
 */
public class AltB {
    public static boolean altB(int n) {
        int i = 30;
        while(i > 0 && ((n >> i) & 1) == 0)
            i--;
        boolean switcher = false;//
        while(i >= 0){
            if( ( (n >> i & 0x1) ^ (switcher?1:0) ) == 0)
                return false;
            switcher = !switcher;
            i--;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(altB(5));
    }
}
