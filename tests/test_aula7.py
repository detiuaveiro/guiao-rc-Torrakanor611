import pytest
from semantic_network import *
from tests.test_aula6 import sn_net

def compare_decl_lists(l1,l2):
    l1_tuples = [str(d) for d in l1]
    l2_tuples = [str(d) for d in l2]
    return set(l1_tuples)==set(l2_tuples)

def test_exercicio10(sn_net):
    assert sn_net.predecessor_path('vertebrado','socrates') == ['vertebrado', 'mamifero', 'homem', 'socrates']

def test_exercicio11(sn_net):
    assert compare_decl_lists(sn_net.query('socrates','altura'),[
Declaration('descartes',Association('mamifero','altura',1.2)), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75))] )

    assert compare_decl_lists(sn_net.query('platao'), [
Declaration('darwin',Association('mamifero','mamar','sim')), \
Declaration('descartes',Association('mamifero','altura',1.2)), \
Declaration('darwin',Association('homem','gosta','carne')), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75)), \
Declaration('descartes',Association('platao','professor','filosofia')), \
Declaration('simao',Association('platao','professor','filosofia')), \
Declaration('darwin',Association('platao','peso',75))] )

    assert compare_decl_lists(sn_net.query2('platao'), [
Declaration('darwin',Association('mamifero','mamar','sim')), \
Declaration('descartes',Association('mamifero','altura',1.2)), \
Declaration('darwin',Association('homem','gosta','carne')), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75)), \
Declaration('descartes',Association('platao','professor','filosofia')), \
Declaration('simao',Association('platao','professor','filosofia')), \
Declaration('darwin',Association('platao','peso',75)), \
Declaration('descartes',Member('platao','homem'))] )


def test_exercicio12(sn_net):
    assert compare_decl_lists(sn_net.query_cancel('socrates'), [
Declaration('darwin',Association('mamifero','mamar','sim')), \
Declaration('darwin',Association('homem','gosta','carne')), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75)), \
Declaration('damasio',Association('filosofo','gosta','filosofia')), \
Declaration('descartes',Association('socrates','professor','filosofia')), \
Declaration('descartes',Association('socrates','professor','matematica')), \
Declaration('simao',Association('socrates','professor','matematica')), \
Declaration('simoes',Association('socrates','professor','matematica')), \
Declaration('descartes',Association('socrates','peso',80)), \
Declaration('darwin',Association('socrates','peso',75))] )

def test_exercicio13(sn_net):
    assert compare_decl_lists(sn_net.query_down('vertebrado', 'altura'), [
Declaration('descartes',Association('mamifero','altura',1.2)), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75)), \
Declaration('descartes',Association('mamifero','altura',1.2)), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75)), \
Declaration('descartes',Association('mamifero','altura',1.2)), \
Declaration('descartes',Association('homem','altura',1.75)), \
Declaration('simao',Association('homem','altura',1.85)), \
Declaration('darwin',Association('homem','altura',1.75))] )



