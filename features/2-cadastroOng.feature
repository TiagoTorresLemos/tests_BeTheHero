# language: pt
@cadastroOng

  Funcionalidade: Cadastro ONG
    Eu enquanto Fundador,
    gostaria de cadastrar uma ONG,
    para criar os casos de ONG e disponibilizar para as pessoas

    Contexto: Acessar a WebSite
      Dado que o fundador acesse a WebSite Be The Hero "http://localhost:3000/"

    Cenário: Acessar a tela de cadastro de ONGs
      Quando o fundador escolhe a opção "Não tenho cadastro" pelo fato de não possuir ID
      Então o fundador visualiza a tela de "Cadastro"

    Cenário: Cadastrar uma ONG sem preencher os campos
    	Dado que acessa a tela de Cadastro de ONGs
    	Quando o fundador clica no botão "Cadastrar" sem preencher os campos
    	Então o fundador visualizar a mensagem "Erro no cadastro, tente novamente."

    Cenário: Verificar a possibilidade de retornar para tela de log in
    	Dado que o fundador acessa a tela de Cadastro de ONGs
    	Então o fundador visualizar o botão "Voltar para o logon"

    Cenário: Cadastrar uma ONG com sucesso
    	Dado que o fundador está acessando a tela de Cadastro de ONGs
    	Quando o fundador cadastra uma ONG preenchendo os campos
    	Então o fundador visualiza a mensagem que informa seu Id
