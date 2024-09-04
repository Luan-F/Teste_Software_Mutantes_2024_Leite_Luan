# Projeto base
- https://github.com/inducer/pudb

---

# Tutorial - cal (1  e 2)
## Etapa 1 - Configurando ambiente
1. Baixar e acessar o repositório
	- `git clone https://github.com/stevaoaa/cal_python`
	- `cd cal_python`
1. Testando aplicação
	- `python cal.py`
2. Configurar ambiente virtual
	1. Instalando `python3-venv`
		- Ubuntu: `sudo apt install python3-venv`
		- Arch/Manjaro: `sudo pacman -S python3-venv`
	2. Criando pasta `venv`
		- `python -m venv venv`
3. Instalando dependências
	1. Acessando ambiente virtual
		- `source venv/bin/activate`
	2. Instalando `pylint`
		- `pip install -U pylint`
	3. Instalando dependências do projeto
		- `pip install -r requirements.txt`
## Etapa 2 - Executando testes
1. Executando testes unitários
	- `pytest -vv test_cal.py`
2. Verificando e analisando cobertura dos testes
	1. Rodando testes de cobertura
		- `pytest -vv test_cal.py -cov=cal`
	2. Gerando relatório em HTML da cobertura dos testes
		- `pytest -vv test_cal.py --cov=cal --cov-branch --cov-report html `
	- Com o relatório é possível perceber que os testes não cobrem a função `main`, apenas as funções implementadas.
## Etapa 3 - Executando testes de mutação `mutmut`
1. Executando testes de mutação
	- `mutmut run paths-to-mutate=cal.py`
2. Analisando mutantes que sobreviveram
	- Gerando relatório em html
		- `mutmut html`
	- Selecionando mutante que sobreviveu, com base no relatório.
		- Mutante 27 selecionado

       ![Pasted image 20240903215542](https://github.com/user-attachments/assets/e19b1369-1d42-441d-a30f-88d863bad076)


3. Adicionando o caso de teste `test_first_of_month_mutant`
# Tutorial - pudb (3 e 4)
## Etapa 1 - Configurando ambiente
1. Baixar e acessar o repositório
	- `git clone https://github.com/inducer/pudb.git`
	- `cd pudb`
2. Configurar ambiente virtual
	1. Criando pasta `venv`
		- `python -m venv venv`
3. Instalando dependências
	1. Acessando ambiente virtual
		- `source venv/bin/activate`
	2. Instalando dependências do projeto
		- `pip install -r requirements.dev.txt`
	3. Instalando `mutmut`
		- `pip install mutmut`
## Etapa 2 - Executando e analisando testes
1. Executando os testes unitários
	- `pytest -vv`

     ![Pasted image 20240903174149](https://github.com/user-attachments/assets/60aaa273-f03d-4231-9637-9422ac46972e)

2. Verificando cobertura do código
	- `pytest -vv --cov=pudb --cov-branch --cov-report html`

     ![Pasted image 20240903174335](https://github.com/user-attachments/assets/df6db6d9-3a63-4fdb-90af-6cf60e790f6b)

	- Analisando cobertura de código (`chromium coverage_html_report/index.html`)

    ![Pasted image 20240903175133](https://github.com/user-attachments/assets/3f353d17-601c-4500-88a5-8478a0bb2539)

	  - Podemos perceber que há uma baixa cobertura de código no projeto.
## Etapa 3 - Executando testes de mutação
1. Acessando pasta `pudb`
	- `cd pudb`
2. Executando teste de mutação
	- `mutmut run --paths-to-mutate=.`

    ![Pasted image 20240903175757](https://github.com/user-attachments/assets/cdfe470f-e051-448c-96e2-b1412713d45f)

	- Observação:
		- Como o projeto não tem uma ampla cobertura de testes, boa parte dos módulos mutados nem serão executados. Por isso a quantidade de mutantes que sobreviveram é elevada.
3. Analisando e gerando relatório de mutação
	1. Gerando relatório
		- `mutmut html`
	2. Analisando o relatório

  ![Pasted image 20240903185319](https://github.com/user-attachments/assets/435580b6-5408-43f5-8405-b3c06bd00798)

  - Com isso, podemos perceber que boa parte dos mutantes que foram mortos fazem parte do código de teste ou possuem uma quantidade de testes maior comparada aos outros módulos.
## Etapa 4 - Melhorando testes
- Nesta etapa iremos adicionar alguns testes para aumentar a cobertura de código e matar possíveis mutantes.
1. Escolhendo módulo
	- O `pubd/debugger.py` foi escolhido por ter uma baixa cobertura de código (8%) e alta quantidade de mutantes vivos (1823).
	- O foco principal será na classe `Debugger`.
2. Melhorando testes
	- Para melhorar a cobertura e qualidade dos testes referentes ao `debugger.py`, foi utilizado o relatório do `mutmut` como base para criação dos casos de teste.
	- Com isso, os seguintes testes:
		- `test_singleton_constructor`
		- `test_continue_at_start`
		- `test_ui_should_not_be_none`
		- `test_steal_output`
3. Analisando melhoria
	- Os testes implementados aumentaram a cobertura de código do módulo `debugger.py` de 8% para 23%.
		- Antes
    - ![Pasted image 20240903213417](https://github.com/user-attachments/assets/9bb8e9b2-e12f-43d5-b215-67411cf2aa6e)

    - Depois
    - ![Pasted image 20240903213435](https://github.com/user-attachments/assets/5b9ac6a7-7d53-476f-8d22-4ac5da710a41)
