
/* --- OTTO-TASK CORE: PROTOCOLO DE SUPERVIVENCIA v5.0 --- */
const CACHE_NAME = 'otto-task-v5';
const OFFLINE_URLS = [
    '/',
    '/login/',
    '/manifest.json',
    '/sw.js',
    '/static/css/bootstrap.min.css',
    '/static/images/logo-pwa.png',
    '/static/images/google-logo.png',
    '/static/images/github-logo.png'
];

// 1. INSTALACIÓN: Forzar guardado de archivos críticos
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            console.log('🛰️ [BÚNKER]: Asegurando suministros...');
            return cache.addAll(OFFLINE_URLS);
        })
    );
    self.skipWaiting();
});

// 2. ACTIVACIÓN: Tomar el control de inmediato
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

// 3. FETCH: El filtro que evita el error "Sin Internet"
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
