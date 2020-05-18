from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys


@given(u'que o usuário acesse a Website Be The Hero "{link_web}"')
def acessaWeb(context, link_web):
    context.browser.get(link_web)



@then(u'a mensagem "{msm}" deverá estar no título')
def verificar_titulo(context, msm):
    assert context.browser.title == msm
