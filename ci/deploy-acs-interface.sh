#!/bin/bash -ex

cd "$( dirname "${BASH_SOURCE[0]}" )"

trap "vagrant destroy -f"  EXIT

vagrant up

vagrant ssh -- < ./test-pytest.sh
