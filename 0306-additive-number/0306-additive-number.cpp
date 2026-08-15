class Solution {
public:
    bool isValid(string s) {
        if (s.length() > 1 && s[0] == '0')
            return false;
        return true;
    }

    string addStrings(string a, string b) {
        string result;
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;

            if (i >= 0)
                sum += a[i--] - '0';

            if (j >= 0)
                sum += b[j--] - '0';

            result.push_back((sum % 10) + '0');
            carry = sum / 10;
        }

        reverse(result.begin(), result.end());
        return result;
    }

    bool check(string num, int start, string a, string b) {
        int n = num.length();

        while (start < n) {
            string c = addStrings(a, b);

            // Next number must exactly match the sum
            if (start + c.length() > n ||
                num.substr(start, c.length()) != c) {
                return false;
            }

            start += c.length();

            a = b;
            b = c;
        }

        return true;
    }

    bool isAdditiveNumber(string num) {
        int n = num.length();

        // Choose first number
        for (int i = 1; i <= n - 2; i++) {

            // Leading zero is not allowed
            if (i > 1 && num[0] == '0')
                break;

            string a = num.substr(0, i);

            // Choose second number
            for (int j = i + 1; j <= n - 1; j++) {

                // Leading zero is not allowed
                if (j - i > 1 && num[i] == '0')
                    break;

                string b = num.substr(i, j - i);

                if (check(num, j, a, b))
                    return true;
            }
        }

        return false;
    }
};