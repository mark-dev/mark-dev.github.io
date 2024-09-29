#!/bin/bash

set -e

git add --all
git commit -m 'save'
git pull
echo -n '==============================================='
./update_readme_md.py
echo -n '==============================================='
git add --all
git commit -m 'save readme'
git push
