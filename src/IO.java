import java.io.IOException;
import java.util.*;

public class IO {

	public static String readFile(String path) throws IOException
	{
		StringBuilder sb = new StringBuilder(1024);
		MyFile mf = new MyFile(path);
		char[] ch = new char[1024];
		int len;
		while((len = mf.read(ch))!=-1)
			sb.append(ch, 0, len);
		mf.close();
		return sb.toString();
	}
	/**
	 * 
	* @author: waiting
	* @date: 2017年9月12日 上午11:11:30
	* @Title: readFile   
	* @Description: TODO(将文件中的内容以指定的字符集解码读出)   
	* @param @param path 想要读取的文件的绝对路径
	* @param @param 指定的字符集来解码
	* @param @return    设定文件   
	* @return String    返回类型   
	* @throws   

	 */
	public static String readFile(String path,String charsetName) 
	{
		StringBuilder sb = new StringBuilder(1024);
		MyReader mf = new MyReader(charsetName, path);
		char[] ch = new char[1024];
		int len;
		while((len = mf.read(ch))!=-1)
			sb.append(ch, 0, len);
		mf.close();
		return sb.toString();
	}
	/**
	 * 
	* @author: waiting
	* @date: 2017年9月12日 上午11:12:48
	* @Title: writeFile   
	* @Description: TODO(将指定的内容以指定的编码输出到指定的文件中)   
	* @param @param dir 输出文件的目录名
	* @param @param fileName 想要输出的文件名（应形如filename.suffixName）
	* @param @param charsetName 字符集名
	* @param @param content  输出的内容   
	* @return void    返回类型   
	* @throws   
	 */
	public static void writeFile(String dir,String fileName,String charsetName,String content) 
	{
		MyWriter mf = new MyWriter(charsetName, dir, fileName);
		mf.print(content);
		mf.close();
	}
	public static void writeFile(String fileName,String charsetName,String content) 
	{
		MyWriter mf = new MyWriter(charsetName, fileName);
		mf.print(content);
		mf.close();
	}
	public static int power(int bot, int exp)
	{
		if(exp == 0)
			return 1;
		int tem = bot;
		for(int i =1;i<exp;i++)
			bot *= tem;
		return bot;
	}
	public static int getRanInt(int n)
	{
		Random rnd = new Random();
		return rnd.nextInt(n);
	}
	public static int getRanInt(int min ,int max)
	{
		return min+getRanInt(max);
	}
	public  static <T> void  swap(T t1,T t2)
	{
		T temp = t1;
		t1 = t2;
		t2 = temp;
	}
	public static MyFile getMyFile(String path)
	{
		MyFile mf = null;
		try {
			mf = new MyFile(path);
		} catch (IOException e) {
			e.printStackTrace();
		}
		return mf;
	}
	public static void write(String path,boolean isAppend,String content) {
		MyFile mf = null;
		try {
			mf  = new MyFile(path);
			mf.setWritePath(path, isAppend);
			mf.print(content);
			mf.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
}
