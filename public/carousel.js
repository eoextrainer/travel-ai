(function(){
  const track = document.querySelector('.carousel-track');
  const slides = Array.from(document.querySelectorAll('.slide'));
  const prev = document.querySelector('.nav.prev');
  const next = document.querySelector('.nav.next');
  let index = 0;
  function update(){
    track.style.transform = `translateX(-${index * 100}%)`;
    // pause all iframes; play current via postMessage
    slides.forEach((iframe, i) => {
      const msg = JSON.stringify({ event: 'command', func: i === index ? 'playVideo' : 'pauseVideo' });
      iframe.contentWindow && iframe.contentWindow.postMessage(msg, '*');
    });
  }
  prev.addEventListener('click', () => { index = (index - 1 + slides.length) % slides.length; update(); });
  next.addEventListener('click', () => { index = (index + 1) % slides.length; update(); });
  update();
})();