# Tic-em-Trilhas

Trilhas de exercícios de lógica e algoritmos em **Java** e **Python**, organizadas por nível (Trilha 01 a Trilha 05). É um repositório de estudo, não um aplicativo único.

## Conteúdo

O histórico publicado contém **71 arquivos**:

- `Dominando Algoritmos Com Java/Trilha 01` e `Trilha 02` — 20 exercícios Java.
- `Dominando Algoritmos com Python /Trilha 01` a `Trilha 05` — 49 arquivos Python e um arquivo `IMC` sem extensão.
- Este README.

Os exercícios abordam cálculo de médias, ingressos, boletim, FROM/condicionais, laços, fatorial, Fibonacci, tabuada, sistema bancário, controle de estoque, jogos e análise de faturamento, entre outros.

## Clonagem no Windows

O diretório chamado `Dominando Algoritmos com Python ` terminava com um **espaço**, o que impedia o checkout completo no Windows e falhava em `git archive`. Em 25/11/2026 ele foi renomeado para `Dominando Algoritmos com Python` em um commit normal, sem reescrita de histórico. Quem já tinha clonado deve atualizar o repositório ou fazer um clone novo para obter os caminhos corrigidos.

## Como executar

Com os arquivos disponíveis em disco:

```bash
# Java (um arquivo por vez)
javac -d saida BoletimAluno.java
java -cp saida BoletimAluno

# Python
py fatorial.py
```

Verificação realizada em 25/11/2026 sobre os arquivos extraídos do histórico: os exercícios Java compilaram com `javac` 27 e os Python passaram em `py_compile` com Python 3.14.7. Alguns arquivos Java usam `package Modúlo2;` e um deles usa `package TrilhasJava.Modúlo2;`; essa diferença é uma característica dos exercícios e não foi alterada.

## Tecnologias

Java e Python.
