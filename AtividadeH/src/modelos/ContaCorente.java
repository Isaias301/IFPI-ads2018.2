package modelos;

public class ContaCorente extends Conta {
    private boolean especial;
    private float limite;
    // cartao de credito
    // emprestimo

    public ContaCorente(String proprietario, int numero, boolean especial){
        this.setProprietario(proprietario);
        this.setNumero(numero);
        this.setEspecial(especial);

    }


    public boolean getEspecial() {
        return especial;
    }

    public void setEspecial(boolean especial) {
        this.especial = especial;
    }

    public float getLimite() {
        return limite;
    }

    public void setLimite(float limite) {
        if (this.especial) {
            this.limite = limite;
        }
    }

    public void transferencia(String conta, float valor){

    }

}
