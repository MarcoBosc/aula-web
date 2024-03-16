const tempoNyandando = document.querySelector('.nyaned_time');

function nyanporizador() {
    const tempoDePagina = Date.now() - tempoInicial;
    
    const segundos = Math.floor(tempoDePagina / 1000);
    const milissegundos = tempoDePagina % 1000;
    
    const tempoFormatado = `${segundos}.${milissegundos} segundos`;
    
    tempoNyandando.textContent = `Você "Nyandou" por ${tempoFormatado}`;
}

const tempoInicial = Date.now();

setInterval(nyanporizador, 1);
