#!/bin/bash

# Step 1: Add all changes
git add .

# Step 2: Prompt for commit message
read -p "Enter commit message: " commit_msg

# Step 3: Commit
git commit -m "$commit_msg"

# Step 4: Push to the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
git push origin "$current_branch"
