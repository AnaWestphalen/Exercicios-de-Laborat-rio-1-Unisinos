public class Main
{
    public static void main (String args[]) {
        // cria uma prateleira com 3 produtos
        System.out.println("-- Cadastro de produtos Prateleira 1 ---");
        double preco;

        System.out.println("-> Produto 1");
        do {
            preco = Teclado.leDouble("Digite o preço do produto: R$ ");
            if (preco <= 0) {
                System.out.println("O preço deve ser maior do que zero! Tente novamente!");
            }
        } while (preco <= 0);

        Produto p1 = new Produto("Amaciante", preco, new Data(10, 4, 2014));

        System.out.println("-> Produto 2");
        do {
            preco = Teclado.leDouble("Digite o preço do produto: R$ ");
            if (preco <= 0) {
                System.out.println("O preço deve ser maior do que zero! Tente novamente!");
            }
        } while (preco <= 0);

        Produto p2 = new Produto("Creme Dental", preco, new Data(5, 5, 2015));

        System.out.println("-> Produto 3");
        do {
            preco = Teclado.leDouble("Digite o preço do produto: R$ ");
            if (preco <= 0) {
                System.out.println("O preço deve ser maior do que zero! Tente novamente!");
            }
        } while (preco <= 0);
        Produto p3 = new Produto("Leite Condensado", preco, new Data(4, 12, 2012));

        Prateleira prat1 = new Prateleira(p1, p2, p3);

        // cria uma prateleira sem produtos e adiciona a cortina
        System.out.println("\n-- Cadastro de produtos Prateleira 2 --");
        Produto cortina = new Produto("cortina", 167.98, new Data(13, 10, 2025));
        //public Prateleira()
        Prateleira prat2 = new Prateleira();
        prat2.setProduto1(cortina);
        System.out.printf("%s", cortina);

        // cria um mercado com as duas prateleiras
        //public Mercado(Prateleira p1, Prateleira p2)
        Mercado mercado = new Mercado(prat1, prat2);

        System.out.println("\n\n\t-------- MERCADO JAVA --------");
        System.out.print(prat1);
        System.out.print((mercado.getPrateleira2()).toString());

        System.out.print("\n-- Produtos Vencidos --");
        // mostra as informações dos produtos vencidos (supondo a data 25/04/2023)
        Data dataAtual = new Data(25, 4, 2023);
        //Prateleira 1
        if ((mercado.getPrateleira1()).getProduto1() != null)
            if (((mercado.getPrateleira1()).getProduto1()).verificaProdutoVencido(dataAtual))
                System.out.printf("\n%s: Produto Vencido", ((mercado.getPrateleira1()).getProduto1()).getNome());

        if ((mercado.getPrateleira1()).getProduto2() != null)
            if (((mercado.getPrateleira1()).getProduto2()).verificaProdutoVencido(dataAtual))
                System.out.printf("\n%s: Produto Vencido", ((mercado.getPrateleira1()).getProduto2()).getNome());

        if ((mercado.getPrateleira1()).getProduto3() != null)
            if (((mercado.getPrateleira1()).getProduto3()).verificaProdutoVencido(dataAtual))
                System.out.printf("\n%s: Produto Vencido", ((mercado.getPrateleira1()).getProduto3()).getNome());

        //Prateleira 2
        if ((mercado.getPrateleira2()).getProduto1() != null)
            if (((mercado.getPrateleira2()).getProduto1()).verificaProdutoVencido(dataAtual))
                System.out.printf("\n%s: Produto Vencido", ((mercado.getPrateleira2()).getProduto1()).getNome());

        if ((mercado.getPrateleira2()).getProduto2() != null)
            if (((mercado.getPrateleira2()).getProduto2()).verificaProdutoVencido(dataAtual))
                System.out.printf("\n%s: Produto Vencido", ((mercado.getPrateleira2()).getProduto2()).getNome());

        if ((mercado.getPrateleira2()).getProduto3() != null)
            if (((mercado.getPrateleira2()).getProduto3()).verificaProdutoVencido(dataAtual))
                System.out.printf("\n%s: Produto Vencido", ((mercado.getPrateleira2()).getProduto3()).getNome());

        // imprime as informações do produto mais caro do mercado
        System.out.print("\n\n-- Produto mais Caro --");
        if ((mercado.getPrateleira1()).produtoMaisCaro() != null)
        {
            if (((mercado.getPrateleira1()).produtoMaisCaro()).getPreco() > ((mercado.getPrateleira2()).getProduto1()).getPreco())
                System.out.printf("\n%s R$ %.2f", ((mercado.getPrateleira1()).produtoMaisCaro()).getNome(),((mercado.getPrateleira1()).produtoMaisCaro()).getPreco());
            else if (((mercado.getPrateleira2()).getProduto1()).getPreco() > ((mercado.getPrateleira1()).produtoMaisCaro()).getPreco())
                System.out.printf("\n%s R$ %.2f", ((mercado.getPrateleira2()).getProduto1()).getNome(),((mercado.getPrateleira2()).getProduto1()).getPreco());
            else{
                System.out.print("\nDois preços iguais: ");
                System.out.printf("\n%s R$ %.2f", ((mercado.getPrateleira1()).produtoMaisCaro()).getNome(),((mercado.getPrateleira1()).produtoMaisCaro()).getPreco());
                System.out.printf("\n%s R$ %.2f", ((mercado.getPrateleira2()).getProduto1()).getNome(),((mercado.getPrateleira2()).getProduto1()).getPreco());
            }
        }

        // imprime a média de preço dos produtos do mercado
        System.out.println("\n\n-- Média de preço dos produtos --");
        System.out.printf("Média de preço: R$ %.2f", mercado.mediaValorProdutos());
    }
}
