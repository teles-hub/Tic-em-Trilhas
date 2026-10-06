package Modúlo2;

import java.util.Scanner;

public class Semaforo {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite a cor do semáforo: ");
        String cor = ent.nextLine().trim();

        if (cor.equalsIgnoreCase("Vermelho")) {
            System.out.println("Espere");
        } else if (cor.equalsIgnoreCase("Verde")) {
            System.out.println("Atravesse");
        } else {
            System.out.println("Farol inoperante");
        }

        ent.close();
    }
}