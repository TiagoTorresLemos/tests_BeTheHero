from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys
from time import sleep
from pprint import pprint

#Cenario 1

@when(u'o fundador escolhe a opção "Não tenho cadastro" pelo fato de não possuir ID')
def clickBtn_Registrar(context):
    registrar = context.browser.find_element_by_class_name("back-link")
    registrar.click()

@then(u'o fundador visualiza a tela de "Cadastro"')
def verificaTelaRegistro(context):
    cadastroText = context.browser.find_element_by_xpath("//h1[contains(.,'Cadastro')]").text
    assert cadastroText == "Cadastro"


#Cenario 2

@given(u'que acessa a tela de Cadastro de ONGs')
def acessaCadastroOng(context):
    registrar = context.browser.find_element_by_class_name("back-link")
    registrar.click()

@when(u'o fundador clica no botão "Cadastrar" sem preencher os campos')
def clickBtn_CadastrarOng(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then(u'o fundador visualizar a mensagem "Erro no cadastro, tente novamente."')
def verifica_ErroCadastro(context):
    sleep(1)
    msmAlert = context.browser.switch_to.alert
    msg = msmAlert.text
    assert msg == "Erro no cadastro, tente novamente."
    msmAlert.accept()

#Cenario 3

@given(u'que o fundador acessa a tela de Cadastro de ONGs')
def acessaCadastroOng(context):
    registrar = context.browser.find_element_by_class_name("back-link")
    registrar.click()

@then(u'o fundador visualizar o botão "Voltar para o logon"')
def verifica_btn_VoltarLogon(context):
    btn_voltarLogon = context.browser.find_element_by_xpath("//a[contains(text(),'Voltar para o logon')]")
    btn_voltarLogon.click()

# Cenario 4

@given(u'que o fundador está acessando a tela de Cadastro de ONGs')
def acessaCadastroOng(context):
    registrar = context.browser.find_element_by_class_name("back-link")
    registrar.click()


@when(u'o fundador cadastra uma ONG preenchendo os campos')
def preencheFormulario(context):
    nomeOng = context.browser.find_element_by_xpath("//input[@value='']")
    nomeOng.send_keys("Curando Vidas")

    sleep(2)
    email = context.browser.find_element_by_xpath("(//input[@value=''])[1]")
    email.send_keys("naodeveexistir@gmail.com")

    sleep(2)
    whatsaap = context.browser.find_element_by_css_selector("input:nth-child(3)")
    whatsaap.send_keys("20898141514")

    sleep(2)
    cidade = context.browser.find_element_by_xpath("//div[@id='root']/div/div/form/div/input")
    cidade.send_keys("Manaus")

    sleep(2)
    uf = context.browser.find_element_by_xpath("//div[@id='root']/div/div/form/div/input[2]")
    uf.send_keys("AM")

    btn_RegistraOng = context.browser.find_element_by_xpath("//button[@type='submit']")
    btn_RegistraOng.click()


@then(u'o fundador visualiza a mensagem que informa seu Id')
def visualizaId(context):
    sleep(6)
    msmAlertId = context.browser.switch_to.alert
    msgId = msmAlertId.text
    Id = msgId[17:]

    pprint(f' O Id gerado: {Id}')
    assert msgId[0:17] == "Seu ID de acesso:"
    msmAlertId.accept()
