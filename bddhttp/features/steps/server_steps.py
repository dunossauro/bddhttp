from behave import step
from time import sleep
from bddhttp.auxiliar.elementos import Constantes
from bddhttp.auxiliar.auxiliar import read_config

constantes = Constantes()

dic = read_config(constantes.config)

@step('que o server seja iniciado')
def teste(context):
    context.browser.get(dic['ipv4'])
    context.browser.get(dic['ipv6'])
    context.browser.close()
