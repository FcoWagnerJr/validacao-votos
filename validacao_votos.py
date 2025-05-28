from datetime import date
atual = date.today().year
def voto(v): 
    if v < 16:
        return 'VOTO NEGADO'
    elif v >= 16 and v < 18:
       return 'VOTO OPCIONAL'
    elif v >= 18 and v < 70:
        return 'VOTO OBRIGATÓRIO'
    elif v >= 70:
        return 'VOTO OPCIONAL'

ano = int(input("Em que ano você nasceu? "))
idade = atual - ano 
print(f'Com {idade} anos: {voto(idade)}')
print('>>> FIM DA EXECUÇÃO <<<')