
const CACHE_NAME = 'otto-task-v3';
const urlsToCache = [
  '/',
  '/login/',
  '/static/manifest.json',
  '/static/css/bootstrap.min.css', // Ruta confirmada en tu captura
  '/static/images/logo-pwa.png',
  '/static/images/google-logo.png',
  '/static/images/github-logo.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('Sistema Offline: Archivos guardados');
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request).catch(() => {
      return caches.match(event.request).then(response => {
        return response || caches.match('/');
      });
    })
  );
});
