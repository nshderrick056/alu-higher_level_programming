#!/bin/bash

git add .

echo "Enter commit message:"
read msg

if [ -z "$msg" ]; then
  echo "❌ Commit message cannot be empty. Aborting."
  exit 1
fi

git commit -m "$msg"
git push