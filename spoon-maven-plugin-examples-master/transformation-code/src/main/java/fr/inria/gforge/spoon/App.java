package fr.inria.gforge.spoon;

/**
 * Hello world!
 *
 */
public class App
{
    public static int calc(String s){
        int i = 0;
        i = i + 10;
        return i;
    }
    public static void main( String[] args )
    {
        String s = "l";
        int i = calc(s);
        System.out.println(i);
        System.out.println( "Hello World!" );
    }
}