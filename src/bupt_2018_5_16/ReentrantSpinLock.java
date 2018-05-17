package bupt_2018_5_16;

import java.util.concurrent.atomic.AtomicReference;

/**
 * Created by waiting on 2018/5/16.
 */
public class ReentrantSpinLock implements MyLock{
    AtomicReference<Thread> lockOwner = new AtomicReference<>();
    int count;
    @Override
    public void lock() {
        Thread currentThread = Thread.currentThread();
        if (currentThread == lockOwner.get())
            count++;
        while (!lockOwner.compareAndSet(null,currentThread)) {

        }
    }

    @Override
    public void unlock() {
        Thread currentThread = Thread.currentThread();
        if (currentThread == lockOwner.get()) {
            if (count > 0)
                count--;
            else
                lockOwner.compareAndSet(currentThread,null);
        }
    }
}
