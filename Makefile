define USAGE
Commands:
	serve     Run the app
endef

export USAGE
help:
	@echo "$$USAGE"

serve:
	poetry run streamlit run main.py