
import java.util.Scanner;

public class ChurrascoDeDomingo {

    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.println("Digite o número de convidados: ");
        int numConvidados = ent.nextInt();
        double carneNecessaria = numConvidados * 0.3; // 300g por pessoa
        double linguiçaNecessaria = numConvidados * 0.2; // 200g por pessoa
        double frangoNecessario = numConvidados * 0.15; // 150g por pessoa

        double valorCarne = carneNecessaria * 50; // R$50 por kg
        double valorLinguiça = linguiçaNecessaria * 28; // R$28 por kg
        double valorFrango = frangoNecessario * 22; // R$22 por kg
        double total = valorCarne + valorLinguiça + valorFrango;
        System.out.printf("Quantidade de carne necessária: %.2f kg%n", carneNecessaria);
        System.out.printf("Quantidade de linguiça necessária: %.2f kg%n", linguiçaNecessaria);
        System.out.printf("Quantidade de frango necessária: %.2f kg%n", frangoNecessario);
        System.out.printf("Valor total da carne: R$ %.2f%n", valorCarne);
        System.out.printf("Valor total da linguiça: R$ %.2f%n", valorLinguiça);
        System.out.printf("Valor total do frango: R$ %.2f%n", valorFrango);

        System.out.printf("Custo total do churrasco: R$ %.2f%n", total);
        System.out.printf("Custo por pessoa: R$ %.2f%n", total / numConvidados);

        ent.close();
    }
}
