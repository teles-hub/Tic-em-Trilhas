package Modúlo2;

import java.util.Scanner;

public class DiaPorExtenso {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite o número do dia (0 a 6): ");
        int dia = ent.nextInt();

        if (dia == 0) {
            System.out.println("Domingo");
        } else if (dia == 1) {
            System.out.println("Segunda-feira");
        } else if (dia == 2) {
            System.out.println("Terça-feira");
        } else if (dia == 3) {
            System.out.println("Quarta-feira");
        } else if (dia == 4) {
            System.out.println("Quinta-feira");
        } else if (dia == 5) {
            System.out.println("Sexta-feira");
        } else if (dia == 6) {
            System.out.println("Sábado");
        } else {
            System.out.println("Dia da semana inválido");
        }

        ent.close();
    }
}