import java.util.Locale;
import java.util.Scanner;

public class VoceLeRapido {
    public static void main(String[] args) {
        // Força o Scanner e a saída a usarem PONTO (.) para decimais
        Scanner ent = new Scanner(System.in).useLocale(Locale.US);
        
        System.out.println("Digite seu nome: ");
        String nomeUsuario = ent.nextLine();
        
        System.out.println("Digite o nome do livro: ");
        String nomeDoLivro = ent.nextLine();
        
        System.out.println("Digite a quantidade de páginas do livro: ");
        int quantidadeDePaginas = ent.nextInt();
        
        System.out.println("Digite o tempo em segundos que você leva para ler uma página: ");
        double tempoPorPagina = ent.nextDouble();
        ent.nextLine(); 
        
        System.out.printf(Locale.US, "Olá, %s!%n", nomeUsuario);
        

        double tempoEmSegundos = (double) quantidadeDePaginas * tempoPorPagina;
        double tempoEmHoras = tempoEmSegundos / 3600.0;
        double tempoEmMinutos = tempoEmSegundos / 60.0;
        
        System.out.printf(Locale.US, "Você vai ler o livro %s em %.2f horas (aproximadamente %.2f minutos).%n", nomeDoLivro, tempoEmHoras, tempoEmMinutos);

        ent.close();
    }
}