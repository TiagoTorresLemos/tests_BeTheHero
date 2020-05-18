# tests_BeTheHero
Projeto de testes com intuito de aprendizado.

Este Projeto de testes é apenas para fim de estudo e aprendizado, segue as configurações:

	Os testes serão realizados no Projeto Be The Hero (indico utilizar do mesmo repositório informado abaixo).
	Os testes serão realizados somente no ambiente web.
	Sistema Operacional: Windows 10.




Para realizar este Projeto de testes foi utilizado o Projeto Be The Hero, segue algumas informações a respeito:

	O Be The Hero é um projeto voltado para conectar ONGS.
	Foi desenvolvido durante a Semana OmniStack 11.0, um evento da @Rocketsea.
	Utilizei o Projeto Be The Hero, neste repositório do github: "EliasMelo1/be-te-hero".


Para rodar os testes será necessário baixar o projeto Be The Hero.

	1 - Baixar o projeto (não necessariamente precisa fazer o clone, pode baixar o zip).
	2 - Após baixar o projeto, extrair do Zip para um local, por exemplo "C:\PROJETO-AUTOMACAO".
	3 - Após extrair, notará que existe 3 pastas: "BackEnd, FrontEnd e Mobile".
	Como o intuito do estudo é realizar os testes no ambiente web, a pasta "Mobile" poderá ser apagada.
	4 - Com o CMD (Administrador) navegar até a pasta BackEnd:
		- Dentro da pasta BackEnd digitar o comando "npm install"
		- Após o primeiro comando ter terminado, executar "npm start"
	5 - Abrir um novo CMD (Administrador), e navegar até a pasta FrontEnd:
		- Dentro da pasta BackEnd digitar o comando "npm install"
		- Após o primeiro comando ter terminado, executar "npm start"
	6 - Depois que os comandos foram exutados o Projeto Be The Hero será iniciado localmente no navegador.

O Projeto Be The Hero, já está pronto para realizar os testes.

 # Configuração e passos para executar os testes

 Configurações utilizadas:

	Sistema Operacional: Windows 10
	Editor: Atom (https://atom.io/)
	Terminal utilizado no Atom (platformio-ide-terminal)
	Liguagem utilizada: Python 3 (https://www.python.org/downloads/)
	Ferramenta para automação: Selenium/Selenium webdriver
	Utilizado BDD: Behave (https://behave.readthedocs.io/en/latest/index.html)
	Navegador utilizado: Firefox, no caso precisa ter o GeckoDriver instalado na máquina




1. Criar a pasta do Projeto
2. Navegar para dentro da pasta criada (Projeto)
3. Criar um ambiente virtual (para rodar o selenium isolado da máquina) - Virtual Env (venv)

	- Código para criar o ambiente
	  python -m venv venv

	Obs: A criação desse ambiente virtual pode ser realizado de duas formas:
	1 - Pelo terminal do windows (cmd, no modo administrador)

	2 - Pelo próprio terminal do Atom (este precisa configurar o terminal do Atom para que abra sempre com o cmd e não o powershell)

	Passos para configurar o CMD para que sempre execute no modo administrador:
	1 - Digitar no menu iniciar do windows "cmd"
	2 - Clicar na opção "abrir local do arquivo"
	3 - Clicar com botão direito sobre o icone do CMD/Prompt de Comando
	4 - Selecionar a opção "Propriedades"
	5 - Clicar na opção "Avançadas"
	6 - Marcar o check na opção "Executar como administrador"

	Estes passos irão garantir que sempre que o CMD for iniciado, será sempre como modo administrador.


4. Ativar o ambiente virtual para poder instalar o selenium

	- Código
	  venv\Scripts\activate.bat
	  (Para desativar o ambiente virtual: venv\Scripts\deactivate)

5. Com ambiente virutal ativado, instalar o Selenium

	- Código
	  pip install selenium

6. Instalar o Behave
	- Código
		pip install behave

7. Estrutura do behave pode ser verificada no site: https://behave.readthedocs.io/en/latest/gherkin.html
	- Necessário seguir o padrão da estrutura informada.

8. Para executar um teste com o behave, lembrando que ainda está dentro da venv ativada, basta digitar "behave"
