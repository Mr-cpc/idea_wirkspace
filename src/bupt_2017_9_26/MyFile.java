package bupt_2017_9_26;

import java.io.*;
import java.math.BigDecimal;
import java.util.LinkedList;
import java.util.List;


public class MyFile {
	private File file;
	private BufferedReader bfr;
	private BufferedWriter bfw;
	public void close() {
		if(bfr != null) {
			try {
				bfr.close();
			} 
			catch (IOException e) {
			}
		}
		if(bfw != null) {
			try {
				bfw.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	public MyFile(String path) throws IOException
	{
		this.file = new File(path);
		if(!this.file.exists())
			this.file.createNewFile();
		this.bfr = new BufferedReader(new FileReader(this.file));
		
	}
	public BufferedWriter getWrier()
	{
		try {
			this.bfw = new BufferedWriter(new FileWriter(this.file));
		} catch (IOException e) {
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
		return this.bfw;
	}
	public BufferedWriter getWrier(boolean append)
	{
		try {
			this.bfw = new BufferedWriter(new FileWriter(this.file,append));
		} catch (IOException e) {
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
		return this.bfw;
	}
	public int read(char[] ch)
	{
		int len = 0;
		try {
			len = this.bfr.read(ch);
		} catch (IOException e) {
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
		return len;
	}
	public String readLine() throws IOException
	{
		return this.bfr.readLine();
	}
	public void setPath(String path) throws IOException
	{
		this.file = new File(path);
		if(!this.file.exists())
			this.file.createNewFile();
		this.bfr = new BufferedReader(new FileReader(this.file));
		this.bfw = new BufferedWriter(new FileWriter(this.file,true));
	}
	public void setWritePath(String path,boolean isAppend) throws IOException
	{
		this.file = new File(path);
		if(!this.file.exists())
			this.file.createNewFile();
		this.bfw = new BufferedWriter(new FileWriter(this.file,isAppend));
	}
	public String getPath()
	{
		return this.file.getAbsolutePath();
	}
	public synchronized void println(int i) throws IOException
	{
		this.bfw.write(i);
		this.bfw.newLine();
		this.bfw.flush();
	}
	
	public synchronized void println(String str) throws IOException
	{
		this.bfw.write(str);
		this.bfw.newLine();
		this.bfw.flush();
	}
	public synchronized void print(String str) throws IOException
	{
		this.bfw.write(str);
		this.bfw.flush();
	}
	public synchronized void print(BigDecimal bd) throws IOException
	{
		this.bfw.write(bd.toString());
		this.bfw.flush();
	}
	public synchronized void println(BigDecimal bd) throws IOException
	{
		this.bfw.write(bd.toString());
		this.bfw.flush();
	}
	public static String match(String target,String dir,String suffix) throws IOException {
		File d = new File(dir);
		StringBuilder sb = new StringBuilder();
		traverse(d, suffix, target);
		for(File f:files) {
			sb.append(f.getName());
			sb.append('\n');
		}
		return sb.toString();
	}
	public static void visit(File f,String suffix,String target) throws IOException {
		if(f.getName().endsWith(suffix) && IO.readFile(f.getAbsolutePath()).contains(target))
			files.add(f);
//		System.out.println(f.getName());
	}
	static List<File> files = new LinkedList<>();
	public static void traverse(File f,String suffix,String target) throws IOException {
		if(f.isFile()) {
			visit(f,suffix,target) ;
		}
		else {
			if(f.listFiles().length == 0)
				return ;
			for(File file:f.listFiles()) {
				if(file.isFile())
					visit(file,suffix,target);
				else
					traverse(file,suffix,target);
			}
		}
	}
	public static void main(String[ ]args) throws IOException
	{
		double a = 0.1;
//		System.out.print(Double.valueOf(a));
		System.out.println(match("拦截请求", "C:\\Users\\waiting\\Desktop\\SpringMVC-Mybatis-shiro-master\\test\\src\\main\\java", ".java"));
	}
}
