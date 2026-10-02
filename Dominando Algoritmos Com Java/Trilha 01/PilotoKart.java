import java.util.Scanner;

public class PilotoKart {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Digite o tamanho da pista em metros: ");
        double tamanhoPista = ent.nextDouble();

        System.out.print("Digite a quantidade de voltas: ");
        int voltas = ent.nextInt();

        System.out.print("Digite o tempo da primeira volta em segundos: ");
        double tempoVoltaSegundos = ent.nextDouble();

        double distanciaKm = (tamanhoPista * voltas) / 1000.0;

        double tempoTotalMinutos = (tempoVoltaSegundos * voltas) / 60.0;

        System.out.println("\nAnálise Preditiva Concluída");
        System.out.println("--");
        System.out.println("Distância total a ser percorrida: " + distanciaKm + " km.");
        System.out.println("Previsão de conclusão: " + tempoTotalMinutos + " minutos.");

        ent.close();
    }
}