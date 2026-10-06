package TrilhasJava.Modúlo2;

import java.util.Scanner;

public class OrçamentoFamiliar {

    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite o total de ganhos: ");
        double ganhos = ent.nextDouble();

        System.out.print("Digite o total de gastos: ");
        double gastos = ent.nextDouble();

        if (ganhos >= gastos) {
            System.out.println("Você está dentro do orçamento!");
        } else {
            System.out.println("Você está fora do orçamento! Não gaste mais!");
        }

        ent.close();
    }
}
