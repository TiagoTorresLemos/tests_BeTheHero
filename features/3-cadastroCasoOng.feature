# language: pt

@casoOng
Funcionalidade: Cadastro de casos de ONG
  Eu enquanto Fundador,
  gostaria de cadastrar Casos de ONG,
  para que outras pessoas possam visualizar e realizar contatos

  Contexto: Acessar a WebSite para Realizar Login
    Dado que o fundador acesse a WebSite Be The Hero "http://localhost:3000/" para realizar login
    Quando realiza o login na website
    Então a mensagem "Bem vinda, Curando Vidas" é exibida na home

  Cenário: Verificar a possibilidade de retornar para tela de home
    Dado que o fundador acesse a tela de cadastro de casos de ONG
    Então o fundador visualiza a opção "Voltar para home"

  Cenário: Cadastrar um caso de ONG com sucesso
    Dado que esteja na tela de cadastro de casos de ONG
    Quando o fundador cadastra um caso de ONG, preenchendo todos os campos
    Então o fundador visualiza o caso criado na tela de home

  Cenário: Excluir um caso de ONG
    Dado que já exista um caso de ONG exibido na tela de home
    Quando o fundador exclui o caso de ONG
    Então o caso de ONG foi removido com sucesso

  Cenário: Cadastrar um caso de ONG sem preencher os campos
    Dado que o fundador esteja na tela de cadastro de casos de ONG
    Quando o fundador tenta cadastrar um caso sem preencher os campos
    Então o fundador visualiza a mensagem "Erro no cadastro, tente novamente."
