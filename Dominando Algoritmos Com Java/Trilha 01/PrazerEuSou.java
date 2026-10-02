import java.util.Scanner;

public class PrazerEuSou {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        
        System.out.println("Digite seu nome: ");
        String nome = ent.nextLine();
        
        System.out.println("Digite seu curso: ");
        String curso = ent.nextLine();
        
        System.out.println("Digite seu semestre: ");
        int semestre = ent.nextInt();
        ent.nextLine(); 
        
        System.out.println("Digite seu hoobby: ");
        String hoobby = ent.nextLine();
        
        System.out.println("Prazer, eu sou " + nome + "!");
        System.out.println("Estudo " + curso + " no semestre " + semestre + "º");
        System.out.println("Meu hobby é " + hoobby);
        
        ent.close();
    }
}