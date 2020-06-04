from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys
from time import sleep
from pprint import pprint


#contexto 1
@given(u'que o fundador acesse a WebSite Be The Hero "{link_login}" para realizar login')
def acessarLogin(context, link_login):
    context.browser.get(link_login)

@when(u'realiza o login na website')
def realizaLogin(context):
    campoID = context.browser.find_element_by_xpath("//div[@id='root']/div/section/form/input")
    campoID.send_keys("bc737207")

    btnEntrar_Login = context.browser.find_element_by_xpath("//button[@type='submit']")
    btnEntrar_Login.click()

@then(u'a mensagem "Bem vinda, Curando Vidas" é exibida na home')
def verificaMsmHome(context):
    textoHome = context.browser.find_element_by_xpath("//div[@id='root']/div/header/span")
    assert textoHome.text == "Bem vinda, Curando Vidas"

#cenario 1
@given(u'que o fundador acesse a tela de cadastro de casos de ONG')
def acessaTelaCasoOng(context):
    btnCasoOng = context.browser.find_element_by_xpath("//a[contains(text(),'Cadastrar novo caso')]")
    btnCasoOng.click()

@then(u'o fundador visualiza a opção "Voltar para home"')
def verificaVoltarHome(context):
    link_home = context.browser.find_element_by_xpath("//div[@id='root']/div/div/section/a").text
    assert link_home == "Voltar para home"


#cenario 2
@given(u'que esteja na tela de cadastro de casos de ONG')
def acessaCasoOng(context):
    btnCasoOng = context.browser.find_element_by_xpath("//a[contains(text(),'Cadastrar novo caso')]")
    btnCasoOng.click()

@when(u'o fundador cadastra um caso de ONG, preenchendo todos os campos')
def preencheFormCaso(context):
    campoTitulo = context.browser.find_element_by_xpath("//div[@id='root']/div/div/form/input")
    campoTitulo.send_keys("Alimentos")

    campoDesc = context.browser.find_element_by_xpath("//div[@id='root']/div/div/form/textarea")
    campoDesc.send_keys("Entrega de alimentos + valores financeiro deverão ocorrer no dia 15/06/2020, no CSU - Parque 10")

    campoValor = context.browser.find_element_by_xpath("//div[@id='root']/div/div/form/input[2]")
    campoValor.send_keys("50")

    btnCadastroCaso = context.browser.find_element_by_xpath("//button[@type='submit']")
    btnCadastroCaso.click()


@then(u'o fundador visualiza o caso criado na tela de home')
def confirmaCasoCriado(context):
    sleep(0.5)
    confirmaTitulo = context.browser.find_element_by_xpath("//*[@id='root']/div/ul/li/p[1]").text
    assert confirmaTitulo == "Alimentos"

    sleep(0.5)
    confirmaDesc = context.browser.find_element_by_xpath("//*[@id='root']/div/ul/li/p[2]").text
    assert confirmaDesc == "Entrega de alimentos + valores financeiro deverão ocorrer no dia 15/06/2020, no CSU - Parque 10"

    sleep(0.5)
    confirmaValor = context.browser.find_element_by_xpath("//*[@id='root']/div/ul/li/p[3]").text
    assert confirmaValor == "R$ 50,00"


#cenario 3
@given(u'que já exista um caso de ONG exibido na tela de home')
def verfificaCasoCriado(context):
    confirmaTitulo = context.browser.find_element_by_xpath("//*[@id='root']/div/ul/li/p[1]").text
    assert confirmaTitulo == "Alimentos"


@when(u'o fundador exclui o caso de ONG')
def removeCaso(context):
    casoCriadoRemover = context.browser.find_element_by_xpath("//*[@id='root']/div/ul/li/button")
    casoCriadoRemover.click()


@then(u'o caso de ONG foi removido com sucesso')
def verificaRemovidoCaso(context):
    existe = context.browser.find_element_by_xpath("//*[@id='root']/div").text
    if existe[63:67] != "CASO":
        return print(f'Caso removido')



#cenario 4
@given(u'que o fundador esteja na tela de cadastro de casos de ONG')
def acessaCadastroCasoOng(context):
    btnCasoOng = context.browser.find_element_by_xpath("//a[contains(text(),'Cadastrar novo caso')]")
    btnCasoOng.click()

@when(u'o fundador tenta cadastrar um caso sem preencher os campos')
def clickCadastrarCaso(context):
    btnCadastroCaso = context.browser.find_element_by_xpath("//button[@type='submit']")
    btnCadastroCaso.click()

@then(u'o fundador visualiza a mensagem "Erro no cadastro, tente novamente."')
def verifica_ErroCadastroCaso(context):
    msmAlert = context.browser.switch_to.alert
    msg = msmAlert.text
    assert msg == "Erro no cadastro, tente novamente."
    msmAlert.accept()
