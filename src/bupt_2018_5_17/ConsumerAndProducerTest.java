package bupt_2018_5_17;

import bupt_2018_5_16.MyLock;
import bupt_2018_5_16.SpinLock;

/**
 * Created by waiting on 2018/5/17.
 */
public class ConsumerAndProducerTest {
    static int n = 3;
    static Consumer[] consumers = new Consumer[n];
    static Producer[] producers = new Producer[n];
    static MyLock lock = new SpinLock();
    static Food food = new Food(5);
    private static int produce_limit = 10000000;

    static {
        for (int i = 0; i < consumers.length;i++) {
            consumers[i] = new Consumer(lock);
            producers[i] = new Producer(lock);
        }
    }
    public static void main(String[] args) {
        Runnable[] producers_run = new Runnable[n];
        Runnable[] consumers_run = new Runnable[n];
        Thread[] producers_t = new Thread[n];
        Thread[] consumers_t = new Thread[n];
        for (int i = 0;i <producers_run.length;i++) {
            final int index = i;
            producers_run[i] = ()->{
                boolean exit = false;
                while (true) {
                    lock.lock();
                    if (food.produceTime >= produce_limit)
                        exit = true;
                    else if (food.num < food.limit) {
//                        System.out.println(Thread.activeCount());
                        producers[index].produce(food);
                        food.produceTime++;
                        System.out.printf("共生产了%s次\n",food.produceTime);
                    }
                    lock.unlock();
                    if (exit)
                        break;

                }
            };
            consumers_run[index] = () -> {
                boolean exit = false;
                while (true) {
                    lock.lock();
                    if (food.consumeTime >= produce_limit)
                        exit = true;
                   else if (food.num > 0) {
                        consumers[index].consume(food);
                        food.consumeTime++;
                        System.out.printf("共消费了%s次\n",food.consumeTime);
                    }
                    lock.unlock();
                    if (exit)
                         break;
//                    System.out.println(Thread.activeCount());
                }
            };
            producers_t[index] = new Thread(producers_run[index]);
            producers_t[index].setName(String.format("生产者线程%s",index));
            consumers_t[index] = new Thread(consumers_run[index]);
            consumers_t[index].setName(String.format("消费者线程%s",index));
        }
        for (int i = 0;i < n;i++) {
            producers_t[i].start();
            consumers_t[i].start();
        }

    }
}
