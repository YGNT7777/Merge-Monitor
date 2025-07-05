# Merge-Monitor

This GitHub Action helps protect specific files in your repository from being modified by external contributors.

## 🚫 How It Works

1. Add a file named `.lockedFiles` to the **root** of your repository.
2. List the file paths you want to protect inside `.lockedFiles`.

---

### 📄 Example : .lockedFiles
```bash
src/secure/config.yml
secrets.json
```
- Any pull request that modifies these files will be blocked automatically.

---

## ✅ Bypass Label

To allow a pull request that **modifies locked files** to go through anyway, add the label:
``` BYPASS_LABEL```

- This label will bypass the Merge-Monitor check.

## 📺 Demo
### If there has been changes:
![final](https://github.com/user-attachments/assets/4def21bf-2e47-4e3b-be61-8fa396cee045)

### No changes 
![ok](https://github.com/user-attachments/assets/193c153c-23dc-4e1a-a960-feb0769b3f74)

### Using label
![withLabel](https://github.com/user-attachments/assets/562f8ff4-a6e5-4d3e-8cae-a7e0dde2d5df)


## 📥 How to Install

### 1. Download the Action

- Go to the [Releases](https://github.com/your-org/your-action/releases) page of this repository.
- Download the latest release ZIP file.

### 2. Add to Your Repo

- Extract the contents into your own repository.
### 🏗️ Architecture

```bash
.github/
├── actions/
│   └── check-sensitive-files/
│       ├── Dockerfile            # Builds the environment for the action
│       ├── action.yml            # Defines what the action does and how it runs
│       └── check.py              # The script that performs the file check
└── workflows/
    └── pr-check.yml              # The workflow that triggers the action on every PR

.lockedFiles                      # List of files that should not be modified
```

### 3. Configure the Workflow

> ⚠️ This step is **already configured** in the ZIP release.  
> But in case it doesn't work or you want to set it up manually

Create a file at `.github/workflows/locked-files.yml` with the following content:

```yaml
name: 'PR Check: Sensitive Files'

on:
  pull_request_target:
    types: [opened, synchronize, reopened]

permissions:
  pull-requests: write
  issues: write

jobs:
  check-sensitive-files:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Run Check Sensitive Files Action
        uses: ./.github/actions/check-sensitive-files
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
          BYPASS_LABEL: ${{ secrets.BYPASS_LABEL }}
```
### 4. Edit .lockedFiles
List the files you want to protect, one per line.

### 5. Commit and Push

## 🤝 Contibuting
Feel free to open issues and pull requests
