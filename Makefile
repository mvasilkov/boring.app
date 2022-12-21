runserver:
	uvicorn boring.app:app --reload

.PHONY: runserver

app:
	uvicorn boring.app:app --workers 1

.PHONY: app
