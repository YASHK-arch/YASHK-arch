#!/usr/bin/env python3
"""
update_contributions.py
Fetches merged PRs and issues authored by YASHK-arch via the GitHub Search API
and updates README.md between <!-- PR-LIST:START/END --> and <!-- ISSUES-LIST:START/END --> markers.
"""

import os
import re
import sys
import urllib.request
import urllib.error
import json
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────
USERNAME       = "YASHK-arch"
README_PATH    = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
TOKEN          = os.environ.get("GITHUB_TOKEN", "")
MAX_PRS        = 20
MAX_ISSUES     = 20

# ── Helpers ───────────────────────────────────────────────────────────────────
def gh_get(url: str) -> dict:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "readme-updater/1.0")
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"[ERROR] HTTP {e.code} for {url}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return {}


def fmt_date(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return iso[:10]


def label_badge(label: str) -> str:
    """Map a GitHub label to a short terminal-style tag."""
    l = label.lower()
    if any(k in l for k in ["bug", "fix", "patch"]):
        return "🐛 BUG-FIX"
    if any(k in l for k in ["feat", "feature", "enhancement", "improve"]):
        return "✨ FEATURE"
    if any(k in l for k in ["doc", "readme"]):
        return "📝 DOCS"
    if any(k in l for k in ["test"]):
        return "🧪 TEST"
    if any(k in l for k in ["chore", "refactor", "style", "ci"]):
        return "🔧 CHORE"
    if any(k in l for k in ["question", "help"]):
        return "❓ QUESTION"
    return f"🏷 {label[:12].upper()}"


def classify_issue(item: dict) -> str:
    labels = [lb["name"] for lb in item.get("labels", [])]
    if labels:
        return label_badge(labels[0])
    title = item.get("title", "").lower()
    if any(k in title for k in ["bug", "fix", "error", "crash", "fail"]):
        return "🐛 BUG-FIX"
    if any(k in title for k in ["feat", "add", "new", "request", "enhance"]):
        return "✨ FEATURE"
    if any(k in title for k in ["doc", "readme", "wiki"]):
        return "📝 DOCS"
    return "📋 GENERAL"


# ── Fetch data ────────────────────────────────────────────────────────────────
def fetch_merged_prs() -> list:
    url = (
        f"https://api.github.com/search/issues"
        f"?q=author:{USERNAME}+type:pr+is:merged"
        f"&sort=updated&order=desc&per_page={MAX_PRS}"
    )
    data = gh_get(url)
    return data.get("items", [])


def fetch_issues() -> list:
    url = (
        f"https://api.github.com/search/issues"
        f"?q=author:{USERNAME}+type:issue"
        f"&sort=updated&order=desc&per_page={MAX_ISSUES}"
    )
    data = gh_get(url)
    return data.get("items", [])


# ── Render ────────────────────────────────────────────────────────────────────
def render_pr_table(prs: list) -> str:
    if not prs:
        return (
            "<div align=\"center\">\n\n"
            "> No public merged PRs found for this account yet.\n\n"
            "</div>"
        )

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = []
    for pr in prs:
        repo_url  = pr.get("repository_url", "")
        repo_name = repo_url.replace("https://api.github.com/repos/", "") if repo_url else "unknown/repo"
        title     = pr.get("title", "No title")[:72]
        body      = (pr.get("body") or "").strip().split("\n")[0][:90]
        desc      = body if body else "_No description provided_"
        number    = pr.get("number", "?")
        pr_url    = pr.get("html_url", "#")
        date      = fmt_date(pr.get("closed_at") or pr.get("updated_at") or "")
        rows.append(
            f"| `✓ MERGED` | [**#{number}** — {title}]({pr_url}) | `{repo_name}` | {desc} | `{date}` |"
        )

    header = (
        "| Status | Pull Request | Repository | Description | Merged |\n"
        "|:---:|:---|:---|:---|:---:|"
    )
    table = header + "\n" + "\n".join(rows)

    return (
        f"<div align=\"center\">\n\n"
        f"<sub>🔄 Auto-updated: `{updated}` · showing last {len(prs)} merged PRs</sub>\n\n"
        f"</div>\n\n"
        f"{table}"
    )


def render_issues_table(issues: list) -> str:
    if not issues:
        return (
            "<div align=\"center\">\n\n"
            "> No public issues found for this account yet.\n\n"
            "</div>"
        )

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = []
    for issue in issues:
        repo_url  = issue.get("repository_url", "")
        repo_name = repo_url.replace("https://api.github.com/repos/", "") if repo_url else "unknown/repo"
        title     = issue.get("title", "No title")[:72]
        body      = (issue.get("body") or "").strip().split("\n")[0][:90]
        desc      = body if body else "_No description provided_"
        number    = issue.get("number", "?")
        issue_url = issue.get("html_url", "#")
        state     = issue.get("state", "open").upper()
        state_tag = "🟢 OPEN" if state == "OPEN" else "🔴 CLOSED"
        date      = fmt_date(issue.get("updated_at") or "")
        kind      = classify_issue(issue)
        rows.append(
            f"| `{state_tag}` | `{kind}` | [**#{number}** — {title}]({issue_url}) | `{repo_name}` | {desc} | `{date}` |"
        )

    header = (
        "| State | Type | Issue | Repository | Description | Updated |\n"
        "|:---:|:---:|:---|:---|:---|:---:|"
    )
    table = header + "\n" + "\n".join(rows)

    return (
        f"<div align=\"center\">\n\n"
        f"<sub>🔄 Auto-updated: `{updated}` · showing last {len(issues)} issues</sub>\n\n"
        f"</div>\n\n"
        f"{table}"
    )


# ── README updater ────────────────────────────────────────────────────────────
def replace_between(text: str, start_marker: str, end_marker: str, new_content: str) -> str:
    pattern = re.compile(
        rf"({re.escape(start_marker)}\n)(.*?)(\n{re.escape(end_marker)})",
        re.DOTALL,
    )
    replacement = rf"\g<1>{new_content}\g<3>"
    updated, count = pattern.subn(replacement, text)
    if count == 0:
        print(f"[WARN] Marker pair not found: {start_marker!r}", file=sys.stderr)
    return updated


def main():
    readme_path = os.path.abspath(README_PATH)
    print(f"[INFO] Reading {readme_path}")
    with open(readme_path, "r", encoding="utf-8") as f:
        original = f.read()

    print("[INFO] Fetching merged PRs…")
    prs = fetch_merged_prs()
    print(f"[INFO]   → {len(prs)} PRs found")

    print("[INFO] Fetching issues…")
    issues = fetch_issues()
    print(f"[INFO]   → {len(issues)} issues found")

    pr_content     = render_pr_table(prs)
    issues_content = render_issues_table(issues)

    updated = original
    updated = replace_between(updated, "<!-- PR-LIST:START -->",     "<!-- PR-LIST:END -->",     pr_content)
    updated = replace_between(updated, "<!-- ISSUES-LIST:START -->", "<!-- ISSUES-LIST:END -->", issues_content)

    if updated == original:
        print("[INFO] No changes detected — README is already up to date.")
        return

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("[INFO] README.md updated successfully ✓")


if __name__ == "__main__":
    main()
