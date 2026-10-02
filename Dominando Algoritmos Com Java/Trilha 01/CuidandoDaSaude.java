import java.util.Scanner;
public class CuidandoDaSaude {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nomeDoUsuario = ent.nextLine();

        System.out.print("Digite seu peso (em kg): ");
        double peso = ent.nextDouble();

        System.out.print("Digite sua altura (em metros): ");
        double altura = ent.nextDouble();

        double imc = peso / (altura * altura);
        
        System.out.printf("Olá, %s!%n", nomeDoUsuario);
        System.out.printf("Seu IMC é: %.4f%n", imc);

        ent.close();
    }
}
