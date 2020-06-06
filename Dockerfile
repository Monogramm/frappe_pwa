FROM monogramm/docker-erpnext:11-debian

# Install Google Chrome & Chrome WebDriver for UI tests
RUN set -ex; \
    sudo apt-get update -q; \
    sudo apt-get install -y --no-install-recommends \
        unzip \
    ; \
    CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`; \
    sudo mkdir -p "/opt/chromedriver-${CHROMEDRIVER_VERSION}"; \
    sudo curl -sS -o /tmp/chromedriver_linux64.zip "http://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"; \
    sudo unzip -qq /tmp/chromedriver_linux64.zip -d "/opt/chromedriver-${CHROMEDRIVER_VERSION}"; \
    sudo rm /tmp/chromedriver_linux64.zip; \
    sudo chmod +x "/opt/chromedriver-${CHROMEDRIVER_VERSION}/chromedriver"; \
    sudo ln -fs "/opt/chromedriver-${CHROMEDRIVER_VERSION}/chromedriver" /usr/local/bin/chromedriver; \
    export PATH="${PATH};/usr/local/bin/chromedriver"

# Build environment variables
ARG FRAPPE_APP_TO_TEST=${FRAPPE_APP_TO_TEST}


# Copy the whole repository to app folder for manual install
COPY --chown=frappe:frappe . "/home/$FRAPPE_USER/frappe-bench/apps/${FRAPPE_APP_TO_TEST}"

# Install current app
RUN set -ex; \
    ./env/bin/pip install -q -U -e "./apps/${FRAPPE_APP_TO_TEST}"; \
    bench build --app "${FRAPPE_APP_TO_TEST}"

VOLUME "/home/${FRAPPE_USER}/frappe-bench/apps/${FRAPPE_APP_TO_TEST}/public"
