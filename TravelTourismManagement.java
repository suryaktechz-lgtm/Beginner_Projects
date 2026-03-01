import java.util.*;

class TravelPackage {
    int id;
    String destination;
    int days;
    double price;

    TravelPackage(int id, String destination, int days, double price) {
        this.id = id;
        this.destination = destination;
        this.days = days;
        this.price = price;
    }

    void displayPackage() {
        System.out.println(id + ". " + destination + " | " + days + " days | ₹" + price);
    }
}

class Booking {
    String customerName;
    TravelPackage travelPackage;
    int persons;
    double totalCost;

    Booking(String customerName, TravelPackage travelPackage, int persons) {
        this.customerName = customerName;
        this.travelPackage = travelPackage;
        this.persons = persons;
        this.totalCost = travelPackage.price * persons;
    }

    void displayBooking() {
        System.out.println("\n===== BOOKING SUMMARY =====");
        System.out.println("Customer Name: " + customerName);
        System.out.println("Destination: " + travelPackage.destination);
        System.out.println("Days: " + travelPackage.days);
        System.out.println("Persons: " + persons);
        System.out.println("Total Cost: ₹" + totalCost);
    }
}

public class TravelTourismManagement {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        List<TravelPackage> packages = new ArrayList<>();

        // Predefined packages
        packages.add(new TravelPackage(1, "Goa", 3, 5000));
        packages.add(new TravelPackage(2, "Manali", 5, 12000));
        packages.add(new TravelPackage(3, "Jaipur", 4, 8000));
        packages.add(new TravelPackage(4, "Kerala", 6, 15000));

        while (true) {
            System.out.println("\n===== TRAVEL & TOURISM MANAGEMENT =====");
            System.out.println("1. View Packages");
            System.out.println("2. Book Package");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("\nAvailable Packages:");
                    for (TravelPackage p : packages) {
                        p.displayPackage();
                    }
                    break;

                case 2:
                    System.out.print("Enter your name: ");
                    sc.nextLine(); // clear buffer
                    String name = sc.nextLine();

                    System.out.println("\nSelect Package ID:");
                    for (TravelPackage p : packages) {
                        p.displayPackage();
                    }

                    int packageId = sc.nextInt();
                    TravelPackage selectedPackage = null;

                    for (TravelPackage p : packages) {
                        if (p.id == packageId) {
                            selectedPackage = p;
                            break;
                        }
                    }

                    if (selectedPackage == null) {
                        System.out.println("Invalid Package ID!");
                        break;
                    }

                    System.out.print("Enter number of persons: ");
                    int persons = sc.nextInt();

                    Booking booking = new Booking(name, selectedPackage, persons);
                    booking.displayBooking();
                    break;

                case 3:
                    System.out.println("Thank you for using Travel Management System!");
                    System.exit(0);

                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}