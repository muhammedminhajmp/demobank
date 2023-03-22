const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
  const form = document.getElementById('form');

  if (form.style.display === 'hidden') {
    // 👇️ this SHOWS the form
    form.style.display = 'visible';
  } else {
    // 👇️ this HIDES the form
    form.style.display = 'hidden';
  }
});
