import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        for (int i =0;i<n;i++){     
            for (int j =(n-1);j>=0;j--){
                if(j>i){System.out.print(" ");}
                else{System.out.print("#");}
            }
            System.out.println();
        }
    }
}
