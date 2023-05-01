import javax.crypto.spec.PSource;
import java.sql.SQLOutput;

public class Main {
    public static void main(String[] args) {
        //Criar uma instância de Livro com o construtor sem parâmetros
        Livro livro1 = new Livro();
        Livro livro2 = new Livro();
        Livro livro3 = new Livro();


        //Criar uma instância de Cliente passando todos as infos pelo teclado e dentro dessa instância de cliente eu
        // coloco os atributos do objeto livro via teclado.
        //Tenho que chamar o contrutor do objeto Livro dentro do construtor do objeto Cliente
        Cliente cliente1 = new Cliente(Teclado.leString("Nome: "),
                                       Teclado.leInt("Idade: "),
                                       Teclado.leChar("Sexo: "),
                                       Teclado.leString("Email: "),
                                       Teclado.leString("Senha: "),
                                       livro1 = new Livro(Teclado.leString("Título: "),
                                                          Teclado.leString("Autor: "),
                                                          Teclado.leString("Ano de Publicação: "),
                                                          Teclado.leDouble("Preço: R$"),
                                                          Teclado.leInt("Quantidade de páginas: ")));

        Cliente cliente2 = new Cliente(Teclado.leString("Nome: "),
                                       Teclado.leInt("Idade: "),
                                       Teclado.leChar("Sexo: "),
                                       Teclado.leString("Email: "),
                                       Teclado.leString("Senha: "),
                                       livro2 = new Livro(Teclado.leString("Título: "),
                                                          Teclado.leString("Autor: "),
                                                          Teclado.leString("Ano de Publicação: "),
                                                          Teclado.leDouble("Preço: R$"),
                                                          Teclado.leInt("Quantidade de páginas: ")));

        Cliente cliente3 = new Cliente(Teclado.leString("Nome: "),
                                       Teclado.leInt("Idade: "),
                                       Teclado.leChar("Sexo: "),
                                       Teclado.leString("Email: "),
                                       Teclado.leString("Senha: "),
                                       livro3 = new Livro(Teclado.leString("Título: "),
                                                          Teclado.leString("Autor: "),
                                                          Teclado.leString("Ano de Publicação: "),
                                                          Teclado.leDouble("Preço: R$"),
                                                          Teclado.leInt("Quantidade de páginas: ")));

        System.out.println("O cliente " + cliente1.getNome() + " está com o livro " + livro1.getTitulo() +
                           " e o preço por página deste livro é R$" + String.format( "%.2f", livro1.calcularPrecoPorPagina()) +".");
        System.out.println("O cliente " + cliente2.getNome() + " está com o livro " + livro2.getTitulo() +
                           " e o preço por página deste livro é R$" + String.format( "%.2f", livro2.calcularPrecoPorPagina()) +".");
        System.out.println("O cliente " + cliente3.getNome() + " está com o livro " + livro3.getTitulo() +
                           " e o preço por página deste livro é R$" + String.format( "%.2f", livro3.calcularPrecoPorPagina()) +".");
    }

}

