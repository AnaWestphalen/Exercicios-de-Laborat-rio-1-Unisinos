public class FuncionarioCaixa {
    private String nome;
    private String endereco;
    private char sexo;
    private Calculadora calculadora;

    public FuncionarioCaixa(){
        this.nome = null;
        this.endereco = null;
        this.sexo = ' ';
        this.calculadora = null;
    }

    public FuncionarioCaixa(String nome, String endereco, char sexo, Calculadora calculadora){
        this.nome = nome;
        this.endereco = endereco;
        this.sexo = sexo;
        this.calculadora = calculadora;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getEndereco(){
        return endereco;
    }

    public void setEndereco(String endereco){
        this.endereco = endereco;
    }

    public char getSexo(){
        return sexo;
    }

    public void setSexo(char sexo){
        this.sexo = sexo;
    }

    public Calculadora getCalculadora(){
        return calculadora;
    }

    public void setCalculadora(Calculadora calculadora){
        this.calculadora = calculadora;
    }

    public double soma(double num1, double num2){
        double resultadoSoma = calculadora.soma(num1, num2);
        return resultadoSoma;
    }

    public double subtrai(double num1, double num2){
        double resultadoSubtrai = calculadora.subtrai(num1, num2);
        return resultadoSubtrai;
    }

    public double multiplica(double num1, double num2){
        double resultadoMultiplica = calculadora.multiplica(num1, num2);
        return resultadoMultiplica;
    }

    public double divide(double num1, double num2){
        double resultadoDivide = calculadora.divide(num1, num2);
        return resultadoDivide;
    }

    public int elevaAoQuadrado(int num1){
        int resultadoElevaAoQuadrado = calculadora.elevaAoQuadrado(num1);
        return resultadoElevaAoQuadrado;
    }

    public int elevaAoCubo(int num1){
        int resultadoElevaAoCubo = calculadora.elevaAoCubo(num1);
        return resultadoElevaAoCubo;
    }

    public String imprimeInfo(){
        return "Funcionário{" +
                "Nome:'" + nome + '\'' +
                ", Endereço:'" + endereco + '\'' +
                ", Sexo:'" + sexo + '\'' +
                ", Calculadora:'" + calculadora.imprimeInfo() + '\'' +
                '}';
    }
}

