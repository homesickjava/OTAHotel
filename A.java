import java.io.File;
import java.util.List;

public class A {

    private Long filenum = 0L;
    private Long emptydirnum = 0L;

    public static void main(String[] args) {

        File f = new File("c://");

        A a = new A();
        Long start = System.currentTimeMillis();
        a.getFileNum(f);
        Long end = System.currentTimeMillis();
        System.out.println("c盘文件总数："+a.filenum);
        System.out.println("c盘空文件夹总数："+a.emptydirnum);
        System.out.println("读取文件总耗时："+(end-start));
    }

    public void getFileNum(File f) {

        File[] flist = f.listFiles();
        if(flist!=null) {
            if(flist.length==0) {
                emptydirnum++;
            } else {
                for(File file:flist) {
                    if(file.isDirectory()) {
                        getFileNum(file);
                    } else {
                        filenum++;
                    }
                }
            }
        }
    }
}
