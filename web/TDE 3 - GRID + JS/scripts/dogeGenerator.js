document.getElementById("memeForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const topText = formData.get('topText');
    const bottomText = formData.get('bottomText');

    const requestData = {
        "top_word": topText,
        "bottom_word": bottomText
    };

    const url = `https://nwv2sesopl.execute-api.us-east-1.amazonaws.com/default/doge-meme-generator`;
    const options = {
        method: 'POST',
        body: JSON.stringify(requestData),
        headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
        }
    };

    try {
        const response = await fetch(url, options);
        if (response.ok) {
            const blob = await response.blob(); // Obtém o blob da imagem
            const imageURL = URL.createObjectURL(blob); // Cria a URL do objeto
            const memeImage = document.createElement('img');
            memeImage.src = imageURL;
            memeImage.alt = "Imagem gerada";
            document.getElementById("memeImageContainer").innerHTML = ""; // Limpa o conteúdo anterior
            document.getElementById("memeImageContainer").appendChild(memeImage);
        } else {
            throw new Error('Erro ao fazer a requisição: ' + response.statusText);
        }
    } catch (error) {
        console.error(error);
    }
});
