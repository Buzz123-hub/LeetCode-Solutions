class Solution {
    public int myAtoi(String s) {

        int n = s.length();
        int i = 0;

        // Step 1: Ignore leading whitespace
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        // Step 2: Check sign
        int sign = 1;

        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {

            if (s.charAt(i) == '-') {
                sign = -1;
            }

            i++;
        }

        // Step 3: Convert digits
        long num = 0;

        while (i < n && Character.isDigit(s.charAt(i))) {

            int digit = s.charAt(i) - '0';

            num = num * 10 + digit;


            // Step 4: Overflow check
            if (sign * num > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }

            if (sign * num < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }

            i++;
        }

        return (int)(sign * num);
    }
}