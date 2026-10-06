package Modúlo2;

import java.util.Locale;
import java.util.Scanner;

public class SorveteriaPromocao {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Digite o peso em gramas: ");
        double gramas = ent.nextDouble();

        if (gramas <= 0) {
            System.out.println("Peso inválido");
        } else {
            double precoPor100g = 3.50;
            if (gramas >= 1000) {
                precoPor100g = 3.00;
            }

            double total = (gramas / 100.0) * precoPor100g;
            System.out.printf(Locale.US, "O total é R$ %.2f%n", total);
        }

        ent.close();
    }
}