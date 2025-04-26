# Nome que aparece na lista de workflows
name: Generate Snake Animation

# Eventos que disparam a Action
on:
  # Dispara a Action automaticamente todo dia à meia-noite UTC
  schedule:
    - cron: "0 0 * * *"
  # Permite rodar a Action manualmente pela aba "Actions"
  workflow_dispatch:

# Definição dos jobs (tarefas)
jobs:
  # Nome do job (mantendo "build" já que apareceu nos seus logs)
  build:
    # Ambiente de execução
    runs-on: ubuntu-latest
    # Permissões para escrever no repositório (necessário para o commit)
    permissions:
      contents: write

    # Passos do job
    steps:
      # Passo 1: Faz o checkout do código do seu repositório
      - name: Checkout code
        uses: actions/checkout@v4

      # Passo 2: Gera o arquivo da animação da cobrinha
      # O "name" abaixo aparecerá nos logs dessa etapa
      - name: Generate snake file
        # Usa a Action específica que cria a animação
        uses: PlatypusBuilder/github-contribution-grid-snake@v2.2.1
        with:
          # >>> SEU NOME DE USUÁRIO DO GITHUB - MUITO IMPORTANTE! <<<
          github_user_name: Pedrinscrk
          # Formatos de saída da animação (SVG é bom para README)
          outputs: |
            github-contribution-grid-snake.svg  # Arquivo SVG para o README
            github-contribution-grid-snake.gif  # Opcional: arquivo GIF
            github-contribution-grid-snake.svg.dark # Opcional: versão escura
            github-contribution-grid-snake.gif.dark # Opcional: versão escura
        env:
          # Token de autenticação do GitHub (fornecido automaticamente pela Action)
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      # Passo 3: Commita o arquivo gerado de volta para o repositório
      # O "name" abaixo aparecerá nos logs dessa etapa
      - name: Commit snake file
        # Roda comandos shell
        run: |
          # Configurações do Git para identificar o commit como feito pela Action
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          # Adiciona os arquivos gerados para o staging area do Git
          git add github-contribution-grid-snake.svg github-contribution-grid-snake.gif github-contribution-grid-snake.svg.dark github-contribution-grid-snake.gif.dark
          # Cria o commit. O "|| echo ..." garante que não falhe se não houver mudanças
          git commit -m "Atualiza snake animation" || echo "Nenhuma alteração a commitar"
          # Envia o commit para o branch atual (geralmente main/master)
          git push
