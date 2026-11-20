"""Holt die 500 GitHub-Repos mit den meisten Sternen und schreibt data.json."""
import datetime
import json
import os
import urllib.request

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def fetch(page):
    url = ("https://api.github.com/search/repositories"
           f"?q=stars:%3E20000&sort=stars&order=desc&per_page=100&page={page}")
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["items"]


repos, seen = [], set()
for page in range(1, 6):
    for r in fetch(page):
        if r["full_name"] in seen:
            continue
        seen.add(r["full_name"])
        repos.append({
            "n": r["full_name"],
            "s": r["stargazers_count"],
            "f": r["forks_count"],
            "l": r["language"] or "Other",
            "d": (r["description"] or "")[:140],
            "c": r["created_at"][:4],
            "t": (r.get("topics") or [])[:4],
        })

out = {"updated": datetime.date.today().isoformat(), "repos": repos}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print(f"{len(repos)} Repos gespeichert")
