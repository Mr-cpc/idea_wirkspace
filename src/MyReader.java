import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

/**
 * @author waiting
 * @time 2017年9月12日
 * @descrption 此类可用于以指定的编码从流中读取字符
 */
public class MyReader {

	private BufferedReader bfr;
	/**
	 * 
	 * @param charsetName 指定以哪种字符集来解码流
	 * @param filePath    要读取的文件的绝对路径
	 */
	public MyReader(String charsetName,String filePath) {
		File file = new File(filePath);
		if(!file.exists() || !file.isFile())
			throw new RuntimeException("该文件不存在 或者 不是一个文件");
		try {
			bfr = new BufferedReader(new InputStreamReader(new FileInputStream(file), charsetName));
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	/**
	 * 
	* @author: waiting
	* @date: 2017年9月12日 上午10:12:02
	* @Title: readLine   
	* @Description: (从流中读取一行，遇到换行返回)   
	* @param @return    设定文件   
	* @return String    读取的那一行String   
	* @throws   

	 */
	public String readLine() {
		try {
			return bfr.readLine();
		} catch (IOException e) {
			e.printStackTrace();
			return "";
		}
	}
	/**
	 * 
	* @author: waiting
	* @date: 2017年9月12日 上午10:13:01
	* @Title: read   
	* @Description: TODO(从流中读取字符，放到ch数组的0-读取的长度处)   
	* @param @param ch 用于存放读取的字符的数组
	* @param @return    设定文件   
	* @return int    返回读取的字符数，发生IOException返回0   
	* @throws   

	 */
	public int read(char[] ch) {
		try {
			return bfr.read(ch);
		} catch (IOException e) {
			e.printStackTrace();
			return 0;
		}
	}
	public void close() {
		try {
			if(bfr != null)
				bfr.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {
		IO.writeFile("D:\\certs\\a.txt" ,"gbk",IO.readFile("D:\\RB.java", "utf-8"));
	}
}
