# E001 — Initial Booking Flow

## Proveniência desejada
P1 — observado diretamente em execução preservada.

## Estado inicial
Repositório: juanthrasher/vibe-engineering-case-study
Branch de trabalho: episode/E001-initial-booking
Commit-base canônico: 5b8a1489e176a27359cead09d2bc7f16c1ff22ae
Estado do código: apenas README inicial; nenhuma aplicação implementada.

## Problema concreto
O prestador organiza horários por mensagens e anotações manuais. O objetivo é reduzir a coordenação repetitiva, permitindo publicar horários e receber reservas sem negociar cada opção por mensagem.

## Pergunta do episódio
Um agente consegue transformar o Estado Zero especificado em um primeiro sistema executável, testável e pequeno, sem adicionar funcionalidades que ainda não foram exigidas?

## Resultado desejado
Construir o primeiro estado executável com:
- um prestador;
- um serviço de duração fixa;
- publicação manual de horários;
- listagem pública de disponibilidade;
- reserva por cliente identificado por nome e contato;
- consulta de reservas pelo prestador.

## Critérios de aceitação
A1. O prestador consegue registrar um horário futuro disponível.
A2. Um horário registrado aparece na listagem pública.
A3. Um cliente consegue reservar um horário disponível informando nome e contato.
A4. Depois da reserva, o horário deixa de aparecer como disponível.
A5. A reserva aparece na consulta do prestador.
A6. Uma tentativa sequencial de reservar horário inexistente ou já indisponível não cria reserva válida.
A7. Os dados persistem após reiniciar o servidor enquanto o mesmo banco SQLite for preservado.
A8. Os testes automatizados centrais passam em ambiente limpo após migrations.

## Limite explícito de concorrência
E001 NÃO verifica duas solicitações simultâneas concorrendo pelo mesmo horário. Correção sob concorrência simultânea não pode ser inferida deste episódio.

## Restrições
Não implementar autenticação, cancelamento, pagamento, notificações, múltiplos prestadores, múltiplos serviços gerenciáveis, API pública, SPA, filas, Docker, PostgreSQL ou deploy de produção.
A interface deve ser server-rendered e funcionalmente mínima.

## Stack aprovada
Python 3.14.7.
Django 5.2.17.
SQLite.
Django templates.
django.test.TestCase.
venv + pip.

## Ambiente
Sistema operacional/ambiente de execução: A REGISTRAR no início da execução.
Arquivo de dependências exatas: A CRIAR antes da primeira mudança funcional.

## Autoridade inicial prevista
Leitura e escrita no repositório da branch do episódio.
Execução de comandos locais de desenvolvimento e testes.
Sem credenciais de produção.
Sem deploy.
Sem acesso a dados pessoais reais.
Sem necessidade de serviços externos.

## Verificação planejada
- suíte automatizada do Django cobrindo A1–A6;
- verificação de persistência para A7;
- execução em ambiente limpo/CI para A8 quando o primeiro estado estiver pronto;
- execução manual do fluxo prestador → cliente → prestador.

## Riscos conhecidos
- o agente pode adicionar funcionalidades além do escopo;
- pode confundir regra de indisponibilidade sequencial com garantia de concorrência;
- pode introduzir dependências desnecessárias;
- pode produzir testes que apenas confirmem sua própria implementação sem cobrir os critérios.

## O que este episódio poderá mostrar localmente
Como um primeiro sistema mínimo foi produzido sob esta especificação, quais decisões o agente tomou, quais verificadores detectaram sucesso ou falha e qual estado final foi aceito.

## O que este episódio NÃO permitirá concluir
Não permite concluir produtividade geral de IA, segurança de produção, correção sob concorrência, escalabilidade, manutenibilidade de longo prazo ou superioridade de Django/modelo/agente.

## Status
PRÉ-REGISTRADO. Nenhuma implementação funcional deve ocorrer antes do gate formal de execução ser liberado no Mapa Mestre.
