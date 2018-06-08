package bupt_2018_6_8;

/**
 * Created by waiting on 2018/6/8.
 */
public class IEEETest {
    public static void main(String[] args) {
        IEEE754 num = new IEEEFloat(0.1f);
        System.out.println(num);
        System.out.println(new IEEEFloat(-2.7f));
        System.out.println(new IEEEFloat(5.5f));
    }
}