param(
    [switch]$Detached
)

$ErrorActionPreference = "Stop"
$env:DOCKER_BUILDKIT = "0"
$env:COMPOSE_DOCKER_CLI_BUILD = "0"

if ($Detached) {
    docker compose up --build -d
} else {
    docker compose up --build
}
