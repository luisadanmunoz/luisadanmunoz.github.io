/* luisadanmunoz.es — comportamiento ligero, sin dependencias */
(function () {
  'use strict';

  /* Menús: solo uno abierto a la vez; se cierran al pulsar fuera o con Escape */
  var menus = Array.prototype.slice.call(document.querySelectorAll('.nav details'));
  menus.forEach(function (m) {
    m.addEventListener('toggle', function () {
      if (m.open) menus.forEach(function (o) { if (o !== m) o.open = false; });
    });
  });
  document.addEventListener('click', function (e) {
    menus.forEach(function (m) { if (m.open && !m.contains(e.target)) m.open = false; });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    menus.forEach(function (m) {
      if (m.open) { m.open = false; m.querySelector('summary').focus(); }
    });
  });

  /* Filtros por tema en los listados */
  var zona = document.querySelector('[data-filtrable]');
  if (zona) {
    var botones = zona.querySelectorAll('.filter');
    var filas = zona.querySelectorAll('.post-row');
    var contador = zona.querySelector('[data-count]');
    botones.forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-filter');
        var n = 0;
        botones.forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        filas.forEach(function (r) {
          var ok = f === '*' || r.getAttribute('data-tema') === f;
          r.hidden = !ok;
          if (ok) n++;
        });
        if (contador) {
          contador.textContent = n + ' ' + (n === 1 ? contador.getAttribute('data-singular') : contador.getAttribute('data-plural'));
        }
      });
    });
  }

  var articulo = document.getElementById('articulo');
  if (!articulo) return;

  /* Bloques de código con barra de lenguaje y botón Copiar */
  articulo.querySelectorAll('div.highlighter-rouge, figure.highlight').forEach(function (bloque) {
    if (bloque.closest('.code-block')) return;
    var code = bloque.querySelector('code');
    if (!code || code.classList.contains('language-mermaid')) return;
    var lang = (bloque.className.match(/language-([\w-]+)/) || [])[1] || '';
    var marco = document.createElement('div');
    marco.className = 'code-block';
    var barra = document.createElement('div');
    barra.className = 'code-bar';
    var etiqueta = document.createElement('span');
    etiqueta.textContent = lang && lang !== 'plaintext' ? lang : 'código';
    var copiar = document.createElement('button');
    copiar.type = 'button';
    copiar.textContent = 'Copiar';
    copiar.addEventListener('click', function () {
      navigator.clipboard.writeText(code.innerText).then(function () {
        copiar.textContent = 'Copiado';
        setTimeout(function () { copiar.textContent = 'Copiar'; }, 1800);
      });
    });
    barra.appendChild(etiqueta);
    barra.appendChild(copiar);
    bloque.parentNode.insertBefore(marco, bloque);
    marco.appendChild(barra);
    marco.appendChild(bloque);
  });

  /* Índice lateral a partir de los títulos de sección */
  var toc = document.querySelector('.toc');
  var titulos = articulo.querySelectorAll('h2[id]');
  if (toc && titulos.length >= 2) {
    var nav = toc.querySelector('nav');
    titulos.forEach(function (h) {
      if (h.closest('.sources')) return;
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      nav.appendChild(a);
    });
    toc.hidden = false;
    if ('IntersectionObserver' in window) {
      var enlaces = nav.querySelectorAll('a');
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (en) {
          if (!en.isIntersecting) return;
          enlaces.forEach(function (l) { l.classList.toggle('is-active', l.getAttribute('href') === '#' + en.target.id); });
        });
      }, { rootMargin: '0px 0px -70% 0px' });
      titulos.forEach(function (h) { obs.observe(h); });
    }
  }
})();
