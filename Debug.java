public class Debug {
    public static void main(String [] args) {
        final int DAYS = 30;
        double money = 0.01;
        int day = 1;
        while (day < DAYS) {
            money = 2 * money;
            System.out.println("After day " + String.valueOf(day) + " you have " + String.valueOf(money));
            day++;
        }
    }
}


