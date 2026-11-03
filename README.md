# Rastreador de Despesas Diárias

Este é um projeto realizado juntamente com o site de prática de programação Coddy, ou coddy.tech, no décimo quarto capítulo da primeira seção de Python.
A fim de reforçar o aprendizado exercitado no projeto proposto pelo capítulo do Coddy, refiz o código que fiz dentro da plataforma, traduzindo algumas partes que fui obrigado a submeter em inglês para cumprir a tarefa, e acrescentando outras coisas, ainda dentro da proposta principal.
O exercício/projeto ainda pode ser aprimorado em momentos futuros, mas o repositório foi inicialmente criado com as linhas de código que completaram a tarefa, dentro do Coddy.
O código original que enviei na plataforma está disponível como `tracker_raw.py`, para ver o arquivo alterado, procure por `tracker.py`.

## Finalidade e funções

O exercício tem como finalidade um rastreador de despesas diárias para acompanhamento financeiro, com um menu interativo que responde a números. As opções são:
> 1. Adicione uma nova despesa
> 2. Verifique todas as despesas
> 3. Calcule o total e a média das despesas
> 4. Apagar o histórico de despesas
> 5. Sair

O projeto acompanha de forma local as despesas armazenadas, as exibe e manuseia estes dados calculando a soma e a média dos mesmos.

## Exemplo de uso

Para exemplificação de uso, fiz a adição de cinco despesas, de 10 a 50:

<img width="366" height="121" alt="image" src="https://github.com/user-attachments/assets/e23b6689-942b-453b-aacc-e3d452abaeb1" />

Todas foram perfeitamente armazenadas, como mostra a imagem abaixo:

<img width="423" height="271" alt="image" src="https://github.com/user-attachments/assets/da8bfc41-11df-45f2-9372-198bb92e945f" />

E a funcionalidade de soma e média também funcionaram conforme o esperado:

<img width="422" height="206" alt="image" src="https://github.com/user-attachments/assets/3be81e0b-5711-4de1-b50f-a92f29b51826" />

## Como executá-lo

Requer Python 3.10 ou superior.
1. Clone a pasta do repositório com o comando `git clone https://github.com/niconsoli/dailyExpenseTracker_coddy.git`, ou faça o download dos arquivos pelo GitHub.
2. Entre na pasta pelo cmd com `cd %caminhodoDownload%\dailyExpenseTracker_Coddy` ou clicando com o botão direito na pasta baixada e clicando em `Abrir no terminal`.
3. Digite `python.exe tracker.py` ou `python.exe tracker_raw.py`, de acordo com qual versão você deseja executar.
4. Aproveite!
