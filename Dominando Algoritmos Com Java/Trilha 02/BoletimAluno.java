package Modúlo2;

import java.util.Locale;
import java.util.Scanner;

public class BoletimAluno {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Digite a nota 1: ");
        double nota1 = ent.nextDouble();

        System.out.print("Digite a nota 2: ");
        double nota2 = ent.nextDouble();

        System.out.print("Digite a nota 3: ");
        double nota3 = ent.nextDouble();

        System.out.print("Digite a quantidade de faltas: ");
        int faltas = ent.nextInt();

        double media = (nota1 + nota2 + nota3) / 3.0;

        if (nota1 < 0 || nota1 > 10 || nota2 < 0 || nota2 > 10 || nota3 < 0 || nota3 > 10 || faltas < 0) {
            System.out.println("Parâmetros inválidos");
        } else if (faltas > 4) {
            System.out.printf(Locale.US, "Média: %.1f.%n", media);
            System.out.println("Situação: Reprovado por Falta");
        } else if (media == 0) {
            System.out.printf(Locale.US, "Média: %.1f.%n", media);
            System.out.println("Situação: Desistente");
        } else if (media >= 8.0) {
            System.out.printf(Locale.US, "Média: %.1f.%n", media);
            System.out.println("Situação: Aprovado com sucesso");
        } else if (media >= 6.0) {
            System.out.printf(Locale.US, "Média: %.1f.%n", media);
            System.out.println("Situação: Aprovado");
        } else {
            System.out.printf(Locale.US, "Média: %.1f.%n", media);
            System.out.println("Situação: Recuperação");
        }

        ent.close();
    }
}