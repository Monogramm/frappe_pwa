[![License: AGPL v3][uri_license_image]][uri_license]
[![Docs](https://img.shields.io/badge/Docs-Github%20Pages-blue)](https://monogramm.github.io/frappe_pwa/)
[![gitmoji-changelog](https://img.shields.io/badge/Changelog-gitmoji-blue.svg)](https://github.com/frinyvonnick/gitmoji-changelog)
[![Managed with Taiga.io](https://img.shields.io/badge/managed%20with-TAIGA.io-709f14.svg)](https://tree.taiga.io/project/monogrammbot-monogrammfrappe_pwa/ "Managed with Taiga.io")
[![Build Status](https://travis-ci.org/Monogramm/frappe_pwa.svg)](https://travis-ci.org/Monogramm/frappe_pwa)
[![Coverage Status](https://coveralls.io/repos/github/Monogramm/frappe_pwa/badge.svg?branch=master)](https://coveralls.io/github/Monogramm/frappe_pwa?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/347f10fa884446c492b6ba8cd7f4d7fc)](https://app.codacy.com/gh/Monogramm/frappe_pwa?utm_source=github.com&utm_medium=referral&utm_content=Monogramm/frappe_pwa&utm_campaign=Badge_Grade_Dashboard)

<!--
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/273679c703bb4f02ba1aacb350f7b1c5)](https://www.codacy.com/gh/Monogramm/frappe_pwa?utm_source=github.com&utm_medium=referral&utm_content=Monogramm/frappe_pwa&utm_campaign=Badge_Coverage)
[![codecov](https://codecov.io/gh/Monogramm/frappe_pwa/branch/master/graph/badge.svg)](https://codecov.io/gh/Monogramm/frappe_pwa)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/Monogramm/frappe_pwa/?ref=repository-badge)
-->

## Frappe PWA

> :alembic: PWA setup for Frappe website.

## :blue_book: Docs

See GitHub Pages at [monogramm.github.io/frappe_pwa](https://monogramm.github.io/frappe_pwa/).

## :chart_with_upwards_trend: Changes

All notable changes to this project will be documented in [CHANGELOG](./CHANGELOG.md) file.
This CHANGELOG is generated with :heart: by [gitmoji-changelog](https://github.com/frinyvonnick/gitmoji-changelog).

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## :bookmark: Roadmap

See [Taiga.io](https://tree.taiga.io/project/monogrammbot-monogrammfrappe_pwa/ "Taiga.io monogrammbot-monogrammfrappe_pwa")

## :construction: Install

**Install Frappe application**

```sh
bench get-app https://github.com/Monogramm/frappe_pwa
bench install-app frappe_pwa
```

Check [Frappe Install](https://github.com/frappe/frappe/wiki/The-Hitchhiker%27s-Guide-to-Installing-Frappe-on-Linux) for more details.

## :white_check_mark: Run tests

```sh
bench run-tests --app frappe_pwa
```

Check [Frappe Unit Testing](https://frappe.io/docs/user/en/guides/automated-testing/unit-testing) for more details.

When installing Frappe app, the following python requirements will be installed:

## :rocket: Usage

How to use this application:

-   Setup website Progressive Web Application:
    -   Go to "_Website App Manifest_" and press button "_Automatically configure PWA_" or go to "_Website Settings_" and add into "_HTML HEADER & ROBOTS_" the web app manifest manually: `<link rel="manifest" href="/manifest.json">`

After setup has been done, just go to `/install` page and press on `install` inside pop-up message.

<!--
[TODO] If project is deployed to DockerHub:
## :whale: Supported tags
[Dockerhub monogramm/frappe_pwa](https://hub.docker.com/r/monogramm/frappe_pwa/)
* `latest`
-->

## :bust_in_silhouette: Authors

**Monogramm**

-   Website: <https://www.monogramm.io>
-   Github: [@Monogramm](https://github.com/Monogramm)

## :handshake: Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Monogramm/frappe_pwa/issues).
[Check the contributing guide](./CONTRIBUTING.md).<br />

## :thumbsup: Show your support

Give a :star: if this project helped you!

## :page_facing_up: License

Copyright © 2021 [Monogramm](https://github.com/Monogramm).<br />
This project is [AGPL v3](uri_license) licensed.

* * *

_This README was generated with :heart: by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

[uri_license]: https://opensource.org/licenses/AGPL-3.0

[uri_license_image]: https://img.shields.io/badge/license-AGPL%20v3-blue
