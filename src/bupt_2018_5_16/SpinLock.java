package bupt_2018_5_16;

import java.util.concurrent.atomic.AtomicReference;

/**
 * Created by waiting on 2018/5/16.
 */
public class SpinLock implements MyLock{
    AtomicReference<Thread> lockOwner = new AtomicReference<>();
    @Override
    public void lock() {
        Thread currentThread = Thread.currentThread();
        while ( !lockOwner.compareAndSet(null,currentThread)){

        }
    }

    @Override
    public void unlock() {
        Thread currentThread = Thread.currentThread();
        if (lockOwner.get() == currentThread)
            lockOwner.compareAndSet(currentThread,null);
        else
            throw new RuntimeException("illegal lock status");
    }
}
