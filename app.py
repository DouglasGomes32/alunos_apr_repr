import controle_alunos

while True:
    print('1 - Gerar arquivo de alunos aprovados e reprovados \n2 - Enviar e-mail para alunos aprovados \n3 - sair')
    opcao_escolhida = input('Digite uma opção: ')
    
    match opcao_escolhida:
        case '1':
            controle_alunos.gerar_arquivos_reprovados()
            controle_alunos.gerar_arquivos_aprovados()
            print('Os arquivos foram gerados com sucesso na pasta saida/')
        case '2':
            controle_alunos.email_aprovados()
        case '3':
            break
        case _:
            print('Opção invalida')