const canvas       = document.getElementById('wheel');
const ctx          = canvas.getContext('2d');
const size         = canvas.width;
const radius       = size / 2;
const startAngle   = -Math.PI / 2;
const sliceAngle   = 2 * Math.PI / books.length;

// modal elements
const modal        = document.getElementById('result-modal');
const closeBtn     = document.getElementById('close-modal');
const spinAgainBtn = document.getElementById('spin-again-btn');
const startLink    = document.getElementById('start-reading-link');

const titleEl      = document.getElementById('book-title');
const authorEl     = document.getElementById('book-author');
const genreEl      = document.getElementById('book-genre');
const moodEl       = document.getElementById('book-mood');
const lengthEl     = document.getElementById('book-length');

// draw wheel
function getSliceColor(i) {
  const hue = (i * 360 / books.length + 10) % 360;
  return `hsl(${hue},35%,50%)`;
}
function drawWheel() {
  for (let i = 0; i < books.length; i++) {
    const angle = startAngle + i * sliceAngle;
    ctx.beginPath();
    ctx.moveTo(radius, radius);
    ctx.arc(radius, radius, radius, angle, angle + sliceAngle);
    ctx.fillStyle = getSliceColor(i);
    ctx.fill();

    ctx.save();
    ctx.translate(radius, radius);
    ctx.rotate(angle + sliceAngle / 2);
    ctx.textAlign = 'right';
    ctx.fillStyle = '#F5F0E1';
    ctx.font = 'bold 14px serif';
    ctx.fillText(books[i].title, radius - 10, 0);
    ctx.restore();
  }
}
drawWheel();

function showResult(book) {
  titleEl.textContent  = book.title;
  authorEl.textContent = book.author;
  genreEl.textContent  = book.genre;
  moodEl.textContent   = book.mood;
  lengthEl.textContent = book.length;
  document.getElementById('book-description').textContent = book.description || "No description available.";


  startLink.href = startReadingTemplate.replace(/0$/, book.id);

  modal.style.display = 'block';
}


closeBtn.onclick = () => modal.style.display = 'none';
spinAgainBtn.onclick = () => modal.style.display = 'none';
window.onclick = e => {
  if (e.target === modal) modal.style.display = 'none';
};

// spin logic
document.getElementById('spin').onclick = () => {
  const turns = Math.floor(Math.random() * 3600) + 3600; // 10–20 revs
  canvas.style.transition = 'transform 5s cubic-bezier(0.33,1,0.68,1)';
  canvas.style.transform  = `rotate(${turns}deg)`;

  canvas.addEventListener('transitionend', () => {
    const finalDeg = turns % 360;
    const rad      = finalDeg * Math.PI / 180;
    const hit      = (2 * Math.PI - rad - startAngle + 2 * Math.PI) % (2 * Math.PI);
    const idx      = Math.floor(hit / sliceAngle);

    canvas.style.transition = 'none';
    canvas.style.transform  = `rotate(${finalDeg}deg)`;

    showResult(books[idx]);
  }, { once: true });
};
