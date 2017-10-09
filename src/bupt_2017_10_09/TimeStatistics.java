package bupt_2017_10_09;

/**
 * Created by waiting on 2017/10/9.
 */
public class TimeStatistics {
    private static ThreadLocal<Long> TIME = new ThreadLocal<>();

    public static void begin() {
        TIME.set(System.currentTimeMillis());
    }
    public static Long end() {
        return System.currentTimeMillis() - TIME.get();
    }
}
