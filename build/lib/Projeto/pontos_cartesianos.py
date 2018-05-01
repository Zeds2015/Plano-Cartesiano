if __name__ == '__main__':
    from projeto import PontosEm2D
    from math import sqrt
    import numpy as np
    import matplotlib.pyplot as pyplot
    import re

    def somar(a,b):
        return a+b

    def subtrair(a,b):
        return a-b

    def multiplicar(a,b):
        return a*b

    def dividir_inteiro(a,b):
            a.converter_para_int()
            b.converter_para_int()
            if b.x != 0 and b.y != 0:
                return a//b
            else:
                print('Impossivel dividir por zero, uma divisao inteira nao pode ter valores menores que um, no denominador!')

    def dividir_float(a,b):
        if b.x != 0 and  b.y != 0:
            return a/b


    def verificar_igualdade(a,b):
        return a == b

    def mostrar_ponto(a,nome=''):
        x = np.array([a.x,0])
        y = np.array([0,a.y])
        pyplot.plot(x,y)
        pyplot.xlabel('Eixo X')
        pyplot.ylabel('Eixo Y')
        pyplot.xlim(-0.2,a.x+0.02)
        pyplot.ylim(-0.2,a.y+0.2)
        pyplot.title('Sobre o vetor '+nome)
        pyplot.show()

    def ver_coordenada(a):
        mostrar_ponto(a)
        return """
                Coordenada x = {x}
                Coordenada y = {y}
                Tamanho do vetor = {t}
                """.format(x=a.x,y=a.y,t = sqrt(a.x**2 + a.y**2))

    def retorna_valores_das_tuplas(entrada,j):
        lista = [i for i in re.findall(r'([\d]*\.[\d]*|[\d]*)', entrada[j])]
        lista = list(filter(lambda x: x != '',lista))
        return [float(i) for i in lista]

    def conferir_entrada(entrada,operacoes):
        achou = True
        for i in range(1,len(entrada),2):
            if entrada[i] not in operacoes:
                achou = False
        return achou

    def definir_pontos(entrada):
        pontos_cartesianos = []
        for j in range(len(entrada)):
            if j % 2 != 0:
                continue
            valores = retorna_valores_das_tuplas(entrada, j)
            pontos_cartesianos.append(PontosEm2D(float(valores[0]),float(valores[1])))
        return pontos_cartesianos

    def realizar_operacao_item_sem_prioridade_depois(operacoes, entrada,pontos_cartesianos,k,identidade = PontosEm2D()):
        resultado = operacoes[entrada[k]](pontos_cartesianos[(k-1)//2],pontos_cartesianos[(k+1)//2])
        pontos_cartesianos[(k+1)//2] = resultado
        return operacoes[entrada[k]](resultado,identidade)

    def realizar_operacao_item_sem_prioridade_antes(operacoes, entrada,pontos_cartesianos,k,identidade = PontosEm2D()):
        resultado = operacoes[entrada[k]](pontos_cartesianos[(k-1)//2],pontos_cartesianos[(k+1)//2])
        pontos_cartesianos[(k-1)//2] = resultado
        return operacoes[entrada[k]](resultado,identidade)

    def operar_nos_pontos(pontos_cartesianos,entrada,operacoes):
        ocorrencias_tipo_a = lambda lst: (i for i,e in enumerate(lst) if e in ['*','/','//'])
        lista_de_ocorrencias_tipo_a = list(ocorrencias_tipo_a(entrada))
        ocorrencias_tipo_b = lambda lst: (i for i,e in enumerate(lst) if e in ['+','-'])
        lista_de_ocorrencias_tipo_b = list(ocorrencias_tipo_b(entrada))
        ocorrencias_tipo_c = lambda lst: (i for i,e in enumerate(lst) if e in ['==','sobre'])
        lista_de_ocorrencias_tipo_c = list(ocorrencias_tipo_c(entrada))
        assert not (any([k < i for i in lista_de_ocorrencias_tipo_a for k in lista_de_ocorrencias_tipo_b]) and len(lista_de_ocorrencias_tipo_a) > 0)
        
        pos_op = lista_de_ocorrencias_tipo_a+lista_de_ocorrencias_tipo_b+lista_de_ocorrencias_tipo_c
        for k in pos_op:
            if k in lista_de_ocorrencias_tipo_a and any([i > k for i in lista_de_ocorrencias_tipo_b]):
                resultado = realizar_operacao_item_sem_prioridade_depois(operacoes,entrada,pontos_cartesianos,k,PontosEm2D(1,1))

            elif k in lista_de_ocorrencias_tipo_a:
                resultado = realizar_operacao_item_sem_prioridade_antes(operacoes,entrada,pontos_cartesianos,k,PontosEm2D(1,1))

            elif k in lista_de_ocorrencias_tipo_b:
                resultado = realizar_operacao_item_sem_prioridade_depois(operacoes,entrada,pontos_cartesianos,k)

            else:
                if entrada[k] == 'sobre':
                    identidade = pontos_cartesianos[(k-1)//2]
                    print(operacoes[entrada[k]](identidade))
                elif entrada[k] == '==':
                    print(operacoes[entrada[k]](pontos_cartesianos[(k-1)//2],pontos_cartesianos[(k+1)//2]))     
        print(resultado)

    def inicio():
        operacoes = {'+':somar, '*':multiplicar, '-':subtrair, '/':dividir_float, '//': dividir_inteiro, '==': verificar_igualdade, 'sobre': ver_coordenada}
        print('''Digite desta forma (n,m) operacao (z,e), se voce digitar (a.b) entao sera entendido (a,0.b).
Utilize os operadores de maiores precedencia na frente neste padrao 1- (*|/|//) 2- (+|-) 3- (==) | 1- (*|/|//) 2- (+|-) 3- (==) caso queira ver
o vetor digite (sobre) no final, caso queira sair digite (quit)\n''')
        while True:
            entrada = input('>> ').split(' ')
            if entrada.count('quit') > 0:
                break
            try:  
                if conferir_entrada(entrada,operacoes):
                        operar_nos_pontos(definir_pontos(entrada),entrada,operacoes)        
                else:
                    print('Formato incorreto')
            except (IndexError, AssertionError):
                print('Formato de entrada invalido')
    inicio()