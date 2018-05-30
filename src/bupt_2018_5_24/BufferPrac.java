package bupt_2018_5_24;

import java.io.*;
import java.nio.ByteBuffer;
import java.nio.channels.Channel;
import java.nio.channels.FileChannel;

/**
 * Created by waiting on 2018/5/24.
 */
public class BufferPrac {
    public static void practice1() throws FileNotFoundException {
        RandomAccessFile file = new RandomAccessFile("C:\\Users\\waiting\\Desktop\\contest\\idea_wirkspace\\src\\bupt_2018_5_24\\nio.txt","rw");
        FileChannel channel = file.getChannel();
        ByteBuffer buffer = ByteBuffer.allocate(1);
        FileOutputStream out = new FileOutputStream("C:\\Users\\waiting\\Desktop\\contest\\idea_wirkspace\\src\\bupt_2018_5_24\\out.txt");
        FileChannel outChannel = out.getChannel();
        try {
            channel.read(buffer);
            System.out.printf("position:%s",buffer.position());
            channel.read(buffer);
            channel.read(buffer);
            buffer.flip();
            outChannel.write(buffer);
            out.close();
        } catch (IOException e) {
            System.out.println("io ex");
        }
    }
    public static void copy(String res,String des) throws IOException {
        FileInputStream in = new FileInputStream(res);
        FileChannel channel1 = in.getChannel();
        FileOutputStream out = new FileOutputStream(des);
        FileChannel channel2 = out.getChannel();
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        while (channel1.position() < channel1.size()) {
            channel1.read(buffer);
            buffer.flip();
            channel2.write(buffer);
            buffer.flip();
            buffer.clear();
        }
    }
    public static void practice2() throws IOException {
        RandomAccessFile f1 = new RandomAccessFile("C:\\Users\\waiting\\Desktop\\contest\\idea_wirkspace\\src\\bupt_2018_5_24\\1.txt","rw");
        RandomAccessFile f2 = new RandomAccessFile("C:\\Users\\waiting\\Desktop\\contest\\idea_wirkspace\\src\\bupt_2018_5_24\\2.txt","rw");
        System.out.printf("line:%s\n",f1.readLine());
        System.out.printf("length:%s\n",f1.length());
        FileChannel channel1 = f1.getChannel();
        FileChannel channel2 = f2.getChannel();
        System.out.println(channel1.size());
        channel1.transferFrom(channel2,0,channel2.size());
    }
    public static void practice3() {
        try {
            FileChannel channel = new RandomAccessFile("C:\\Users\\waiting\\Desktop\\contest\\idea_wirkspace\\src\\bupt_2018_5_24\\1.txt","rw").getChannel();
            ByteBuffer buffer = ByteBuffer.allocate(1);
            System.out.println(channel.position());
            channel.read(buffer);
            System.out.println(channel.position());
            buffer.clear();
            channel.truncate(1);
            channel.read(buffer);
            FileChannel channel12 = new FileOutputStream("C:\\Users\\waiting\\Desktop\\contest\\idea_wirkspace\\src\\bupt_2018_5_24\\2.txt").getChannel();
            channel12.write(buffer);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        practice3();
    }
}
