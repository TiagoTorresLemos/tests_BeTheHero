from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys
from time import sleep


#Cenario 1
@given(u'que o fundador acesse a website Be The Hero "{link_web}"')
def acessaWeb(context, link_web):
    context.browser.get(link_web)

@then(u'a mensagem "Be The Hero" deverá estar no título')
def verificar_titulo(context):
    assert context.browser.title == "Be The Hero"

#Cenario 2
@when(u'o fundador tenta entrar sem informar o Id')
def clickBtnEntrar(context):
    btn_Entrar = context.browser.find_element_by_class_name("button")
    btn_Entrar.click()


@then(u'o fundador visualiza a mensagem "Falha no login, tente novamente."')
def verificarAlerta_Login(context):
    sleep(1)
    msmAlert = context.browser.switch_to.alert
    msg = msmAlert.text
    assert msg == "Falha no login, tente novamente."
    msmAlert.accept()

#Cenario 3
@given(u'que informa o Id "151617"')
def id_Invalido(context):
    idText = context.browser.find_element_by_xpath("//input[@value='']")
    idText.send_keys("151617")


@when(u'o fundador tenta entrar')
def click_Entrar(context):
    btn_Entrar = context.browser.find_element_by_class_name("button")
    btn_Entrar.click()

@then(u'a mensagem "Falha no login, tente novamente." é exibida')
def verificarLogin_Invaldo(context):
    sleep(1)
    msmAlert = context.browser.switch_to.alert
    msg = msmAlert.text
    assert msg == "Falha no login, tente novamente."
    msmAlert.accept()
