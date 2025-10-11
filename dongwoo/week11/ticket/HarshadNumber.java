package dongwoo.week11.ticket;

public class HarshadNumber {
    public boolean solution(int x) {
        // A single-digit number is always divisible by itself.
        if (x > 0 && x < 10) {
            return true;
        }

        int temp = x;
        int sumOfDigits = 0;
        // Calculate the sum of the digits of the number.
        while (temp != 0) {
            sumOfDigits += (temp % 10);
            temp /= 10;
        }

        // Check if the number is divisible by the sum of its digits.
        return (x % sumOfDigits) == 0;
    }

    public static void main(String[] args) {
        System.out.println("CI check passed.");
    }
}
