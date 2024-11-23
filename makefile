
PYTHON = python
PROGRAM = li.py

.DEFAULT_GOAL := run


run:
	@echo "Running the program..."
	@$(PYTHON) $(PROGRAM)

clean:
	@echo "Cleaning up..."
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -exec rm -f {} +
	@echo "Cleanup complete."

help:
	@echo "Available targets:"
	@echo "  run     - Run the main program"
	@echo "  clean   - Clean up the workspace"
	@echo "  help    - Display this help message"


.PHONY: run clean help
