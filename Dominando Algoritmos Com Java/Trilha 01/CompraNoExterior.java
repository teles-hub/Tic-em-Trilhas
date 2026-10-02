import java.util.Scanner;
public class CompraNoExterior {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite o valor da compra em reais: ");
        double valorReal = ent.nextDouble();
        double cotacaoDolar = 5.42;

        double valorDolar = valorReal / cotacaoDolar;

        System.out.printf("O valor da compra em dólares é: US$ %.2f%n", valorDolar);
        ent.close();
    }
}