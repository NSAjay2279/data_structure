import java.util.Scanner;

public class Hash {
    // Returns a hash code (number) for the given string
    public static int stringToNumber(String s) {
        int hash = 0;
        for (int i = 0; i < s.length(); i++) {
            hash = 31 * hash + s.charAt(i);
        }
        return hash;
    }

    public static void main(String[] args) {
        // 2D array: {name, price}
        String[][] items = {
            {"apple", "1.69"},
            {"banana", "0.59"},
            {"orange", "1.99"}
        };

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter name: ");
        String inputName = scanner.nextLine().trim();

        boolean found = false;
        for (String[] item : items) {
            if (item[0].equalsIgnoreCase(inputName)) {
                System.out.println("Price: " + item);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Name not found.");
        }

        scanner.close();
    }
}
