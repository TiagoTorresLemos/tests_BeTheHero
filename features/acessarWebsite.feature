# language: pt

Funcionalidade: Eu enquanto usuário, gostaria de acessar a website Be The Hero, para conectar minha ONG a internet

  Cenário: Acessar Website
    Dado que o usuário acesse a Website Be The Hero "http://localhost:3000/"
    Então a mensagem "Be the Hero" deverá estar no título
