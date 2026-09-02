# Animated portrait

The package already includes the portrait as an emerald dot matrix.

Animation layers:

1. **Reveal scan** — rows fade in from top to bottom when the SVG loads.
2. **Shimmer** — dot columns pulse continuously after the reveal.
3. **Circular falloff** — the portrait fades at the edge instead of ending in a hard square.

Palette used by `scripts/dotify.py`:

- dark foreground: `#25C686`
- dark dim: `#0B5A3C`
- light foreground: `#0E7A52`
- light dim: `#A9EBD2`

Regenerate from any local photo with:

```powershell
python scripts\dotify.py .\my-photo.png -o assets\portrait --cols 106 --equalize --detail 0.55 --circle --animate --duration 3.8 --reveal --reveal-time 2.2 --reveal-fade 0.35
```

The original photo is not bundled so pushing this package does not unintentionally publish the full-resolution source image.
