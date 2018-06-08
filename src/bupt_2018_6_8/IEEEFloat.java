package bupt_2018_6_8;

/**
 * Created by waiting on 2018/6/8.
 */
public class IEEEFloat extends IEEE754 {
    public IEEEFloat(float value) {
        this.value = value;
        IEEE754IntFormat = Float.floatToIntBits(value);
        IEEE754Format = Integer.toBinaryString(IEEE754IntFormat);
    }

    private final float value;
    private final int IEEE754IntFormat;
    private final String IEEE754Format;
    @Override
    public String getE() {
        int len = IEEE754Format.length();
        if (len == 32)
            return IEEE754Format.substring(0,8);
        else {
            StringBuilder sb = new StringBuilder(IEEE754Format.substring(0,len - 23));
            while (sb.length() < 8)
                sb.insert(0,'0');
            return sb.toString();
        }
    }

    @Override
    public String getS() {
        if (IEEE754Format.length() == 32)
            return "1";
        else
            return "0";
    }

    @Override
    public String getM() {
        int len = IEEE754Format.length();
        return IEEE754Format.substring(len - 23,len);
    }

    @Override
    public String toString() {
        return String.format("%s-%s-%s",getS(),getE(),getM());
    }
}
