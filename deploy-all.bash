#!/bin/bash

set -e

git add --all
git commit -m 'save' || true
git pull
echo -n '==============================================='
./update_readme_md.py
echo -n '==============================================='
echo -n ''
git add --all
git commit -m 'save readme' || true
git push
