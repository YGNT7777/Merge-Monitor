# .github/actions/check-sensitive-files/check.py
import os
import sys
import requests

token = os.environ['GITHUB_TOKEN']
repo = os.environ['GITHUB_REPOSITORY']
pr_number = os.environ['PR_NUMBER']
bypass_label = os.environ.get('BYPASS_LABEL', 'allow-sensitive-change')

locked_file_path = "lockedFiles.txt"

if not os.path.exists(locked_file_path):
    print(f"❌ Error: {locked_file_path} not found in repository.")
    sys.exit(1)

with open(locked_file_path, "r") as f:
    sensitive_files = [line.strip() for line in f if line.strip()]


headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

label_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/labels"
labels_resp = requests.get(label_url, headers=headers)
labels = [label['name'] for label in labels_resp.json()]
if bypass_label in labels:
    print(f"✅ Label '{bypass_label}' found. Allowing changes.")
    sys.exit(0)

files_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"
files_resp = requests.get(files_url, headers=headers)
changed_files = [file['filename'] for file in files_resp.json()]

for f in changed_files:
    if f in sensitive_files:
        print(f"❌ Sensitive file changed: {f}")
        sys.exit(1)

print("✅ No sensitive files changed.")
sys.exit(0)
