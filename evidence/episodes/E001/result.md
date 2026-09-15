# E001 — Result

## Proveniência
P1 — observado diretamente em execução preservada.

## Estado inicial canônico
Commit-base: `5b8a1489e176a27359cead09d2bc7f16c1ff22ae`.

## Pré-registro
Commit: `721f64e11e8e44fac263b78bd7bcf11bd96c90de`.

## Resultado primário funcional
Commit: `b9411a99a2518382709d517bab3b2f7474cc63c2`.

Entre o commit-base e o resultado primário foram produzidos o projeto Django, a aplicação `booking`, migrations, templates, CSS, sete testes automatizados, README, configuração de ambiente, pré-registro e o primeiro workflow de CI.

Comparação base → resultado primário:
- 28 commits à frente do estado inicial;
- 28 arquivos alterados/adicionados no comparador do GitHub;
- nenhuma correção funcional da aplicação foi necessária depois que o resultado primário entrou em verificação canônica.

## Comportamento implementado
- serviço inicial “Atendimento”, 60 minutos;
- cadastro de horário futuro pelo prestador;
- listagem pública de horários disponíveis;
- reserva com nome e contato;
- horário reservado deixa a listagem pública;
- consulta de reservas pelo prestador;
- tentativa sequencial de nova reserva em horário ocupado é rejeitada;
- tentativa de reservar ID inexistente retorna 404.

## Alterações após o resultado primário
Após `b9411a99...`, não houve alteração no código funcional da aplicação. Houve apenas fortalecimento dos verificadores no workflow:
- `468257f5467515b1b88cb1fba3f88a43e19054b5`: verificação de persistência SQLite entre processos;
- `8492ccce4456a29fdfa4b6aeabedd3117c9f8c4b`: smoke test HTTP com servidor real;
- `152a1a9bb40349f45ecb859c29e7edba685f3dca`: fluxo HTTP ponta a ponta via formulários reais.

## Observação central
O primeiro resultado funcional passou na primeira execução canônica do GitHub Actions. Este episódio, portanto, não é um caso de “agente falha e Engenharia de Software corrige”. Ele registra um caso em que escopo pequeno, critérios explícitos, stack integrada e verificadores definidos permitiram um primeiro resultado que satisfez os testes planejados sem correção funcional posterior.

Isso é observação local do E001, não evidência de que agentes em geral acertam de primeira.
