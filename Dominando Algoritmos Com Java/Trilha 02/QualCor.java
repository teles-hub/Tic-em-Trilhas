package Modúlo2;
import java.util.Scanner;

public class QualCor {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite a primeira cor: ");
        String c1 = ent.nextLine().trim();

        System.out.print("Digite a segunda cor: ");
        String c2 = ent.nextLine().trim();

        boolean c1EhPrimaria = c1.equalsIgnoreCase("Vermelho") || c1.equalsIgnoreCase("Azul") || c1.equalsIgnoreCase("Amarelo");
        boolean c2EhPrimaria = c2.equalsIgnoreCase("Vermelho") || c2.equalsIgnoreCase("Azul") || c2.equalsIgnoreCase("Amarelo");

        if (!c1EhPrimaria || !c2EhPrimaria) {
            System.out.println("Apenas cores primárias são aceitas.");
        } else {
            System.out.println("A combinação resulta em:");
            if (c1.equalsIgnoreCase(c2)) {
                System.out.println(c1.substring(0, 1).toUpperCase() + c1.substring(1).toLowerCase());
            } else if ((c1.equalsIgnoreCase("Vermelho") && c2.equalsIgnoreCase("Azul")) || (c1.equalsIgnoreCase("Azul") && c2.equalsIgnoreCase("Vermelho"))) {
                System.out.println("Roxo");
            } else if ((c1.equalsIgnoreCase("Vermelho") && c2.equalsIgnoreCase("Amarelo")) || (c1.equalsIgnoreCase("Amarelo") && c2.equalsIgnoreCase("Vermelho"))) {
                System.out.println("Laranja");
            } else if ((c1.equalsIgnoreCase("Azul") && c2.equalsIgnoreCase("Amarelo")) || (c1.equalsIgnoreCase("Amarelo") && c2.equalsIgnoreCase("Azul"))) {
                System.out.println("Verde");
            }
        }

        ent.close();
    }
}