# data-quality

Este projeto tem o propósito de apresentar alguns padrões de um projeto para criação de pacotes python.

### Informações gerais:
- assets : Arquivos de configuração 
- dataset : Base de dados de exemplo
- quality : Fontes do pacote
- tests : Exemplo de teste unitário

O repositório possui a seguinte estrutura:

```
├───assets
    └───configs.json
    └───metadado.xlsx
├───dataset
    └───house_price.csv
    └───logs.log
└───src
    └───app.py
    └───prepare.py
    └───validator.py
└───tests
    └───quality_test.py
└───Makefile
└───requirements.txt
└───pyproject.toml
└───tox.ini
└───README.md
└───.gitignore
```

### Como utilizar:

1. Crie um ambiente virtual
```
python -m venv env
```
2. Ative o ambiente virtual
3. Instale o requirements
```
pip install -r requirements.txt
```
4. Execute o make para o processo completo
```
python quality/app.py
```
5. Execute o make para aplicar os testes
```
make all
```
7. para executar o tox
```
python -m tox
```
6. para criar o pacote
```
python -m build
pip install dist/quality-0.0.1-py3-none-any.whl
``` 