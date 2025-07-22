#!/usr/bin/env bash

info="Alerts Commit: $(date)"

case "$OSTYPE" in
    darwin*)
        cd "`dirname $0`" || exit 1
        ;;

    linux*)
        cd "$(dirname "$(readlink -f "$0")")" || exit 1
        ;;

    *)
        echo "OS unsupported"
        ;;
esac

python3 ./recorddata.py

# Detect current branch (main, master, etc)
branch=$(git rev-parse --abbrev-ref HEAD)

# Ship it
git add output.txt
git commit -m "$info"
git push origin "$branch"

cd -