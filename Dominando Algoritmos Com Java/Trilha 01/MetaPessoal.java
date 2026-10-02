import java.util.Scanner;

public class MetaPessoal {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        // Entrada dos dados
        System.out.print("Digite a descrição da meta: ");
        String meta = ent.nextLine();

        System.out.print("Digite o valor necessário para a meta: ");
        double valorMeta = ent.nextDouble();

        System.out.print("Digite seu salário mensal: ");
        double salario = ent.nextDouble();

        System.out.print("Digite o total das despesas mensais: ");
        double despesas = ent.nextDouble();

        double saldoAposDespesas = salario - despesas;


        double reservaFixa = saldoAposDespesas * 0.30;


        double valorDisponivelMeta = saldoAposDespesas - reservaFixa;

        double prazoMeses = valorMeta / valorDisponivelMeta;

        System.out.println("\nMeta: " + meta + " (R$ " + String.format("%.2f", valorMeta) + ")");
        System.out.printf("Salário: R$ %.2f - Despesas: R$ %.2f%n", salario, despesas);
        System.out.println();
        System.out.printf("Saldo após despesas: R$ %.2f%n", saldoAposDespesas);
        System.out.printf("Reserva fixa (30%%): R$ %.2f%n", reservaFixa);
        System.out.printf("Valor disponível para a meta: R$ %.2f por mês%n", valorDisponivelMeta);
        System.out.printf("Prazo estimado para atingir a meta: %.2f meses%n", prazoMeses);

        ent.close();
    }
}