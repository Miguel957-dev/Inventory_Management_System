

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("0. Para fechar sistema.")
        print("1. Cadastrar produtos.")
        print("2. Consulta individual de produtos.")
        print("3. Listar de produtos.")
        print("4. Atualizar informações.")
        print("5. Excluir produto.")
        print("6. Registro de entradas.")
        print("7. Registro de saída.")
        print("8. Histórico de movimentações.")
        print("9. Identificar produtos com estoque baixo.")
        print("10. Relatório de valor total do estoque.")
        
        opçao = int(input('Escolha uma opção:'))
        if 0 <= opçao <= 10:
            match opçao:
                case 0:
                    print('Sistema fechado!')
                    break

                case 1:
                    print()

        else:
            print("escolha uma opção valída")
if __name__=="__main__":
    main()