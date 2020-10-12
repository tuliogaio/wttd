"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

''' def solution_one(a, b):
    # +++ SUA SOLUÇÃO +++
    a_frente = a[ : int( len(a) / 2 + ( len(a) % 2 ) ) ]
    a_atras = a[ int( -len(a) / 2 ) : ]
    b_frente = b[ : int( len(b) / 2 + ( len(b) % 2 ) ) ]
    b_atras = b[ int( -len(b) / 2 ) : ]
    return a_frente + b_frente + a_atras + b_atras '''

''' def solution_two(a, b):
    # +++ SUA SOLUÇÃO +++
    a_frente = string_lenght(a)
    a_atras = string_lenght(a, "back")
    b_frente = string_lenght(b)
    b_atras = string_lenght(b, "back")
    return a_frente + b_frente + a_atras + b_atras '''

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    return ''.join([string_lenght(a), string_lenght(b), string_lenght(a, "back"), string_lenght(b, "back")])

def string_lenght(s, pos="front"):
    lenght = len(s)
    return s[ : int( lenght / 2 + ( lenght % 2 ) ) ] if pos=="front" else s[ int( -lenght / 2 ) : ] 


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
    test(front_back, ('Testando ', 'Outra Coisa'), 'TestaOutra ndo Coisa')
