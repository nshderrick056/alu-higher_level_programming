#!/bin/bash

# Prompt for commit message
echo "Enter your commit message:"
read commit_msg

# Stage all changes
git add .

# Commit with message
git commit -m "$commit_msg"

# Push to the current branch
git push

echo "✅ Code pushed to GitHub successfully!"