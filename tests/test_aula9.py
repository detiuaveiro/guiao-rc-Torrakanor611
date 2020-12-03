
import pytest
from bayes_net import *

@pytest.fixture
def bn():
    """ 
    #https://dreampuf.github.io/GraphvizOnline/

    digraph G {
    node [shape=record];
    "sc" [label="Sobre Carregado\n|0.6"];
    "pt" [label="Processador Texto\n|0.05"];
    "cp" [label="Cara Preocupada\n|{{~sc^~pa = 0.01}|{~sc^pa = 0.011}|{sc^~pa = 0.01}|{sc^pa = 0.02}}"];
    "fr" [label="Frequência Rato\n|{{~pt^~pa=0.01}|{~pt^pa=0.10}|{pt^~pa=0.90}|{pt^pa=0.90}}"];
    "pa" [label="Precisa Ajuda\n|{{~pt = 0.004}|{pt = 0.25}}"];
    "cnl" [label="Correio Não Lido\n|{{sc = 0.90}|{~sc = 0.001}}"];

    "pt" -> "fr";
    "pa" -> "fr";
    "pt" -> "pa";
    "pa" -> "cp";
    "sc" -> "cnl";
    "sc" -> "cp";
    } 
    """

    bn = BayesNet()

    bn.add('sc',[],0.6)
    bn.add('pt',[],0.05)

    bn.add('cp',[('sc',True ),('pa',True )],0.02)
    bn.add('cp',[('sc',True ),('pa',False)],0.01)
    bn.add('cp',[('sc',False),('pa',True )],0.011)
    bn.add('cp',[('sc',False),('pa',False)],0.001)

    bn.add('fr',[('pt',True ),('pa',True )],0.90)
    bn.add('fr',[('pt',True ),('pa',False)],0.90)
    bn.add('fr',[('pt',False),('pa',True )],0.10)
    bn.add('fr',[('pt',False),('pa',False)],0.01)

    bn.add('pa',[('pt',True )],0.25)
    bn.add('pa',[('pt',False)],0.004)

    bn.add('cnl',[('sc',True )],0.90)
    bn.add('cnl',[('sc',False)],0.001)

    return bn

def test_exercicio15(bn):
    assert round(bn.individualProb('pa', True),5) == 0.0163

