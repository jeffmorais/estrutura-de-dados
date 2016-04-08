import unittest


def _quick_recursivo(seq, inicio, final):
    if inicio >= final:
        return seq
    indice_pivot = final
    pivot = seq[indice_pivot]
    i_esquerda = inicio
    i_direita = final - 1

    while i_esquerda<=i_direita:
        while i_esquerda<=i_direita and seq[i_esquerda]<=pivot:
            i_esquerda=i_esquerda+1
        while i_esquerda<=i_direita and seq[i_direita]>=pivot:
            i_direita=i_direita-1
        if i_esquerda<i_direita:
            aux=seq[i_esquerda]
            seq[i_esquerda]=seq[i_direita]
            seq[i_direita]=aux
    aux=seq[i_esquerda]
    seq[i_esquerda]=seq[final]
    seq[final]=aux
    _quick_recursivo(seq, inicio, i_esquerda - 1)
    _quick_recursivo(seq, i_esquerda + 1, final)
    

    return seq

def quick_sort(seq):
    return _quick_recursivo(seq, 0, len(seq) - 1)


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_com_elementos_repetidos(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0, 9, 9]))

    def teste_lista_so_com_elementos_repetidos(self):
        self.assertListEqual([9, 9, 9], quick_sort([9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
