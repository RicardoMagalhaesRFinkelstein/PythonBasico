frase = 'Ai meu deus como é bom ser piranha'

                            ######## MANIPULAÇÕES BÁSICAS #############
#imprimindo a string somente na posição dentro do vetor
print (frase[0])
#imprimindo a string entre a posição inicial e a posição final, sem contar a posição final (10 até 29)
print (frase[10:30])
#mesma coisa que o anterior, só que pulando de 2 em 2
print (frase[5:24:2])
#inicia do 0. mesma coisa que escrever frase[0:8]
print (frase[:8])
#imprime do ponto especificado até o final da string
print (frase[16:])
#imprime do ponto especificado até o final, pulando de 3 em 3
print (frase[10::3])

                            ########### ANÁLISE DE STRING #############
#tamanho da string
print(len(frase))
#conta as ocorrências de x na string
print(frase.count('a'))
#mesma coisa que o anterior, porém dentro de um range
print(frase.count('i',0,20))
#retorna a primeira posição na qual o valor foi achado. caso não ache, retorna -1
print(frase.find('deus'))
#verifica se existe o valor requisitado dentro da variável
print('bom' in frase)

                            ######### TRANSFORMAÇÃO DE STRING #########
#troca o primeiro valor (caso exista) na string pelo segundo. pra mudança ser permanente, deve-se fazer com que frase = frase.replace...
print(frase.replace('piranha','inteligente'))
#joga tudo pra maiúsculo. .lower faz o inverso. capitalize joga tudo pra minúsculo e deixa o primeiro em maiúsculo. title faz o mesmo que o capitalize, mas para todas as palavras
print(frase.upper())

fraseNova = '   Aprenda Python  '
#remove os espaços inúteis (no começo e no fim da string. se tiver 45 espaços no meio de duas palavras, eles ficam)
print(fraseNova.strip())
#semelhante ao anterior, porém só remove o escedente na direita, não na esquerda. pra se fazer o oposto, basta usar o lstrip
print(fraseNova.rstrip())
                            ######### DIVISÃO DE STRING ###############
#cada palavra da string vira um sub-vetor
frase = frase.split()
#join os une
print('-'.join(frase))

#print com """ no início e no fim imprime o texto sem perder a formatação. Exemplo
print("""Um álbum de estúdio é uma coleção de gravações de áudio emitidas como uma coleção em disco compacto (CD), 
vinil, fita de áudio ou outro meio. Álbuns de som gravado foram desenvolvidos no início do século XX como 
registros individuais de 78 rpm coletados em um álbum encadernado que lembra um álbum de fotografia; este 
formato evoluiu depois de 1948 em vinil individuais LPs tocada em 331⁄3 rpm.""")