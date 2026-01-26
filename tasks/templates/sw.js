
/* --- OTTO-TASK CORE: PROTOCOLO DE SUPERVIVENCIA v5.0 --- */
const CACHE_NAME = 'otto-task-v5';
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

// 1. INSTALACIÓN
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            console.log('🛰️ [BÚNKER]: Asegurando suministros...');
            return cache.addAll(OFFLINE_URLS);
        })
    );
    self.skipWaiting();
});

// 2. ACTIVACIÓN
self.addEventListener('activate', event => {
    event.waitUntil(
        Promise.all([
            self.clients.claim(),
            caches.keys().then(keys => Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            ))
        ])
    );
});

// 3. FETCH: EL FILTRO ANTI-ERROR
self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;

    event.respondWith(
        fetch(event.request)
            .then(response => {
                const resClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, resClone);
                });
                return response;
            })
            .catch(() => {
                return caches.match(event.request).then(response => {
                    return response || caches.match('/');
                });
            })
    );
});
