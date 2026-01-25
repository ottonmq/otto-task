
/* --- OTTO-TASK CORE: PROTOCOLO DE SUPERVIVENCIA v5.0 --- */
const CACHE_NAME = 'otto-task-v5';
const OFFLINE_URLS = [
    '/',
    '/login/',
    '/static/manifest.json',
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
    self.skipWaiting(); // Fuerza la actualización sin esperar a cerrar el navegador
});

// 2. ACTIVACIÓN: Tomar el control de inmediato
self.addEventListener('activate', event => {
    event.waitUntil(
        Promise.all([
            self.clients.claim(),
            // Borrar cachés viejos (v3, v4, etc)
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
                // Si hay red, guardamos una copia de lo que el usuario ve
                const resClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, resClone);
                });
                return response;
            })
            .catch(() => {
                // SI NO HAY RED: Buscamos en el búnker
                return caches.match(event.request).then(response => {
                    // Si tenemos la página en caché, la damos. 
                    // Si no, forzamos la carga de la Home '/'
                    return response || caches.match('/');
                });
            })
    );
});
