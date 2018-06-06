package bupt_2018_6_6;

import java.util.Scanner;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Created by waiting on 2018/6/6.
 */
public class InteruptedTest {
    public static void main(String[] args) {
        test1();

    }
    private static boolean sleep(long mill) {
        try {
            Thread.sleep(mill);
            return true;
        } catch (InterruptedException e) {
            System.out.println("be interrupted while sleeping!");
            return false;
        }
    }
    private static void test() {
        Thread t = new Thread(()->{
            while (true) {
//                if (!sleep(3000))
//                    break;
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
    private static void test1() {
        final Lock lock = new ReentrantLock();
        Thread t = new Thread(()->{
            Scanner sc = new Scanner(System.in);
            while (true) {
                lock.lock();
                while (true) {
                    if (1 == 2)
                        break;
                }
                lock.unlock();
            }

        });
        t.start();
        t.interrupt();
    }
}
