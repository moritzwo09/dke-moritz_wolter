FROM ubuntu:jammy

# System setup and basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository universe \
    && apt-get update

# Install all main dependencies
RUN apt-get install -y --no-install-recommends \
    git build-essential curl wget libssl-dev \
    autoconf automake libtool bzip2 \
    pkg-config sudo cmake ninja-build \
    libopenjp2-7-dev libtiff5-dev libpng-dev libgif-dev \
    libxt-dev libxml2-dev libuninameslist-dev libspiro-dev \
    python3-dev libpango1.0-dev libcairo-dev \
    chrpath uuid-dev uthash-dev \
    libpoppler-private-dev libpoppler-glib-dev \
    libcurl4-openssl-dev zlib1g-dev \
    libboost-all-dev \
    qtbase5-dev qttools5-dev-tools qt5-qmake \
    libnss3-dev \
    fontforge \
    && rm -rf /var/lib/apt/lists/*

# Build Poppler
RUN wget https://poppler.freedesktop.org/poppler-23.07.0.tar.xz \
    && tar xvf poppler-23.07.0.tar.xz \
    && cd poppler-23.07.0 && mkdir build && cd build \
    && cmake -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DTESTDATADIR=$PWD/testfiles \
        -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
        .. \
    && ninja \
    && ninja install \
    && cd ../.. && rm -rf poppler-23.07.0*

# Build pdf2htmlEX
RUN git clone --depth 1 https://github.com/pdf2htmlEX/pdf2htmlEX.git \
    && cd pdf2htmlEX \
    && ./buildScripts/buildInstallLocallyApt

VOLUME /pdf
WORKDIR /pdf
CMD ["pdf2htmlEX"]