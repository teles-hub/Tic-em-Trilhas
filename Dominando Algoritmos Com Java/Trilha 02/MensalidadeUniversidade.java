package Modúlo2;

import java.util.Locale;
import java.util.Scanner;

public class MensalidadeUniversidade {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Digite a sigla do curso: ");
        String curso = ent.nextLine().trim();

        System.out.print("É isento? (Sim/Não): ");
        String isento = ent.nextLine().trim();

        System.out.print("Digite o desconto (%): ");
        double desconto = ent.nextDouble();

        double valorBase = 0;
        boolean encontrado = true;

        if (curso.equalsIgnoreCase("SI")) {
            valorBase = 900.00;
        } else if (curso.equalsIgnoreCase("ADS")) {
            valorBase = 750.00;
        } else if (curso.equalsIgnoreCase("CS")) {
            valorBase = 1150.00;
        } else if (curso.equalsIgnoreCase("EC")) {
            valorBase = 1300.00;
        } else if (curso.equalsIgnoreCase("ES")) {
            valorBase = 950.00;
        } else {
            encontrado = false;
        }

        if (!encontrado) {
            System.out.println("Curso não encontrado");
        } else {
            if (isento.equalsIgnoreCase("Sim")) {
                valorBase = 0.0;
            } else {
                valorBase = valorBase - (valorBase * (desconto / 100.0));
            }
            System.out.printf(Locale.US, "Valor da mensalidade:%nR$ %.2f%n", valorBase);
        }

        ent.close();
    }
}