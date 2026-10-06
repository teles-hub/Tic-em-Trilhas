package Modúlo2;

import java.util.Locale;
import java.util.Scanner;

public class NotaDeCorte {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Digite a nota do candidato: ");
        double notaCandidato = ent.nextDouble();

        System.out.print("Digite a nota de corte: ");
        double notaCorte = ent.nextDouble();

        System.out.print("Digite a nota mínima de aprovação: ");
        double notaMinAprovacao = ent.nextDouble();

        if (notaCandidato < notaCorte) {
            System.out.println("Situação candidato:");
            System.out.println("Reprovado");
        } else if (notaCandidato >= notaMinAprovacao) {
            System.out.println("Situação candidato:");
            System.out.println("Aprovado");
        } else {
            System.out.println("Situação candidato:");
            System.out.println("Lista de Espera");
        }

        ent.close();
    }
}