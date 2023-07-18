from aluno import Aluno
from arquivo import criar_arquivo

alunos = [
    Aluno("Douglas", [10,10,8], "douglas@email.com"),
    Aluno("Gabriel", [5,9,7], "gabriel@email.com"),
    Aluno("Silva", [4,5,3], "silva@email.com"),
    Aluno("Gomes", [10,9,9], "gomes@email.com")
]

# primeiro_aluno = alunos[0]
# print(primeiro_aluno.get_media_nota())

# linhas_alunos_aprovados = [f"{aluno.get_linha_arquivo()}\n" for aluno in alunos if aluno.get_situacao() == "APROVADO"]
# linhas_alunos_reprovados = [f"{aluno.get_linha_arquivo()}\n" for aluno in alunos if aluno.get_situacao() == "REPROVADO"]

# print(alunos_aprovados)
# print(alunos_reprovados)
# criar_arquivo(
#     "saida/alunos_aprovados.txt", 
#     linhas_alunos_aprovados,
#     "ALUNOS APROVADOS: "
# )

def alunos_aprovados():
    return [aluno for aluno in alunos if aluno.get_situacao() == 'APROVADO']

def alunos_reprovados():
    return [aluno for aluno in alunos if aluno.get_situacao() == 'REPROVADO']

def gerar_alunos_aprovados():
    linhas_alunos_aprovados = [f"{aluno.get_linha_arquivo()}\n" for aluno in alunos if aluno.get_situacao() == "APROVADO"]
    criar_arquivo(
        "saida/alunos_aprovados.txt", 
        linhas_alunos_aprovados,
        "ALUNOS APROVADOS: "
    )

def gerar_alunos_reprovados():
    linhas_alunos_reprovados = [f"{aluno.get_linha_arquivo()}\n" for aluno in alunos if aluno.get_situacao() == "REPROVADO"]
    criar_arquivo(
        "saida/alunos_reprovados.txt", 
        linhas_alunos_reprovados,
        "ALUNOS REPROVADOS: "
    )


def email_aprovados():
    alunos = alunos_aprovados()
    for aluno in alunos:
        print(f'{aluno.nome_completo} {aluno.email}')