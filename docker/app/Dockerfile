FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

COPY app/ /app/app/
COPY models/ /app/models/
COPY app/config/ /app/config/

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV LOG_STDOUT=true

USER nonroot:nonroot

VOLUME ["/tmp"]

ENTRYPOINT ["python", "-m", "app.api.main"]
