package Modúlo2;

import java.util.Locale;
import java.util.Scanner;

public class CalculadoraComMenu {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Digite o primeiro número: ");
        double n1 = ent.nextDouble();

        System.out.print("Digite o segundo número: ");
        double n2 = ent.nextDouble();
        ent.nextLine(); 

        System.out.print("Digite a operação (nome ou número): ");
        String op = ent.nextLine().trim();

        if (op.equalsIgnoreCase("1") || op.equalsIgnoreCase("Soma")) {
            System.out.printf(Locale.US, "%.1f + %.1f = %.1f%n", n1, n2, (n1 + n2));
        } else if (op.equalsIgnoreCase("2") || op.equalsIgnoreCase("Subtração") || op.equalsIgnoreCase("Subtracao")) {
            System.out.printf(Locale.US, "%.1f - %.1f = %.1f%n", n1, n2, (n1 - n2));
        } else if (op.equalsIgnoreCase("3") || op.equalsIgnoreCase("Multiplicação") || op.equalsIgnoreCase("Multiplicacao")) {
            System.out.printf(Locale.US, "%.1f * %.1f = %.1f%n", n1, n2, (n1 * n2));
        } else if (op.equalsIgnoreCase("4") || op.equalsIgnoreCase("Divisão") || op.equalsIgnoreCase("Divisao")) {
            System.out.printf(Locale.US, "%.1f / %.1f = %.1f%n", n1, n2, (n1 / n2));
        } else if (op.equalsIgnoreCase("5") || op.equalsIgnoreCase("Resto")) {
            System.out.printf(Locale.US, "%.1f mod %.1f = %.1f%n", n1, n2, (n1 % n2));
        } else if (op.equalsIgnoreCase("6") || op.equalsIgnoreCase("Potência") || op.equalsIgnoreCase("Potencia")) {
            System.out.printf(Locale.US, "%.1f ^ %.1f = %.1f%n", n1, n2, Math.pow(n1, n2));
        } else {
            System.out.println("Operação não suportada");
        }

        ent.close();
    }
}