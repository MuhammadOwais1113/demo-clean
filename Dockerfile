FROM python:3.12.7-slim@sha256:60d9996b6a8a3689d36db740b49f4327be3be09a21122bd02fb8895abb38b50d

RUN useradd --create-home --uid 10001 appuser

WORKDIR /app

COPY requirements.lock pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -r requirements.lock \
    && pip install --no-cache-dir --no-deps .

USER appuser

CMD ["python", "-m", "demo_clean.cli", "1", "2", "3"]
