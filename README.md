Este repositório é sobre o exercício de IA da professora Érica, realizado em grupo.

Esse é apenas o código, e a documentação do projeto é um arquivo .docs, que até o momento não estará presente no repositório.

Observação: Para fins didáticos e do meu aprendizado, esse projeto possuirá um requirements.txt, porém para rodar o projeto é necessário possuir uma interface TKINTER instalada na sua instalação do python3.

Anteriormente, eu pretendia forçar o programa a rodar em um modo não interativo, para que não fosse necessário possuir uma instalação python-tk no sistema, ou seja, o programa ao invés de abrir automaticamente os gráficos gerados, salvariam os arquivos dentro da pasta. 
Porém, isso deixaria o programa menos atual, além de ter a necessidade de abrir os arquivos que seriam gerados manualmente um por um.

Lembrando que as instruções são para rodar o código em um ambiente virtual venv.

## Preparação do ambiente:

```bash
sudo apt install python3-tk
python3 -m venv .venv
source .venv/bin/activate
```

## Instalando as dependências e rodando o programa:

```bash
pip install -r requirements.txt

python3 ex4.py
```