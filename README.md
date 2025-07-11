# bsidespgh25

[![CI](https://github.com/jonzeolla/bsidespgh25/actions/workflows/commit.yml/badge.svg)](https://github.com/jonzeolla/bsidespgh25/actions/workflows/commit.yml)

Welcome to bsidespgh25 - Let's ✨vibe✨ with cybersecurity-themed ASCII art!

## Features

- **Vibe Generator**: Generate random cybersecurity-themed ASCII art and motivational messages
- **Multiple Art Styles**: Choose from patterns, matrix-style displays, or cyber word art
- **Continuous Mode**: Keep the vibes flowing with automatic generation
- **Statistics Tracking**: Monitor your vibe generation sessions

## Getting Started

First, you need to ensure you have `brew`, `task`, `docker`, `git`, and `uv` installed locally, and the `docker` daemon is running.

Then, you can setup your local environment via:

```bash
# Install the dependencies
task init

# Build the image
task build

# Run the image
docker run jonzeolla/bsidespgh25:0.2.0 --help
```

## Usage

### Generate a Single Vibe

```bash
# Generate a random vibe
python src/main.py --vibe

# Generate a specific type of vibe
python src/main.py --vibe --vibe-type matrix
python src/main.py --vibe --vibe-type pattern
python src/main.py --vibe --vibe-type word
```

### Continuous Vibe Mode

```bash
# Generate vibes continuously (press Ctrl+C to stop)
python src/main.py --vibe --continuous

# Adjust the delay between vibes (default: 2 seconds)
python src/main.py --vibe --continuous --delay 5.0
```

### View Statistics

```bash
# See vibe generator statistics
python src/main.py --stats
```

### Docker Usage

```bash
# Generate a vibe using Docker
docker run jonzeolla/bsidespgh25:0.2.0 --vibe

# Run in continuous mode
docker run -it jonzeolla/bsidespgh25:0.1.0 --vibe --continuous
```

If you'd like to build all of the supported docker images, you can set the `PLATFORM` env var to `all` like this:

```bash
PLATFORM=all task build
```

You can also specify a single platform of either `linux/arm64` or `linux/amd64`

## Optional setup

If you'd like to be able to run `task license-check` locally, you will need to install `grant` and ensure it's in your `PATH`.

## Troubleshooting

If you're troubleshooting the results of any of the tasks, you can add `-v` to enable debug `task` logging, for instance:

```bash
task -v build
```

## Automated Dependency Management

This project is configured with automated dependency management:

- **Dependabot**: Automatically creates pull requests for Python, GitHub Actions, and Docker dependency updates
- **Renovate**: Provides more advanced dependency update management with grouping and scheduling capabilities

Both tools are pre-configured and will start working once the repository is pushed to GitHub.

## FAQs

For frequently asked questions including release workflow troubleshooting, see our [FAQ documentation](./FAQ.md).

_This project was generated with 🤟 by [Zenable](https://zenable.io)_
