package bupt_2018_5_17;

/**
 * Created by waiting on 2018/5/17.
 */
public class Food {
    int limit;
    volatile int produceTime;
    volatile int consumeTime;
    public Food(int limit) {
        this.limit = limit;
    }

    int num;
}
