package bupt_2018_5_11;

import org.springframework.web.servlet.DispatcherServlet;

import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Created by waiting on 2018/5/11.
 */
public class ThreadGrouPrac {
//    DispatcherServlet s;


    ConcurrentHashMap a = new ConcurrentHashMap();
    HashMap b;
    {
        System.out.println("construct block");
    }

    static  {
        System.out.println("static block");
    }
    static ThreadGrouPrac t1 = new ThreadGrouPrac();
    static ThreadGrouPrac t2 = new ThreadGrouPrac();
    public ThreadGrouPrac()
    {
    }    public static void main(String[] args) {
        System.out.println(1);
        ThreadGrouPrac t = new ThreadGrouPrac();
    }
    public static void t() {
        System.out.println(System.getSecurityManager());
        Thread t = new Thread(()->{
            Thread cur = Thread.currentThread();
            System.out.println(cur.getName()+"的threadgroup:"+cur.getThreadGroup().getName());
            Thread x = new Thread(()->{
                System.out.println(Thread.currentThread().getName()+"的threadgroup:"+Thread.currentThread().getThreadGroup().getName());
            });
            x.start();
        });

        t.start();
        System.out.println(Thread.currentThread().getName()+"的threadgroup:"+Thread.currentThread().getThreadGroup().getName());
    }
}
