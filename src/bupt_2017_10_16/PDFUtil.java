package bupt_2017_10_16;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.filechooser.FileSystemView;

import org.apache.pdfbox.io.RandomAccessBuffer;
import org.apache.pdfbox.pdfparser.PDFParser;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;


/**
 * Created by waiting on 2017/10/16.
 */
public class PDFUtil {

    public static JButton bt ;
    /**
     * 读取PDF文件的文字内容
     * @param pdfPath
     * @throws Exception
     */
    public static String getTextFromPdf(String pdfPath) throws Exception {
        // 是否排序
        boolean sort = false;
        // 开始提取页数
        int startPage = 1;
        // 结束提取页数
        int endPage = Integer.MAX_VALUE;

        String content = null;
        InputStream input = null;
        File pdfFile = new File(pdfPath);
        PDDocument document = null;
        try {
            input = new FileInputStream(pdfFile);
            // 加载 pdf 文档
            PDFParser parser = new PDFParser(new RandomAccessBuffer(input));
            parser.parse();
            document = parser.getPDDocument();
            // 获取内容信息
            PDFTextStripper pts = new PDFTextStripper();
            pts.setSortByPosition(sort);
            endPage = document.getNumberOfPages();
            System.out.println("Total Page: " + endPage);
            pts.setStartPage(startPage);
            pts.setEndPage(endPage);
            try {
                content = pts.getText(document);
            } catch (Exception e) {
                throw e;
            }
            System.out.println("Get PDF Content ...");
        } catch (Exception e) {
            throw e;
        } finally {
            if (null != input)
                input.close();
            if (null != document)
                document.close();
        }

        return content;
    }
    public static void read(String filepath) throws Exception {
        String content = getTextFromPdf(filepath);
        Pattern pattern = Pattern.compile("支付的其他与筹资活动有关的现金");
        Matcher matcher = pattern.matcher(content);
        int i = 0,start = 0,end = 0;
        FileSystemView fsv = FileSystemView.getFileSystemView();
        File com=fsv.getHomeDirectory();
        System.out.println("desktop path:"+com.getAbsolutePath());
        DateFormat df = new SimpleDateFormat("yyyy_MM_dd-HH_mm_ss");
        ExportExcel<Conte> excelUtil = new ExportExcel<Conte>();
        while (matcher.find()) {
            start = matcher.start();
            end = matcher.end();
//            BufferedWriter bfr = null;
            OutputStream os = new FileOutputStream(com.getAbsolutePath()+File.separator+ "筹资_"+i+"_"+df.format(new Date())+".xls");
//            bfr = new BufferedWriter(new FileWriter(com.getAbsolutePath()+File.separator+ "筹资_"+i+"_"+df.format(new Date())+".txt"));
            i++;
//            bfr.write(content.substring(start,end+200));
//            bfr.close();
            List<Conte> l = new ArrayList<Conte>();
            Conte c = new Conte();
            c.setContent(content.substring(start,end+200));
            l.add(c);
            excelUtil.exportExcel(new String[]{"内容"}, l, os);
            System.out.println("start:"+ matcher.start());
            System.out.println(matcher.group());
            System.out.println("end:"+matcher.end());
        }
    }
    public static void main(String[] args) throws Exception {
        // 创建JFrame
        JFrame frame = new JFrame("选择pdf");
        frame.setBounds(300,300,300,300);
        bt = new JButton("选择pdf文件");
        bt.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser jfc=new JFileChooser();
                jfc.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES );
                jfc.showDialog(new JLabel(), "选择");
                File file=jfc.getSelectedFile();
                if(file == null)
                    return ;
                if(file.isDirectory()){
                    System.out.println("文件夹:"+file.getAbsolutePath());
                    return ;
                }else if(file.isFile()){
                    try {
                        read(file.getAbsolutePath());
                    } catch (Exception e1) {
                        e1.printStackTrace();
                    }
                    System.out.println("文件:"+file.getAbsolutePath());
                }
                System.out.println(jfc.getSelectedFile().getName());
            }
        });
        frame.setResizable(false);
//        frame.setLocationRelativeTo(null);

        bt.setSize(150,150);
        frame.setLayout(null);
//        frame.setBounds(300,300,300,300);
        frame.add(bt);
        bt.setBounds((frame.getWidth()-bt.getWidth()-5)/2,(frame.getHeight()-28-bt.getHeight())/2,
                bt.getWidth(),bt.getHeight());
        // 设置尺寸
//        frame.setSize(300, 200);
        // JFrame在屏幕居中
        frame.setLocationRelativeTo(null);
        // JFrame关闭时的操作
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // 显示JFrame
        frame.setVisible(true);

    }
}


