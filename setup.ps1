<#
.SYNOPSIS
    Regenerate the animated dot-matrix portrait used by this GitHub profile.

.EXAMPLE
    .\setup.ps1 -Image .\my-photo.png
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$Image,
    [ValidateSet('dots', 'binary')]
    [string]$Mode = 'dots',
    [int]$Cols = 106,
    [double]$Detail = 0.55,
    [double]$RevealTime = 2.2,
    [double]$RevealFade = 0.35,
    [double]$Duration = 3.8,
    [switch]$NoCircle,
    [switch]$NoAnimate,
    [switch]$NoReveal,
    [switch]$Color,
    [switch]$Invert
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot

$dotArgs = @(
    (Join-Path $root 'scripts\dotify.py'), $Image,
    '-o', (Join-Path $root 'assets\portrait'),
    '--mode', $Mode,
    '--cols', $Cols,
    '--equalize',
    '--detail', $Detail
)

if (-not $NoCircle)  { $dotArgs += '--circle' }
if (-not $NoAnimate) { $dotArgs += @('--animate', '--duration', $Duration) }
if (-not $NoReveal)  { $dotArgs += @('--reveal', '--reveal-time', $RevealTime, '--reveal-fade', $RevealFade) }
if ($Color)           { $dotArgs += '--color' }
if ($Invert)          { $dotArgs += '--invert' }

python @dotArgs
Write-Host "`nPortrait regenerated. Open preview.html to inspect it.`n" -ForegroundColor Green
