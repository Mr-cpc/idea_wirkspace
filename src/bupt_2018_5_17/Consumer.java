package bupt_2018_5_17;

import bupt_2018_5_16.MyLock;

/**
 * Created by waiting on 2018/5/17.
 */
public class Consumer {

    MyLock lock;

    public Consumer(MyLock lock) {
        this.lock = lock;
    }

    public void consume(Food food) {
        Thread cur = Thread.currentThread();
        food.num--;
        System.out.printf("%s消费了一个，现在有%s个\n",cur.getName(),food.num);
    }

    public static void main(String[] args) {
        new Thread(()->{
            System.out.println(Thread.activeCount());
        }).start();
    }
}
