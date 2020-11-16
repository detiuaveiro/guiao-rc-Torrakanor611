import pytest
from semantic_network import *

@pytest.fixture
def sn_net():

    a = Association('socrates','professor','filosofia')
    s = Subtype('homem','mamifero')
    m = Member('socrates','homem')

    da = Declaration('descartes',a)
    ds = Declaration('darwin',s)
    dm = Declaration('descartes',m)

    z = SemanticNetwork()
    z.insert(da)
    z.insert(ds)
    z.insert(dm)
    z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
    z.insert(Declaration('darwin',Association('homem','gosta','carne')))

    # novas declaracoes

    z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
    z.insert(Declaration('descartes', Member('aristoteles','homem')))

    b = Association('socrates','professor','matematica')
    z.insert(Declaration('descartes',b))
    z.insert(Declaration('simao',b))
    z.insert(Declaration('simoes',b))

    z.insert(Declaration('descartes', Member('platao','homem')))

    e = Association('platao','professor','filosofia')
    z.insert(Declaration('descartes',e))
    z.insert(Declaration('simao',e))

    z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
    z.insert(Declaration('descartes',Association('homem','altura',1.75)))
    z.insert(Declaration('simao',Association('homem','altura',1.85)))
    z.insert(Declaration('darwin',Association('homem','altura',1.75)))

    z.insert(Declaration('descartes', Association('socrates','peso',80)))
    z.insert(Declaration('darwin', Association('socrates','peso',75)))
    z.insert(Declaration('darwin', Association('platao','peso',75)))


    z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
    z.insert(Declaration('damasio', Member('socrates','filosofo')))

    return z

def test_exercicio10(sn_net):
    assert sn_net.predecessor_path('vertebrado','socrates') == ['vertebrado', 'mamifero', 'homem', 'socrates']

def test_exercicio11(sn_net):
    assert str(sn_net.query('socrates','altura')) == "[decl(descartes,altura(mamifero,1.2)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75))]"

    assert str(sn_net.query('platao')) == "[decl(darwin,mamar(mamifero,sim)), decl(descartes,altura(mamifero,1.2)), decl(darwin,gosta(homem,carne)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75)), decl(descartes,professor(platao,filosofia)), decl(simao,professor(platao,filosofia)), decl(darwin,peso(platao,75))]"

    assert str(sn_net.query2('platao')) == "[decl(darwin,mamar(mamifero,sim)), decl(descartes,altura(mamifero,1.2)), decl(darwin,gosta(homem,carne)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75)), decl(descartes,professor(platao,filosofia)), decl(simao,professor(platao,filosofia)), decl(darwin,peso(platao,75)), decl(descartes,member(platao,homem))]"


def test_exercicio12(sn_net):
    assert str(sn_net.query_cancel('socrates')) == "[decl(darwin,mamar(mamifero,sim)), decl(darwin,gosta(homem,carne)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75)), decl(damasio,gosta(filosofo,filosofia)), decl(descartes,professor(socrates,filosofia)), decl(descartes,professor(socrates,matematica)), decl(simao,professor(socrates,matematica)), decl(simoes,professor(socrates,matematica)), decl(descartes,peso(socrates,80)), decl(darwin,peso(socrates,75))]"

def test_exercicio13(sn_net):
    assert str(sn_net.query_down('vertebrado', 'altura')) == "[decl(descartes,altura(mamifero,1.2)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75)), decl(descartes,altura(mamifero,1.2)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75)), decl(descartes,altura(mamifero,1.2)), decl(descartes,altura(homem,1.75)), decl(simao,altura(homem,1.85)), decl(darwin,altura(homem,1.75))]"