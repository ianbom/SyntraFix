param(
    [string]$Hostname = "ragas_syntrafix@%h",
    [string]$LogLevel = "info"
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$PythonExe = Join-Path $ProjectRoot "venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $PythonExe)) {
    throw "Project virtualenv Python not found: $PythonExe"
}

Set-Location $ProjectRoot


Write-Host "Using Python: $PythonExe"
& $PythonExe -c "import sys; print(sys.executable); from datasets import Dataset; from ragas import evaluate; from langchain_ollama import ChatOllama, OllamaEmbeddings; print('RAGAS dependencies OK')"

& $PythonExe -m celery -A app.celery_app.celery_app worker -Q ragas_evaluation --loglevel=$LogLevel --pool=solo --hostname=$Hostname
