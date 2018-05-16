package bupt_2018_5_11;

/**
 * Created by waiting on 2018/5/11.
 */
public class ThreadLocalPrac {
    static ThreadLocal<Long>  tl1 = new ThreadLocal<>();
    static ThreadLocal<Long>  tl2 = new ThreadLocal<>();
    StringBuffer s;
    public static void main(String[] args) {
        long l = System.currentTimeMillis();
        tl1.set(l);
        tl2.set(l);
        System.out.println(tl1.get());
        System.out.println(tl2.get());
    }
}
