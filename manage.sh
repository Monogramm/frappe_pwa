#!/bin/bash
set -e

. .env

###########################################################
# Functions

log() {
    echo "[${0}] [$(date +%Y-%m-%dT%H:%M:%S)] ${1}"
}

dc() {
    docker-compose -f ${@}
}

build() {
    log 'Building container(s)...'
    dc "${1}" build ${@:2}
    # (dirty) trick to allow edition of files generated from docker group
    chmod -R g+w .
}

start() {
    log 'Starting container(s)...'
    dc "${1}" up -d ${@:2}
}

stop() {
    log 'Stopping container(s)...'
    dc "${1}" stop ${@:2}
}

restart() {
    log 'Restarting container(s)...'
    dc "${1}" restart ${@:2}
}

ps() {
    log 'Listing container(s)...'
    dc "${1}" ps ${@:2}
}

logs() {
    log 'Following container(s) logs (Ctrl + C to stop)...'
    dc "${1}" logs -f ${@:2}
}

down() {
    log 'Stopping and removing container(s) and data...'
    dc "${1}" down ${@:2}
    rm -rf "${ERPNEXT_HOME:-/srv/erpnext_template/frappe}"/*
}

console() {
    dc -it "${1}" exec erpnext_app bench console ${@:2}
}

## TODO Add function to initialize from template
#   - Replace all occurences of `erpnext_template` and `ERPNext Template` in all files
#   - Rename all directories `erpnext_template`

prepare_release() {
    NEW_VERSION=${1}
    if [ -z "${NEW_VERSION}" ] ; then
        log 'Missing release version!'
        return 1;
    fi

    log 'Updating Frappe app version...'
    sed -i \
        -e "s|__version__ = '.*'|__version__ = '${NEW_VERSION}'|g" \
        ./erpnext_template/__init__.py

    log 'Updating gitmoji-changelog version...'
    sed -i \
        -e "s|\"version\": \".*\"|\"version\": \"${NEW_VERSION}\"|g" \
        ./.gitmoji-changelogrc

    # Generate Changelog for version
    log "Generating Changelog for version '${NEW_VERSION}'..."
    npm install
    npm run gitmoji-changelog

    # TODO Add and commit to git with message `:bookmark: Release X.Y.Z`
}

usage() {
    echo "usage: ./manage.sh COMMAND [ARGUMENTS]

    Commands:
        build               Build Dev env
        start               Start Dev env
        restart             Retart Dev env
        stop                Stop Dev env
        test                Start and follow Dev env test container
        ps                  List Dev env containers
        logs                Follow logs of Dev env
        down                Stop and remove Dev env
        console             Send command to Dev env bench console
        prepare-release     Prepare Frappe app release
    "
}

###########################################################
# Runtime

case "${1}" in
    # DEV env
    build) build docker-compose.yml ${@:2};;
    start) start docker-compose.yml ${@:2};;
    restart) restart docker-compose.yml ${@:2};;
    stop) stop docker-compose.yml ${@:2};;
    test) start docker-compose.yml sut
    logs docker-compose.yml sut;;
    ps) ps docker-compose.yml ${@:2};;
    logs) logs docker-compose.yml ${@:2};;
    down) down docker-compose.yml ${@:2};;
    console) console docker-compose.yml ${@:2};;
    prepare-release) prepare_release ${@:2};;
    # PROD env
    #build) TAG=${DOCKER_TAG} \
    #    VCS_REF=`git rev-parse --short HEAD` \
    #    BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
    #    build .travis/docker-compose.yml ${@:2};;
    #start) start .travis/docker-compose.mariadb.yml ${@:2};;
    #restart) restart .travis/docker-compose.mariadb.yml ${@:2};;
    #stop) stop .travis/docker-compose.mariadb.yml ${@:2};;
    #logs) logs .travis/docker-compose.mariadb.yml ${@:2};;
    #down) down .travis/docker-compose.mariadb.yml ${@:2};;
    #console) console .travis/docker-compose.mariadb.yml ${@:2};;
    # Help
    *) usage;;
esac

exit 0
