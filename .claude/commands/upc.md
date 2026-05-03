Review the current session's changes and close it with a clean commit pushed to GitHub.

Steps:
1. Run `git status` to see all modified and untracked files.
2. Run `git diff HEAD` to understand what changed across the session.
3. Run `git log --oneline -5` to match the repo's commit message style.
4. Identify a commit message following the pattern: `[OS1] Verb Subject — brief detail`. For sessions touching multiple areas, summarize the theme.
5. Stage files by name — prefer specific paths over `git add .`. Never stage: .DS_Store, .env, or files outside the repo structure.
6. Commit using a HEREDOC with the generated message, ending with:
   Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
7. Push to origin main.
8. Confirm: one line stating what was committed and pushed.

If there is nothing to commit, say so and do not create an empty commit.
