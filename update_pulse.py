#!/usr/bin/env python3
import json
import os
import html
import urllib.request
from collections import Counter
from datetime import datetime, timezone

USER = os.getenv("GH_USER", "Pedrinscrk")
TOKEN = os.getenv("GH_TOKEN", "").strip()

def api(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "pedrinscrk-profile-pulse"
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))

def esc(value):
    return html.escape(str(value or ""))

profile = api(f"https://api.github.com/users/{USER}")
repos = api(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&sort=updated")
events = api(f"https://api.github.com/users/{USER}/events/public?per_page=20")

stars = sum(int(repo.get("stargazers_count", 0)) for repo in repos)
forks = sum(int(repo.get("forks_count", 0)) for repo in repos)
langs = Counter(repo.get("language") for repo in repos if repo.get("language"))
top_lang = langs.most_common(1)[0][0] if langs else "—"

if events:
    last = events[0]
    last_type = (last.get("type") or "Activity").replace("Event", "")
    last_repo = (last.get("repo") or {}).get("name", "—").split("/")[-1]
else:
    last_type = "No public event"
    last_repo = "—"

sync = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

def metric(x, label, value, note, accent):
    return f'''
    <g transform="translate({x} 102)">
      <rect width="242" height="92" rx="20" fill="#0D131C" stroke="#28313E"/>
      <circle cx="24" cy="25" r="5" fill="{accent}" opacity=".9"/>
      <text x="40" y="30" class="mono" font-size="10" fill="#758397">{esc(label)}</text>
      <text x="24" y="64" class="ui" font-size="26" font-weight="700" fill="#EFF3F8">{esc(value)}</text>
      <text x="24" y="82" class="ui" font-size="10" fill="#5F6C7E">{esc(note)}</text>
    </g>
    '''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-label="Live GitHub pulse">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#080B11"/>
      <stop offset="1" stop-color="#0D1118"/>
    </linearGradient>
    <style>
      .ui{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Arial,sans-serif}}
      .mono{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
      @keyframes pulse{{0%,100%{{opacity:.28}}50%{{opacity:1}}}}
      .pulse{{animation:pulse 2.2s ease-in-out infinite}}
    </style>
  </defs>
  <rect width="1200" height="260" rx="30" fill="url(#bg)"/>
  <rect x="1" y="1" width="1198" height="258" rx="29" fill="none" stroke="#252D39"/>

  <circle cx="58" cy="55" r="5" fill="#62E6A7" class="pulse"/>
  <text x="78" y="61" class="ui" font-size="13" fill="#7A8799" letter-spacing="1.5">PUBLIC GITHUB PULSE</text>
  <text x="1138" y="61" text-anchor="end" class="mono" font-size="10" fill="#596677">{esc(sync)}</text>

  {metric(56, "PUBLIC REPOS", profile.get("public_repos", 0), f"top language · {top_lang}", "#6EA8FF")}
  {metric(314, "FOLLOWERS", profile.get("followers", 0), f"{profile.get('following', 0)} following", "#9B7DFF")}
  {metric(572, "STARS / FORKS", f"{stars} / {forks}", "across public owned repos", "#43DEFF")}
  {metric(830, "LAST PUBLIC SIGNAL", last_type, last_repo, "#62E6A7")}

  <text x="56" y="229" class="ui" font-size="11" fill="#566274">Public activity only · private/company work intentionally excluded.</text>
</svg>'''

os.makedirs("assets", exist_ok=True)
with open("assets/pulse.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Updated pulse for {USER}")
