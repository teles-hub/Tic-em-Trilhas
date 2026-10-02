import java.util.Scanner;

public class MediaDeNotas {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite o nome do estudante: ");
        String nome = ent.nextLine();
        System.out.print("Digite a primeira nota: ");
        double nota1 = ent.nextDouble();
        System.out.print("Digite a segunda nota: ");
        double nota2 = ent.nextDouble();
        System.out.print("Digite a terceira nota: ");
        double nota3 = ent.nextDouble();

        double media = (nota1 + nota2 + nota3) / 3;

        System.out.printf("O estudante %s tem média %.2f%n", nome, media);
        ent.close();
    }
}