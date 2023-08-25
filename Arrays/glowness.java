package Arrays;
public class glowness{
    public static void main(String[] args){
        int[] a = new int[]{2,-3,4,6,8,2,1,-5,9};
        int x = 0, y = 0;
        int n = a.length;
        for(int i = 0; i < n; i++){
            int val = Math.abs(a[i]);
            if(val > x){
                x = val;
            }
        }
        for(int i=0, j=1; i < n-1 && j < n; i++, j++){
            y += Math.abs(a[j]-a[i]);
        }
        System.out.println(gcd(x,y));
    }
    static int gcd(int a, int b){
        if(a == 0)
            return b;
        if(b == 0)
            return a;
        if(a == b)
            return a;
        if(a > b)
            return gcd(a-b,b);
        return gcd(a, b-a);
    }
}