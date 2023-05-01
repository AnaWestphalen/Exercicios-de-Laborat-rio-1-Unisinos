public class Calculadora {
    private int memoria;
    private String cor;

    public Calculadora(String cor){
        this.memoria = 0;
        this.cor = cor;
    }

    public int getMemoria(){
        return memoria;
    }

    public void setMemoria(int memoria){
        this.memoria = memoria;
    }

    public String getCor(){
        return cor;
    }

    public void setCor(String cor){
        this.cor = cor;
    }

    public double soma(double num1, double num2){
        double resultadoSoma = (num1 + num2);
        return resultadoSoma;
    }

    public double subtrai(double num1, double num2){
        double resultadoSubtrai = (num1 - num2);
        return resultadoSubtrai;
    }

    public double multiplica(double num1, double num2){
        double resultadoMultiplica = (num1 * num2);
        return resultadoMultiplica;
    }

    public double divide(double num1, double num2){
        double resultadoDivide = (num1 / num2);
        return resultadoDivide;
    }

    public int elevaAoQuadrado(int num1){
        int resultadoElevaAoQuadrado = (num1 * num1);
        return resultadoElevaAoQuadrado;
    }

    public int elevaAoCubo(int num1){
        int resultadoElevaAoCubo = (num1 * num1 * num1);
        return resultadoElevaAoCubo;
    }

    public String imprimeInfo(){
        return "Calculadora{" +
                "Memória:'" + memoria + '\'' +
                ", Cor:'" + cor + '\'' +
                '}';
    }
}
