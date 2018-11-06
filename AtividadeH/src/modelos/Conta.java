package modelos;

public class Conta {
    private String proprietario;
    private int numero;
    private float saldo;

    public String getProprietario() {
        return proprietario;
    }

    public void setProprietario(String proprietario) {
        this.proprietario = proprietario;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public void sacar(float valor){
        if (valor < getSaldo()){
            setSaldo(getSaldo() - valor);
        }
    }

    public void depositar(float valor){
        setSaldo(getSaldo() + valor);
    }

}
