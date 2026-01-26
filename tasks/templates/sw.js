
/* --- OTTO-TASK CORE: PROTOCOLO DE SUPERVIVENCIA v5.0 --- */
const CACHE_NAME = 'otto-task-v5';

// Suministros críticos para que el Búnker sea Cyberpunk
const OFFLINE_URLS = [
    '/',
    '/login/',
    '/manifest.json',
    '/sw.js',
    '/static/css/bootstrap.min.css',
    '/static/css/style.css',
    '/static/images/logo-pwa.png',
    '/static/images/google-logo.png',
    '/static/images/github-logo.png',
    'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css',
    'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap',
    'https://unpkg.com/htmx.org@1.9.10',
    'https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js'
];

// 1. INSTALACIÓN: Secuestrar archivos y meterlos al búnker
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            console.log('🛰️ [BÚNKER]: Asegurando suministros...');
            // Force fetch para evitar cachés viejos del navegador
            return cache.addAll(OFFLINE_URLS.map(url => new Request(url, {cache: 'reload'})));
        })
    );
    self.skipWaiting();
});

// 2. ACTIVACIÓN: Purgar versiones viejas y tomar control total
self.addEventListener('activate', event => {
    event.waitUntil(
        Promise.all([
            self.clients.claim(),
            caches.keys().then(keys => Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            ))
        ])
    );
    console.log('🛰️ [SISTEMA]: Búnker v5.0 en línea.');
});

// 3. FETCH: Interceptar peticiones cuando no hay red
self.addEventListener('fetch', event => {
    // Solo manejamos peticiones GET
    if (event.request.method !== 'GET') return;

    event.respondWith(
        fetch(event.request)
            .then(response => {
                // Si hay internet, actualizamos el caché con lo nuevo
                const resClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, resClone);
                });
                return response;
            })
            .catch(() => {
                // SI NO HAY RED: Buscamos en el Búnker
                return caches.match(event.request).then(response => {
                    // Si el archivo está en caché, lo damos. Si no, mandamos a la raíz (búnker)
                    return response || caches.match('/');
                });
            })
    );
});
