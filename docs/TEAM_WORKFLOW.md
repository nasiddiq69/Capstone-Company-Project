# Five-member GitHub workflow

## Suggested branches
- `main`: stable submission/release version
- `develop`: integrated team work
- `feature/<short-task-name>`: one branch per task

Suggested feature branches (adapt these to the actual work):
- `feature/ui`
- `feature/reservation-logic`
- `feature/database`
- `feature/authentication`
- `feature/testing-docs`

## First-time setup (repository owner)
After creating the GitHub repository and uploading these files:
1. Create `develop` from `main` on GitHub (or locally and push it).
2. In repository Settings, add the other four members as collaborators.
3. Add branch rules for `main`; require Pull Requests and at least one approval if available.
4. Consider a similar rule for `develop` once everyone is comfortable with the workflow.

## Each member's workflow
Replace `OWNER` below with the GitHub account that owns the repository.

```bash
git clone https://github.com/OWNER/shared-workspace-system.git
cd shared-workspace-system
git switch develop
git pull origin develop
git switch -c feature/your-task
```

After editing and testing:
```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/your-task
```

Then open a Pull Request on GitHub from `feature/your-task` into `develop`. Ask a teammate to review it before merging.

Before starting the next task:
```bash
git switch develop
git pull origin develop
git switch -c feature/another-task
```

If you already have an existing branch, update it carefully; do not repeatedly create a branch with the same name.

## Collaboration rules
- Do not commit directly to `main`.
- Pull the latest target branch before starting a task.
- Keep Pull Requests focused and reasonably small.
- Discuss changes to shared interfaces before editing them.
- Never commit `.env`, passwords, tokens, student IDs, or private data.
- Do not commit `.venv/`.
- Only the repository owner should change repository settings.
