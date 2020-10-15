"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""
import string
def front_x(words):
    # +++ SUA SOLUÇÃO +++
    words.sort()
    custom_order = list(string.ascii_lowercase)
    custom_order.insert(0,'x')
    ordered = sorted(words, key=lambda words: custom_order.index(words[0]))
    return ordered

def solution_two(words):
    # +++ SUA SOLUÇÃO +++
    comecam_com_x = sorted([w for w in words if w[0] == 'x'])
    comecam_sem_x = sorted([w for w in words if w[0] != 'x'])
    return comecam_com_x + comecam_sem_x

def solution_one(words):
    # +++ SUA SOLUÇÃO +++
    comecam_com_x = [w for w in words if w[0] == 'x']
    comecam_com_x.sort()
    comecam_sem_x = [w for w in words if w[0] != 'x']
    comecam_sem_x.sort()
    return comecam_com_x + comecam_sem_x

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_x, ['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x, ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
