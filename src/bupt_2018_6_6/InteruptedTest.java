package bupt_2018_6_6;

import java.util.Scanner;

/**
 * Created by waiting on 2018/6/6.
 */
public class InteruptedTest {
    public static void main(String[] args) {
        test();

    }

    private static void test() {
        Thread t = new Thread(()->{
            while (true) {
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    System.out.println("be interrupted while sleeping!");
                    break;
                }
            }
        });
        t.start();
        Scanner sc = new Scanner(System.in);
        String line = null;
        while (!(line = sc.nextLine()).equals("exit") ) {
            System.out.printf("you input is %s\n",line);
        }
        t.interrupt();
    }
}
