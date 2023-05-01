public class Livro {
    private String titulo;
    private String autor;
    private String anoDePublicacao;
    private double preco;
    private int quantidadeDePaginas;

    public Livro(){
    }

    public Livro(String titulo, String autor, String anoDePublicacao, double preco, int quantidadeDePaginas){
        this.titulo = titulo;
        this.autor = autor;
        this.anoDePublicacao = anoDePublicacao;
        this.preco = preco;
        this.quantidadeDePaginas = quantidadeDePaginas;
    }

    public String getTitulo(){
        return titulo;
    }

    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public String getAutor(){
        return autor;
    }

    public void setAutor(String autor){
        this.autor = autor;
    }

    public String getAnoDePublicacao(){
        return anoDePublicacao;
    }

    public void setAnoDePublicacao(String anoDePublicacao){
        this.anoDePublicacao = anoDePublicacao;
    }

    public double getPreco(){
        return preco;
    }

    public void setPreco(double preco){
        this.preco = preco;
    }

    public int getQuantidadeDePaginas(){
        return quantidadeDePaginas;
    }

    public void setQuantidadeDePaginas(int quantidadeDePaginas){
        this.quantidadeDePaginas = quantidadeDePaginas;
    }

    public double calcularPrecoPorPagina(){
        return (preco / quantidadeDePaginas);
    }

    public String toString(){
        return "Livro{" +
                "Título:'" + titulo + '\'' +
                ", Autor:'" + autor + '\'' +
                ", Ano de Publicação:'" + anoDePublicacao + '\'' +
                ", Preço:" + preco +
                ", Quantidade de Páginas:" + quantidadeDePaginas +
                '}';
    }
}
