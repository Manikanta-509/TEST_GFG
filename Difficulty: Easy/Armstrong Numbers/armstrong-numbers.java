// User function Template for Java
class Solution {
    static boolean armstrongNumber(int n) {
        int temp=n;
        int sum=0;
        int digit=String.valueOf(n).length();
        while(temp>0){
            int digits=temp%10;
            sum+=Math.pow(digits,digit);
            temp=temp/10;
        }
        return sum==n;
        
    }
}