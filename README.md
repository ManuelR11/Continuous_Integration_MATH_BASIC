# Opción A — Matemática básica (CI con GitHub Actions)

Este repo implementa la librería `math_basic` con 5 funciones: `square`, `factorial`, `is_prime`, `gcd`, `lcm`,
incluye pruebas unitarias con `pytest` y un workflow de CI que corre en cada *pull request*.

## Uso rápido (local)
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Cómo romper un test a propósito
Edita `math_basic/core.py` y cambia la línea `return a * a` de `square` por `return a + a`.
Luego ejecuta:
```bash
pytest -q
```
Verás que fallan tests, demostrando que la CI atraparía el error.
```

## Estructura
```
.
├── math_basic/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_core.py
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md
```
