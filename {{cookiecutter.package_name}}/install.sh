#!/usr/bin/env bash
# This script installs {{cookiecutter.package_name}} and all of its dependencies.
#
# If a dependency can't easily be automatically installed, then it should make a good-faith effort at pointing users
# toward whatever resources they need in order to install it themselves.

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pip install --editable $THIS_DIR