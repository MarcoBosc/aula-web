# TDE 2 - flex box
Adicionei o "Gerador de memes Doge".
Como meu blog é sobre memes, queria colocar uma api que gerasse memes do doge, mas a única que encontrei era paga, então fiz a minha própria. Para isso foi necessário criar uma API utilizando o [Amazon API Gateway](https://aws.amazon.com/pt/api-gateway/) e o [AWS Lambda](https://aws.amazon.com/pt/pm/lambda/) para enviar um POST contendo no body os textos a serem adicionados na imagem.

## Arquitetura
<p align="center">
  <img src="/imgs/Diagrama.png" alt="Arquitetura">
</p>