# -*- coding: utf-8 -*-

name = "fzf"

# Vendor packages: <vendor_version>+local.<our_version>
__version__ = "0.27.2"
version = __version__ + "+local.1.0.0"

variants = [["platform-linux", "arch-x86_64"]]


@late()
def tools():
    import os

    bin_path = os.path.join(str(this.root), "bin")
    executables = []
    for item in os.listdir(bin_path):
        path = os.path.join(bin_path, item)
        if os.access(path, os.X_OK) and not os.path.isdir(path):
            executables.append(item)
    return executables


relocatable = False

build_command = r"""
set -euf -o pipefail

# Setup: curl "{CURL_FLAGS}" ...
# Show progress bar if output to terminal, else silence
declare -a CURL_FLAGS
CURL_FLAGS=("-L")
[ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")
CURL_FLAGS+=("https://github.com/junegunn/fzf/archive/{version}.tar.gz")

if [ $REZ_BUILD_INSTALL -eq 1 ]
then
    curl "{CURL_FLAGS}"  \
    | tar -xz -C "$REZ_BUILD_INSTALL_PATH" --strip-components=1
    "$REZ_BUILD_INSTALL_PATH"/install --bin
fi
""".format(
    CURL_FLAGS="${{CURL_FLAGS[@]}}",
    install_dir="${{REZ_BUILD_INSTALL_PATH:-/usr/local}}",
    version=__version__,
)


def commands():
    import os.path
    import sys

    env.PATH.append(os.path.join("{root}", "bin"))

    if sys.stdin.isatty() and sys.stdout.isatty():
        if str(env.get("SHELL")).endswith("bash"):
            # Imitate $XDG_CONFIG_HOME/fzf/fzf.bash from "install --xdg --all"
            source(os.path.join("{root}", "shell", "completion.bash"))
            source(os.path.join("{root}", "shell", "key-bindings.bash"))
