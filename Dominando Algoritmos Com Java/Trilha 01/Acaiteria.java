
import java.util.Scanner;

public class Acaiteria {

    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite a quantidade de Açaí P: ");
        int qtdP = ent.nextInt();

        System.out.print("Digite a quantidade de Açaí M: ");
        int qtdM = ent.nextInt();

        System.out.print("Digite a quantidade de Açaí G: ");
        int qtdG = ent.nextInt();

        System.out.print("Digite a porcentagem do cupom de desconto: ");
        double cupom = ent.nextDouble();

        double precoP = 13.50;
        double precoM = 15.00;
        double precoG = 17.50;

        double subtotal = (qtdP * precoP) + (qtdM * precoM) + (qtdG * precoG);

        double valorDesconto = subtotal * (cupom / 100.0);
        double total = subtotal - valorDesconto;

        System.out.println("\nSeu pedido foi registrado.");
        System.out.println("- Açaí P: " + qtdP);
        System.out.println("- Açaí M: " + qtdM);
        System.out.println("- Açaí G: " + qtdG);
        System.out.println();
        System.out.printf("Desconto de %.0f%% aplicado.%n", cupom);
        System.out.printf("Total R$ %.2f%n", total);

        ent.close();
    }
}
