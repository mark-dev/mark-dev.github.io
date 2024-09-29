#!/bin/bash

set -x

git add --all
git commit -m 'save'
git pull
echo '==============================================='
./update_readme_md.py
echo '==============================================='
git add --all
git commit -m 'save readme'
git push
