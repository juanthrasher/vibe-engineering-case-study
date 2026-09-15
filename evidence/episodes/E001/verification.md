# E001 — Verification

## Ambiente canônico
GitHub Actions, `ubuntu-latest`.
Python 3.14.7.
Django 5.2.17.
SQLite.

## Run 1 — resultado primário
Run: https://github.com/juanthrasher/vibe-engineering-case-study/actions/runs/34914593898
Head SHA: `b9411a99a2518382709d517bab3b2f7474cc63c2`
Conclusão: **success**.

Verificações observadas:
- instalação de Django 5.2.17;
- Python 3.14.7 no runner;
- `python manage.py check`: sem problemas;
- migrations 0001 e 0002: OK;
- sete testes descobertos;
- sete testes passaram;
- nenhuma falha funcional observada pelos verificadores desse run.

Cobertura principal:
- A1 publicação de horário;
- A2 listagem pública;
- A3 criação de reserva;
- A4 remoção da disponibilidade;
- A5 consulta do prestador;
- A6 rejeição sequencial de horário ocupado/inexistente;
- A8 testes em ambiente limpo.

## Run 2 — persistência
Run: https://github.com/juanthrasher/vibe-engineering-case-study/actions/runs/34914665329
Head SHA: `468257f5467515b1b88cb1fba3f88a43e19054b5`
Conclusão: **success**.

O workflow gravou uma reserva no SQLite em um processo Python e, em um novo processo, leu a mesma reserva com sucesso.

Cobertura adicional:
- A7 persistência entre processos usando o mesmo arquivo SQLite.

## Run 3 — smoke HTTP
Run: https://github.com/juanthrasher/vibe-engineering-case-study/actions/runs/34914717714
Head SHA: `8492ccce4456a29fdfa4b6aeabedd3117c9f8c4b`
Conclusão: **success**.

O runner iniciou o `runserver`, fez requisição HTTP real à página inicial e encontrou a resposta esperada.

## Run 4 — fluxo HTTP ponta a ponta
Run: https://github.com/juanthrasher/vibe-engineering-case-study/actions/runs/34914843321
Head SHA: `152a1a9bb40349f45ecb859c29e7edba685f3dca`
Conclusão: **success**.

O workflow:
1. iniciou o servidor Django;
2. abriu o formulário do prestador e obteve token CSRF;
3. cadastrou um horário por POST HTTP;
4. verificou o horário na listagem pública;
5. abriu o formulário de reserva;
6. criou uma reserva por POST HTTP;
7. verificou nome e contato na visão do prestador;
8. confirmou que o horário reservado deixou a listagem pública;
9. executou novamente a suíte de sete testes.

## Independência dos verificadores
- testes Django e constraints: I3 em relação à geração textual do código;
- GitHub Actions em ambiente limpo: I3 como executor externo determinístico do workflow;
- fluxo HTTP automatizado: I3 para o comportamento específico testado.

A classificação I3 não significa cobertura completa do sistema.

## Limitações
- nenhuma verificação de concorrência simultânea foi executada;
- nenhuma auditoria de segurança de produção foi executada;
- autenticação e autorização não existem no Estado Zero;
- não houve teste manual em navegador por uma pessoa; o requisito operacional foi coberto por fluxo HTTP automatizado no servidor real do runner;
- não há teste multi-OS;
- não há teste de carga;
- não há análise de acessibilidade;
- não há análise estática ou type checking adicional nesta fase.

## Resultado
Todos os critérios A1–A8 possuem evidência compatível com seu escopo, com a ressalva explícita de que A6 é apenas sequencial.
