	# language: pt

	Funcionalidade: Log in
		Eu enquanto Fundador,
		gostaria de acessar a website Be The Hero,
		para realizar o log in no sistema.

		Contexto: Acessar a WebSite
		 	Dado que o fundador acesse a website Be The Hero "http://localhost:3000/"

	  Cenário: Verificar disponibilidade do WebSite Be The Hero
	    Então a mensagem "Be the Hero" deverá estar no título

		Cenário: Realizar log in sem informar Id
		 	Quando o fundador tenta entrar sem informar o Id
		 	Então o fundador visualiza a mensagem "Falha no login, tente novamente."

		Cenário: Realizar log in com Id inválido
	  	E informa o Id "151617"
	  	Quando o fundador tenta entrar
	  	Então a mensagem "Falha no login, tente novamente." é exibida
