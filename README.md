# Python Software Society of Uganda

Website for the Python Software Society of Uganda, built with Django 5 and Tailwind CSS 4.

## Prerequisites

- Python 3.10+
- Node.js 18+
- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Setup

### 1. Install Python dependencies

```bash
uv sync
```

### 2. Install Node dependencies

```bash
npm install
```

### 3. Apply database migrations

```bash
uv run python manage.py migrate
```

## Running locally

You need two processes running simultaneously: the Django dev server and the Tailwind CSS watcher.

**Terminal 1 — Django server:**

```bash
uv run python manage.py runserver
```

**Terminal 2 — Tailwind CSS watcher:**

```bash
npm run watch-css
```

The site will be available at `http://127.0.0.1:8000`.

## Building CSS for production

```bash
npm run build-css
```

## Collecting static files (for deployment)

```bash
uv run python manage.py collectstatic
```
