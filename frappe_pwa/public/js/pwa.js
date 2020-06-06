/*!
 * Frappe PWA (https://github.com/Monogramm/frappe_pwa)
 * Copyright 2020 Monogramm
 * Licensed under AGPL v3 (https://github.com/Monogramm/frappe_pwa/blob/master/LICENSE)
 */

if ('serviceWorker' in navigator) {
    //window.vapidPublicKey = new Uint8Array('{{ vapid_public_key }}');

    window.addEventListener('load', function () {
        if (navigator.serviceWorker.controller) {
            console.log('[PWA] ServiceWorker found, no need to register');
        } else {
            navigator.serviceWorker.register('/assets/frappe_pwa/js/sw.js').then(
                function (registration) {
                    // Registration was successful
                    console.log('[PWA] ServiceWorker registration successful with scope: ' + registration.scope);

                    if (window.vapidPublicKey) {
                        console.log('[PWA] Subscribing to push notifications');

                        registration.pushManager.subscribe({
                            userVisibleOnly: true,
                            applicationServerKey: window.vapidPublicKey
                        }).then(
                            function (pushSubscription) {
                                console.log(pushSubscription.subscriptionId);
                                console.log(pushSubscription.endpoint);
                                // The push subscription details needed by the application
                                // server are now available, and can be sent to it using,
                                // for example, an XMLHttpRequest.
                            }, function (error) {
                                // During development it often helps to log errors to the
                                // console. In a production environment it might make sense to
                                // also report information about errors back to the
                                // application server.
                                console.log(error);
                            }
                        );
                    }
                }, function (err) {
                    // registration failed :(
                    console.log('[PWA] ServiceWorker registration failed: ', err);
                });
        }
    });

    var installPromptEvent = null;
    window.addEventListener('beforeinstallprompt', function (e) {
        e.preventDefault();
        installPromptEvent = e;

        console.log('[PWA] Application could be installed');
        showAddToHomeScreen();
    });

    function showAddToHomeScreen(event) {
        btnAdd = document.getElementById('pwa-install-link');

        if (installPromptEvent === null) {
            console.log('[PWA] No A2HS event stored for this device');
        } else if (btnAdd === null) {
            console.log('[PWA] The page has not finished initializing. Postponing A2HS on page load.');
            document.body.addEventListener('load', showAddToHomeScreen);
        } else {
            // Update UI to notify the user they can add to home screen
            btnAdd.classList.remove('is-hidden');

            btnAdd.addEventListener('click', addToHomeScreen);
        }
    }

    function addToHomeScreen(event) {
        // Show the prompt
        hideAddToHomeScreen();

        if (installPromptEvent === null) {
            console.log('[PWA] No A2HS event to trigger for this device');
        } else {
            installPromptEvent.prompt();

            // Wait for the user to respond to the prompt
            installPromptEvent.userChoice
                .then(function (choiceResult) {
                    if (choiceResult.outcome === 'accepted') {
                        console.log('[PWA] User accepted the A2HS prompt');
                    } else {
                        console.log('[PWA] User dismissed the A2HS prompt');
                    }
                    installPromptEvent = null;
                });
        }
    }

    function hideAddToHomeScreen(event) {
        btnAdd = document.getElementById('pwa-install-link');

        // hide our user interface that shows our A2HS button
        if (btnAdd !== null) {
            btnAdd.classList.add('is-hidden');
        }
    }

    window.addEventListener('appinstalled', hideAddToHomeScreen);

    // Push notifications
    function pushNotification(message) {
        navigator.serviceWorker.ready
            .then(function (serviceWorkerRegistration)  {
                serviceWorkerRegistration.pushManager.getSubscription()
                    .then(function (subscription) {
                        $.post('/push', {
                            subscription: subscription.toJSON(),
                            message: message
                        });
                    });
            });
    }

    // Request to allow push notifications
    if (window.vapidPublicKey) {
        if (!("Notification" in window)) {
            console.error("[PWA] This browser does not support desktop notification");
        } else if (Notification.permission === "granted") {
            console.log("[PWA] Permission to receive notifications has been granted");
        } else if (Notification.permission !== 'denied') {
            Notification.requestPermission(function (permission) {
                // If the user accepts, let's create a notification
                if (permission === "granted") {
                    console.log("[PWA] Permission to receive notifications has been granted");
                }
            });
        }
    }
} else if(window.location.protocol !== 'https:') {
    console.warn('[PWA] Requires secure HTTPS connection');
} else {
    console.warn('[PWA] No Service Worker support on your device');
}
