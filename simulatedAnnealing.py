'''
@author: GEOVANI PEREIRA DOS SANTOS
Simulated annealing

IFNMG - MONTES CLAROS - MG - 2018
'''

import random
import math

''' gera a matriz inicial ,e ela é aleatoria'''
def gerarMatriz(tam):
    matriz =[]
    for i in range(tam):
        matriz.append([0]*tam)
        
    rainhas = random.sample(range(tam), tam)
    
    for i in range(tam):
        matriz[rainhas[i]][i] = 1
    return matriz
    

'''gerar um vizinho aleatorio'''
def vizinho(item):
    viz = item[:]
    a = random.randrange(len(viz))
    b = random.randrange(len(viz))
    aux = viz[a][:]
    viz[a] = viz[b][:]
    viz[b] = aux[:]
    return viz
    
'''funcao objetivo'''
def f(num):
    return checkColuna(num)+checkDiagonal(num)+checkLinha(num)

def checkColuna(item):
    tam = len(item)
    result = 0
    for i in range (0,tam):
        aux =0
        for j in range(0,tam):
            if item[i][j] == 1:
                aux +=1 
        if aux > 1:
            result += aux-1
    return result

def checkLinha(item):
    tam = len(item)
    result = 0
    for i in range (0,tam):
        aux =0
        for j in range(0,tam):
            if item[j][i] == 1:
                aux +=1 
        if aux > 1:
            result += aux-1
    return result


def checkDiagonal(item):
    result = subDiagonal1(item) + subDiagonal2(item)
    inverteLinhas(item)
    result += subDiagonal1(item) + subDiagonal2(item)
    result += checkColuna(item) + checkLinha(item)
    inverteLinhas(item)
    return result

'''DIAGONAL PRINCIPAL, COLUNAS '''
def subDiagonal1(item):
    tam = len(item)
    aux = 0
    result =0
    for i in range(tam-1):
        aux = 0
        for j in range(tam - i): 
            if item[j][j+i] == 1:
                aux +=1 
        if aux > 1:
            result += aux-1
    return result
            
'''DIAGONAL PRINCIPAL, LINHAS '''  
def subDiagonal2(item):
    result = 0 
    aux = 0
    tam = len(item)     
    for i in range(1, tam-1):      
        aux = 0  
        for j in range(0,tam - i): 
            if item[j+i][j] == 1:
                aux +=1 
        if aux > 1:
            result += aux-1      
    return result

def inverteLinhas(item):
    for i in item:
        i.reverse()


def simulatedAnnealing(t0,s0):
    t = t0
    sestrela = atual = s0 
    iteracao = 0
    while t > 0 and iteracao <= 666:
        slinha = vizinho(atual)
        f_slinha = f(slinha)
        f_sestrela = f(sestrela)
        delta = f_slinha - f(atual)
        iteracao += 2
        if delta < 0:
            atual = slinha
            if f_slinha < f_sestrela:
                sestrela = slinha
                f_sestrela = f_slinha
            iteracao += 1
        elif random.random() < (math.exp((-1 * delta)/t)):
            atual = slinha
        t = t-1
        plotS.append(f_sestrela)
        plotT.append(t)

    return sestrela

x = 8
t = 1000

print(simulatedAnnealing(t, gerarMatriz(x)))

        

