# Setup — Pedrinscrk Profile Extreme

## 1. Upload the files

Use the GitHub profile repository:

`Pedrinscrk/Pedrinscrk`

Copy everything from this package into the repository root, preserving folders.

```text
Pedrinscrk/
├─ README.md
├─ SETUP.md
├─ assets/
│  ├─ hero.svg
│  ├─ architecture.svg
│  ├─ orbit.svg
│  ├─ pulse.svg
│  └─ mark.svg
├─ scripts/
│  └─ update_pulse.py
└─ .github/
   └─ workflows/
      ├─ pulse.yml
      └─ snake.yml
```

If the old `.github/workflows/blank.yml` is unused, delete it.
Replace the old empty `snake.yml` with this package's version.

## 2. Enable GitHub Actions writes

Repository:

**Settings → Actions → General → Workflow permissions**

Choose:

**Read and write permissions**

Save.

## 3. Run Live Pulse once

**Actions → Update profile pulse → Run workflow**

The workflow regenerates `assets/pulse.svg` from public GitHub data.
It refreshes every 6 hours.

## 4. Run contribution motion once

**Actions → Generate contribution motion → Run workflow**

This creates an `output` branch with the light/dark contribution animations referenced by the README.

## 5. Company logo

For now, the company stays discreet as text:

`current · Grupo Flamboyan`

When you have the official logo, add:

`assets/flamboyan-logo.png`

Do not recreate or approximate the corporate logo.

## 6. Photo

This version prioritizes the custom visual system.
If you later want a premium portrait, add:

`assets/avatar-premium.png`

## 7. Confidentiality

The case studies are intentionally generalized.
Do not expose private repo links, credentials, internal endpoints, environment variables,
database object names or sensitive architecture in the public profile.

## Troubleshooting

### Live Pulse gets 403 while pushing
Check:

**Settings → Actions → General → Workflow permissions → Read and write permissions**

Then rerun.

### Snake is broken
Run the snake workflow manually once and verify that the `output` branch exists.

### Animation looks static in a Markdown preview
Some preview tools freeze SVG animation.
Test on the actual GitHub profile page.
