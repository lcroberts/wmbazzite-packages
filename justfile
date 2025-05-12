default:
    just --list

setup:
    rpmdev-setuptree

build spec: setup
    spectool -g -R {{spec}}
    rpmbuild -ba {{spec}}
