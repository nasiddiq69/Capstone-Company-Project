# Shared Workspace System — Capstone Company Project

A collaborative Python project for a five-member team.

## Project status
Starter repository scaffold. Confirm the final requirements with your mentor before expanding the features.

## Suggested initial features
- Register and manage workspaces/rooms
- Create, view, and cancel reservations
- Prevent overlapping reservations for the same workspace
- Store reservation data (storage/database choice to be agreed by the team)
- Add tests for booking rules

## Repository structure
```text
.
├── .github/
│   └── pull_request_template.md
├── docs/
│   ├── TEAM_WORKFLOW.md
│   └── REQUIREMENTS.md
├── src/
│   └── shared_workspace/
│       ├── __init__.py
│       ├── models.py
│       └── reservation_service.py
├── scripts/
│   └── explore_dataset.py
├── tests/
│   └── test_reservation_service.py
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Setup (Windows PowerShell)
1. Install Python 3.11+ and Git.
2. Create and activate a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Run tests:
   ```powershell
   python -m unittest discover -s tests -v
   ```
5. Load and inspect the CardiacUDC training split:
   ```powershell
   python scripts/explore_dataset.py
   ```
   The first run downloads the dataset from Hugging Face into the local cache.
   The dataset files are not stored in Git; each collaborator downloads their
   own copy when they run the script.

## Setup (macOS/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/explore_dataset.py
python -m unittest discover -s tests -v
```

## Team rules
- Never commit directly to `main`.
- Create a branch for each task.
- Open a Pull Request into `develop` and ask a teammate to review it.
- Do not commit passwords, API keys, `.env` files, virtual environments, or private datasets.
- Agree on interfaces before multiple people edit the same files.

See [`docs/TEAM_WORKFLOW.md`](docs/TEAM_WORKFLOW.md).
