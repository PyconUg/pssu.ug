# Contributing to PSSU Website

A Django project scaffold with Tailwind CSS for the Python Software Society of Uganda (PSSU).

## Project Structure

```
pssu.ug/
├── core/                    # Django project settings
├── website/                 # Main Django app
├── templates/               # HTML templates
├── static/                  # Static assets
│   ├── css/
│   └── vendor/
├── site.json               # Site configuration
├── tailwind.config.js      # Tailwind configuration
├── pyproject.toml          # Python dependencies
├── package.json            # Node dependencies
└── contributing.md         # This file
```

## Setup

1. Install `uv` if needed:
   ```bash
   pip install uv
   ```
2. Install Python dependencies with `uv`:
   ```bash
   uv install
   ```
3. Install frontend dependencies:
   ```bash
   npm install
   ```
4. Build Tailwind CSS:
   ```bash
   npm run build-css
   ```
5. Run migrations:
   ```bash
   uv run python manage.py migrate
   ```
6. Start the development server:
   ```bash
   uv run python manage.py runserver
   ```

## Development

### CSS Development
- `npm run watch-css` - Watch for CSS changes and rebuild automatically
- `npm run build-css` - Build CSS once

### Site Configuration
Site settings are managed in `site.json`. Key configurations include:
- Site phase (coming_soon, active, archived)
- Contact information
- Feature flags
- Social media links

### Design System
The site uses a custom Tailwind configuration with PSSU brand colors:
- Blue: Primary brand color
- Green: Success/accent color
- Yellow: Warning/accent color

## Tailwind

- `npm run build-css` builds CSS to `static/vendor/main.css`
- `npm run watch-css` watches for changes and rebuilds automatically