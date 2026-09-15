# vibe-engineering-case-study

Estudo de caso longitudinal do livro **Introdução à Vibe Engineering**.

## E001 — primeiro estado executável

Escopo inicial:

- um prestador;
- um serviço de duração fixa;
- cadastro manual de horários disponíveis;
- listagem pública de horários;
- reserva por nome e contato;
- consulta de reservas pelo prestador.

Autenticação, pagamentos, cancelamentos, múltiplos prestadores e concorrência simultânea estão fora do Estado Zero.

## Ambiente canônico do E001

- Python 3.14.7
- Django 5.2.17
- SQLite

## Execução local

```bash
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Prepare o banco:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Abra `http://127.0.0.1:8000/`.

## Testes

```bash
python manage.py test -v 2
```

## Evidências

O pré-registro e os artefatos do episódio ficam em:

```text
evidence/episodes/E001/
```

Os resultados deste caso são locais ao episódio e não constituem evidência geral sobre produtividade, segurança ou qualidade de agentes de IA.
