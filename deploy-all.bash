#!/bin/bash

set -x

git add --all
git commit -m 'save'
git pull
./update_readme_md.py
git add --all
git commit -m 'save readme'
git push
