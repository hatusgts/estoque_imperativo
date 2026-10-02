# Controle de Estoque

Sistema simples de controle de estoque em Python, via terminal (menu interativo).

## Pré-requisitos

- Python 3 instalado (não usa nenhuma biblioteca externa, só a biblioteca padrão).

## Como executar

1. Entre na pasta do projeto.
2. Rode o comando:

```
python3 main.py
```

3. Use o menu numérico que aparece para cadastrar produtos, consultar, registrar entrada/saída de estoque e listar produtos (incluindo os que estão em nível crítico).
4. Para sair, escolha a opção 0.

## Estrutura dos arquivos

- `main.py`: menu e interação com o usuário.
- `operacoes.py`: funções que fazem as operações no estoque (cadastrar, consultar, entrada, saída, listar).
- `dados.py`: guarda o estoque (dicionário com os produtos).
- `validacoes.py`: funções de validação usadas pelas operações.

## Atualizando este README

Sempre que o escopo do projeto mudar (nova funcionalidade, novo arquivo, nova dependência, mudança na forma de executar), atualize este README junto com o código, na mesma alteração/commit. O objetivo é que ele nunca fique desatualizado em relação ao que o código realmente faz.
