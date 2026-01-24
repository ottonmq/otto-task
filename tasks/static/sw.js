
const CACHE_NAME = 'otto-task-v2';
const urlsToCache = [
  '/',
  '/static/logo-pwa.png',
  // Agrega aquí tus archivos CSS si ya los tienes
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});

