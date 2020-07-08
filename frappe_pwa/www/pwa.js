/*!
 * Frappe PWA (https://github.com/Monogramm/frappe_pwa)
 * Copyright 2020 Monogramm
 * Licensed under AGPL v3 (https://github.com/Monogramm/frappe_pwa/blob/master/LICENSE)
 */


function showPrompt(buttonText, messageText, f) {
    const $btn = $(`<button class="pwa-next-action"><span>${__(buttonText)}</span></button>`);
    const next_action_container = $(`<div class="pwa-next-action-container"></div>`);
    $btn.click(() => f());
    next_action_container.append($btn);
    showPwaAlert({
        message: messageText,
        body: next_action_container,
        indicator: 'green',
    })
}

function showPwaAlert(message, seconds = 7) {
    if (typeof message === 'string') {
        message = {
            message: message
        };
    }
    if (!$('#pwa-dialog-container').length) {
        $('<div id="pwa-dialog-container"><div id="pwa-alert-container"></div></div>').appendTo('body');
    }

    const div = $(`
		<div class="pwa-alert pwa-desk-alert">
			<div class="pwa-alert-message"></div>
			<div class="pwa-alert-body" style="display: none"></div>
			<a class="pwa-close">&times;</a>
		</div>`);

    let pwaMessage = div.find('.pwa-alert-message');
    pwaMessage.append(message.message);

    if (message.indicator) {
        pwaMessage.addClass('indicator ' + message.indicator);
    }

    if (message.body) {
        div.find('.pwa-alert-body').show().html(message.body);
    }

    div.hide().appendTo("#pwa-alert-container").show()
        .css('transform', 'translateX(0)');

    div.find('.pwa-close, button').click(function () {
        div.remove();
        return false;
    });

    div.delay(seconds * 1000).fadeOut(300);
    return div;
}

if ('serviceWorker' in navigator) {
    if ('{{ vapid_public_key }}') {
        console.log('[PWA] Set VAPID key for push notifications');
        window.vapidPublicKey = new Uint8Array('{{ vapid_public_key }}');
    }

    window.addEventListener('load', function () {
        if (navigator.serviceWorker.controller) {
            console.log('[PWA] ServiceWorker found, no need to register');
        } else {
            navigator.serviceWorker.register('/sw.js').then(
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

    function showAddToHomeScreen(event) {
        if (installPromptEvent === null) {
            console.log('[PWA] No A2HS event stored for this device');
        } else {
            if (window.location.pathname === '/install') {
                // show to user prompt with PWA installation
                showPrompt(('{{ _("Install") }}'), '{{ _("Do you want to install PWA?") }}', addToHomeScreen);
            } else {
                // show to user prompt with Install Page redirection
                showPrompt('{{ _("Go to Install Page") }}', '{{ _("This application support PWA") }}', function () {
                        window.location.href = "/install";
                    });
            }
        }
    }

    function hideAddToHomeScreen(event) {
        $('#pwa-alert-container').hide()
    }

    window.addEventListener('appinstalled', hideAddToHomeScreen);

    // Push notifications
    function pushNotification(message) {
        navigator.serviceWorker.ready
            .then(function (serviceWorkerRegistration) {
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
} else if (window.location.protocol !== 'https:') {
    console.warn('[PWA] Requires secure HTTPS connection');
} else {
    console.warn('[PWA] No Service Worker support on your device');
}
