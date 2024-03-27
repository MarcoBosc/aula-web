# TDE 2 - flex box
Adicionei o "Gerador de memes Doge".
Como meu blog é sobre memes, queria colocar uma api que gerasse memes do doge, mas a única que encontrei era paga, então fiz a minha própria. Para isso foi necessário criar uma API utilizando o [Amazon API Gateway](https://aws.amazon.com/pt/api-gateway/) e o [AWS Lambda](https://aws.amazon.com/pt/pm/lambda/) para enviar um POST contendo no body os textos a serem adicionados na imagem.

## Arquitetura
<p align="center">
  <img src="https://github.com/MarcoBosc/aula-web/blob/main/web/TDE%203%20-%20GRID%20%2B%20JS/imgs/Diagrama.png" alt="Arquitetura">
</p>

## Exemplo de requisição
```
const topText = "String 1"; // texto do topo da imagem
const bottomText = "String 2"; // texto de baixo da imagem

const requestData = { // Montando o body
    "top_word": topText,
    "bottom_word": bottomText
};

const url = `https://nwv2sesopl.execute-api.us-east-1.amazonaws.com/default/doge-meme-generator`; // Endpoint da api
const options = { // Montando a requisição, aqui definimos o método da requisição "POST" e o content type enviado para o API Gateway
    method: 'POST',
    body: JSON.stringify(requestData), // Convertendo o body para string
    headers: {
        'Content-Type': 'application/json', // Tipo do conteúdo enviado
    }
};

try {
    const response = await fetch(url, options); // Enviando a requisição para a API
    if (response.ok) { // Verifica se o status code da resposta foi 200
        const blob = await response.blob(); // Obtém o blob da imagem
        const imageURL = URL.createObjectURL(blob); // Cria a URL do objeto
        const memeImage = document.createElement('img'); // Cria uma tag img
        memeImage.src = imageURL; // Coloca a imagem retornada pela API como o src
        memeImage.alt = "Imagem gerada"; // Adiciona um texto alternativo
        document.getElementById("memeImageContainer").innerHTML = ""; // Limpa o conteúdo anterior caso exista
        document.getElementById("memeImageContainer").appendChild(memeImage); // Adiciona a tag img criada como filha da div com o id "memeImageContainer"
    } else {
        throw new Error('Erro ao fazer a requisição: ' + response.statusText); // Caso a requisição não esteja com o status code 200 ele mostra o erro
    }
} catch (error) {
    console.error(error); // Caso a requisição falhe ele mostra o erro
}
```

## Exemplo de imagem de retorno
<p align="center">
  <img src="/imgs/image.png" alt="Arquitetura">
</p>