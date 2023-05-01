public class Main {
    public static void main(String[] args){
        //Criar uma instância de Calculadora com o construtor sem parâmetros
        Calculadora calculadora1 = new Calculadora(Teclado.leString("cor: "));

        //Criar uma instância de Funcionário passando todos as infos pelo teclado e dentro dessa instância de cliente eu
        // coloco os atributos do objeto calculadora via teclado.
        //Tenho que chamar o contrutor do objeto Calculadora dentro do construtor do objeto FuncionarioCaixa
        FuncionarioCaixa funcionario1 = new FuncionarioCaixa(Teclado.leString("Nome do funcionário 1: "),
                                                             Teclado.leString("Endereço do funcionário 1: "),
                                                             Teclado.leChar("Sexo: "),
                                                             calculadora1);

        FuncionarioCaixa funcionario2 = new FuncionarioCaixa(Teclado.leString("Nome do funcionário 2: "),
                                                             Teclado.leString("Endereço do funcionário 2: "),
                                                             Teclado.leChar("Sexo: "),
                                                             calculadora1);

        Empresa empresa1 = new Empresa(Teclado.leString("Nome da empresa: "),
                                       funcionario1,
                                       funcionario2);

        double resultadoSoma = funcionario1.getCalculadora().soma(2, 2);
        double resultadoSubtrai = funcionario1.getCalculadora().subtrai(5, 4);
        double resultadoMultiplica = funcionario1.getCalculadora().multiplica(2, 3);
        double resultadoDivide = funcionario1.getCalculadora().divide(6, 3);
        int resultadoElevaAoQuadrado = funcionario1.getCalculadora().elevaAoQuadrado(72);
        int resultadoElevaAoCubo = funcionario1.getCalculadora().elevaAoCubo(83);

        System.out.println(resultadoSoma);
        System.out.println(resultadoSubtrai);
        System.out.println(resultadoMultiplica);
        System.out.println(resultadoDivide);
        System.out.println(resultadoElevaAoQuadrado);
        System.out.println(resultadoElevaAoCubo);

        System.out.println(empresa1.imprimeInfo());
    }
}
