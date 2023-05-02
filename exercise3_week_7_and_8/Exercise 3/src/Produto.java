public class Produto {
    private String nome;
    private double preco;
    private Data dataDeValidade;

    public Produto(String nome, double preco, Data dataDeValidade){
        this.nome = nome;
        this.preco = preco;
        this.dataDeValidade = dataDeValidade;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(){
        this.nome = nome;
    }

    public double getPreco(){
        return preco;
    }

    public void setPreco(){
        this.preco = preco;
    }

    public Data getDataDeValidade(){
        return dataDeValidade;
    }

    public void setDataDeValidade(){
        this.dataDeValidade = dataDeValidade;
    }

    /**
     * Retorna o false se o produto não está vencido de acordo com a dataRecebida e a dataValidade.
     * Retorna o true se o produto está vencido de acordo com a dataRecebida.
     */
    public boolean verificaProdutoVencido(Data dataRecebida){
        if(dataRecebida.getAno() < dataDeValidade.getAno())
            return false;
        else if(dataRecebida.getAno() == dataDeValidade.getAno())
            if(dataRecebida.getMes() < dataDeValidade.getMes())
                return false;
            else if(dataRecebida.getMes() == dataDeValidade.getMes())
                if(dataRecebida.getDia() <= dataDeValidade.getDia())
                    return false;

        return true;
    }

    public String toString() {
        return "Produto{" +
                "Nome do produto:'" + nome + '\'' +
                ", Preço: R$" + preco + '\'' +
                ", Data de validade: " + dataDeValidade.toString() +
                '}';
    }
}
