# **Frappe PWA** User Guide

This is the User Guide for **Frappe PWA**.

## Summary

* [Introduction to PWA](#Introduction%20to%20PWA)
* [Usage](#Usage)

## Introduction to PWA

![PWA logo](pwalogo.svg)
Progressive Web Apps are web applications that behave like native applications, meaning they can be installed on your smartphone (directly from your browser), can send push notifications, can work offline, ...

> In order to call a Web App a PWA, technically speaking it should have the following features: Secure contexts (HTTPS), one or more Service Workers, and a manifest file.

For more details on Progressive Web Apps: <https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps>.

## Usage

This application allows to setup a Web App manifest and a Service Worker for your Frappe web app.

### Web App Manifest

Login to Frappe desk as a System Manager and search for `Web App Manifest`. There, you can set all informations describing your web application: names, icons, ...

For more details on Web App Manifests: <https://developer.mozilla.org/en-US/docs/Web/Manifest>.

### Service Worker

Login to Frappe desk as a System Manager and search for `Service Worker`. There, you can define technical fields like VAPID keys for push notifications and other technical details.

For more details on Service Workers: <https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API>.
For more details on Push Notifications: <https://developer.mozilla.org/en-US/docs/Web/API/Push_API>

## License

Copyright © 2020 [Monogramm](https://github.com/Monogramm).<br />
This project is [AGPL v3](https://opensource.org/licenses/AGPL-3.0) licensed.
