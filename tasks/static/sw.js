self.addEventListener('install', (e) => {
  console.log('[Otto-Task] Instalado');
});

self.addEventListener('fetch', (e) => {
  // Solo deja pasar las peticiones, no cacheamos para no complicar el Nivel 1
  e.respondWith(fetch(e.request));
});
