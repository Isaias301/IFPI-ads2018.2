package app;
import modelos.ContaCorente;


public class App {
    public static void main(String[] args){
        ContaCorente conta = new ContaCorente("isaias", 78667567, false);
        conta.setLimite(100);
        conta.depositar(100);
        conta.sacar(50);
        conta.depositar(1000);

        System.out.println("Número: " + conta.getNumero());
        System.out.println("Proprietário: " + conta.getProprietario());
        System.out.println("Especial: " + conta.getEspecial());
        System.out.println("Limíte: " + conta.getLimite());
        System.out.println("Saldo: " + conta.getSaldo());
    }
}
