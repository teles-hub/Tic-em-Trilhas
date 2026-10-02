import java.util.Scanner;
public class CompraOnline {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nomeDoUsuario = ent.nextLine();

        System.out.print("Digite o valor da compra: ");
        double valorCompra = ent.nextDouble();
        System.out.print("Digite o percentual de desconto: ");
        double desconto = ent.nextDouble() / 100;
        double valorComDesconto = valorCompra * (1 - desconto);
        System.out.printf("Olá, %s, sua compra é de: R$ %.2f foi confirmada.%n", nomeDoUsuario, valorCompra);
        System.out.printf("O desconto aplicado foi de %.2f%%.%n", desconto * 100);
        System.out.printf("O valor da compra com desconto é: R$ %.2f%n", valorComDesconto);
        ent.close();
    }
}
