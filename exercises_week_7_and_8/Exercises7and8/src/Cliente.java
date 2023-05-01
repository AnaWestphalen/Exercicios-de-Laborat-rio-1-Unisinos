public class Cliente {
    private String nome;
    private int idade;
    private char sexo;
    private String email;
    private String senha;
    private Livro livro;

    public Cliente(){
    }

    public Cliente(String nome, int idade, char sexo, String email, String senha, Livro livro){
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
        this.email = email;
        this.senha = senha;
        this.livro = livro;
    }

    public Cliente(String nome, int idade, Livro livro){
        this.nome = nome;
        this.idade = idade;
        this.livro = livro;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public int getIdade(){
        return idade;
    }

    public void setIdade(int idade){
        this.idade = idade;
    }

    public char getSexo(){
        return sexo;
    }

    public void setSexo(char sexo){
        this.sexo = sexo;
    }

    public String getEmail(){
        return email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String getSenha(){
        return senha;
    }

    public void setSenha(String senha){
        this.senha = senha;
    }

    public Livro getLivro(){
        return livro;
    }

    public void setLivro(Livro livro){
        this.livro = livro;
    }

    public void imprimeInformacoes(){
        System.out.println("Nome: "+nome);
        System.out.println("Idade: "+idade);
        System.out.println("Sexo: "+sexo);
        System.out.println("Email: "+email);
        System.out.println("Senha: "+senha);
        System.out.println("Livro: "+livro);
    }

    public String toString(){
        return "Cliente{" +
                "Nome:'" + nome + '\'' +
                ", Idade:'" + idade + '\'' +
                ", Sexo:'" + sexo + '\'' +
                ", Email:" + email +
                ", Senha:" + senha +
                ", Livro:" + livro +
                '}';
    }
}
