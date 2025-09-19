const form = document.querySelector('#conciergeForm');
if (form){
  form.addEventListener('submit', (e)=>{
    let ok = true;
    const fields = ['fullName','email','date','message'];
    fields.forEach(id=>{
      const input = form.querySelector('#'+id);
      const error = input.nextElementSibling;
      if (!input.value.trim()){
        ok = false; error.style.display='block'; error.textContent = 'Required';
      }else{
        error.style.display='none';
      }
      if (id === 'email' && input.value){
        const good = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(input.value);
        if (!good){ ok=false; error.style.display='block'; error.textContent='Enter a valid email'; }
      }
    });
    if (!ok){ e.preventDefault(); }
    else{
      e.preventDefault();
      form.reset();
      const msg = form.querySelector('.success');
      if (msg){ msg.textContent='Request received. A concierge will contact you shortly.'; }
    }
  });
}
