# Git and GitHub assignment walkthrough

Prerequisites: install Git and Python 3, create/sign into a GitHub account, and configure Git (`git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`). Authenticate GitHub using GitHub CLI (`gh auth login`) or your preferred Git credential method.

The ZIP contains starter files, **not** a pre-existing GitHub repository. Create your own repo and execute the actions below to produce genuine commits, PR links and a screenshot. The `.gitignore` is already included; commit it separately as required.

## 1. Create the repository and clone it

On GitHub, create an empty **public** repository named `ai-training-week1` (do not initialize README, license, or gitignore). Copy its HTTPS URL, then run:

```bash
git clone https://github.com/YOUR_USERNAME/ai-training-week1.git
cd ai-training-week1
```

Copy the ZIP's `.gitignore` into this cloned folder first, then:

```bash
git add .gitignore
git commit -m "chore: add Python gitignore"
git push -u origin main
```

If your default branch is not `main`, rename it first with `git branch -M main` before pushing.

## 2. Feature branch and pull request

Copy `charts.py`, `requirements.txt`, `README.md`, and `GIT_WORKFLOW.md` from the ZIP into the cloned folder (optionally `SUBMISSION.md`). Then:

```bash
git switch -c feature/add-charts
git add charts.py requirements.txt README.md GIT_WORKFLOW.md SUBMISSION.md
git commit -m "feat: add four charts in a 2x2 figure"
git push -u origin feature/add-charts
```

If you didn't copy `SUBMISSION.md`, omit it from the `git add` command. On GitHub open a PR from `feature/add-charts` into `main`, record the PR URL, and **merge with 'Create a merge commit'** (not squash/rebase). Then:

```bash
git switch main
git pull origin main
```

## 3. Deliberately create and resolve a README conflict

Start both branches from the same main commit, and change the **same line** in README.md differently. For example, replace the first line (`# AI Training Week 1 — Git and GitHub Workflow`) with the following branch-specific text.

```bash
git switch -c docs/readme-a
# Edit README.md first line to: # AI Training Week 1 — Chart Project
git add README.md
git commit -m "docs: rename README heading for charts"
git switch main
git switch -c docs/readme-b
# Edit README.md first line to: # AI Training Week 1 — Git Practice
git add README.md
git commit -m "docs: rename README heading for Git practice"
git switch main
git merge --no-ff docs/readme-a
# This next command should report a conflict:
git merge --no-ff docs/readme-b
```

Open README.md and locate `<<<<<<<`, `=======`, and `>>>>>>>`. Remove those markers and keep a final heading such as `# AI Training Week 1 — Charts and Git Practice`. Then:

```bash
git add README.md
git commit -m "merge: resolve README heading conflict"
git push origin main
```

The conflict is intentional. Do not run `git merge --abort` unless you want to restart the exercise.

## 4. Show the history and take a real screenshot

```bash
git log --oneline --graph --decorate --all
```

Take a screenshot of your terminal showing the graph (Windows: Win+Shift+S; macOS: Cmd+Shift+4), save it as `screenshots/git-log-graph.png`, then commit and push the screenshot:

```bash
git add screenshots/git-log-graph.png
git commit -m "docs: add Git history screenshot"
git push origin main
```

Update `SUBMISSION.md` with your real repository and PR URLs, commit, and push it. The screenshot itself should show the actual graph, including the feature PR merge and conflict-resolution merge.

## Useful commands

- `git init`: initialize a new local repository (alternative to cloning an empty GitHub repo)
- `git status`: inspect changes and conflict state
- `git add`: stage changes
- `git commit`: save a snapshot
- `git push`: upload local commits
- `git pull`: fetch and integrate remote changes
- `git branch`: list/create branches
- `git merge`: combine branch histories
