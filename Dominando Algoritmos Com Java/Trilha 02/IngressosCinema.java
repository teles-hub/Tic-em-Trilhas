package Modúlo2;
import java.util.Locale;
import java.util.Scanner;

public class IngressosCinema {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Quantidade de inteiras: ");
        int inteiras = ent.nextInt();

        System.out.print("Quantidade de meias: ");
        int meias = ent.nextInt();
        ent.nextLine(); 
        System.out.print("Dia da semana: ");
        String diaSemana = ent.nextLine().trim();

        System.out.print("Filme nacional? (Sim/Não): ");
        String nacional = ent.nextLine().trim();

        double precoInteira = 28.50;
        double precoMeia = precoInteira / 2.0;

        if (nacional.equalsIgnoreCase("Sim")) {
            precoInteira = 5.00;
            precoMeia = 5.00;
        } else if (diaSemana.equalsIgnoreCase("Quarta-feira") || diaSemana.equalsIgnoreCase("Quarta")) {
            precoInteira = 14.50;
            precoMeia = 14.50;
        }

        double total = (inteiras * precoInteira) + (meias * precoMeia);

        System.out.printf(Locale.US, "Total à pagar:%nR$ %.2f%n", total);

        ent.close();
    }
}