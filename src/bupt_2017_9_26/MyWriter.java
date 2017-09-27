package bupt_2017_9_26;

import java.io.*;

/**
 * @author waiting
 * @time 2017年9月12日
 * @descrption 该类可以以指定的编码将内容输出到流中
 */
public class MyWriter {

	private BufferedWriter bfw;
	/**
	 * 以此构造方法构造的对象始终会清空原文件的内容(假如原文件已经存在的话)，然后向其中输出
	 * @param charsetName 字符集名称
	 * @param dir 想要输出的文件的目录路径
	 * @param fileName 想要输出的文件名
	 */
	public MyWriter(String charsetName,String dir,String fileName) {
		File dirFile = new File(dir);
		if(!dirFile.exists())
			dirFile.mkdirs();
		if(dirFile.isFile())
			throw new RuntimeException("dir已经是一个文件的路径了,dir应该是一个目录的路径，即使不存在也可以");
		File file = new File(dirFile + File.separator + fileName);
		try {
			bfw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file), charsetName));
		} catch (UnsupportedEncodingException | FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	/**
	 * 以此构造方法构造的对象始终会清空原文件的内容(假如原文件已经存在的话)，然后向其中输出
	 * filePath应该是一个文件的绝对路径，如果该文件不存在，此构造方法会自动创建文件;
	 * 如果其父目录也不存在，那么构造方法会自动创建不存在的目录;如果此父目录实际是一个已经存在的文件，则会发生运行时异常
	 * @param charsetName 字符集名称
	 * @param filePath 想要输出的文件的名字
	 */
	public MyWriter(String charsetName,String filePath) {
		File file = new File(filePath);
		File dir = file.getParentFile();
		if(dir == null)
			throw new RuntimeException("filePath的父目录不存在");
		if(!dir.exists())
			dir.mkdirs();
		if(dir.isFile())
			throw new RuntimeException("filePath的父目录已经是一个文件了");
		try {
			bfw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file), charsetName));
		} catch (UnsupportedEncodingException | FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	public void print(String content) {
		try {
			bfw.write(content);
			bfw.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void println(String content) {
		try {
			bfw.write(content);
			bfw.newLine();
			bfw.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void close() {
		try {
			if(bfw != null)
				bfw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		finally {
			try {
				bfw.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
