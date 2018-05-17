package bupt_2018_5_17;

import bupt_2018_5_16.MyLock;

/**
 * Created by waiting on 2018/5/17.
 */
public class Producer {
    MyLock lock;

    public Producer(MyLock lock) {
        this.lock = lock;
    }

    public void produce(Food food) {
        Thread cur = Thread.currentThread();
        food.num++;
        System.out.printf("%s生产了一个，现在有%s个\n",cur.getName(),food.num);
    }
}
