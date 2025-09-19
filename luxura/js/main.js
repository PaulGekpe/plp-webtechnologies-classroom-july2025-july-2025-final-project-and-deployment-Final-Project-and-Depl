// Mobile menu toggle
const burger = document.querySelector('.hamburger');
const menu = document.querySelector('.menu');
if (burger && menu){
  burger.addEventListener('click', ()=>{
    const visible = getComputedStyle(menu).display !== 'none';
    menu.style.display = visible ? 'none' : 'flex';
    burger.setAttribute('aria-expanded', String(!visible));
  });
}

// Reveal on scroll
const revealEls = document.querySelectorAll('.reveal');
const onScroll = ()=>{
  const trigger = window.innerHeight * 0.9;
  revealEls.forEach(el=>{
    const top = el.getBoundingClientRect().top;
    if (top < trigger){ el.classList.add('visible'); }
  });
};
window.addEventListener('scroll', onScroll);
window.addEventListener('load', onScroll);

// Image zoom modal (simple)
document.addEventListener('click', (e)=>{
  const img = e.target.closest('.zoomable');
  if (!img) return;
  const overlay = document.createElement('div');
  overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.85);display:grid;place-items:center;z-index:9999;';
  const big = new Image();
  big.src = img.src;
  big.alt = img.alt || '';
  big.style.cssText = 'max-width:92vw;max-height:92vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.6)';
  overlay.appendChild(big);
  overlay.addEventListener('click', ()=> overlay.remove());
  document.body.appendChild(overlay);
});
