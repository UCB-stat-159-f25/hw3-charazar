# Define variables
SOURCEDIR      = .
BUILDDIR       = _build
ENV_NAME = myst_env
CONDA_BIN = $(shell conda info --base)/bin/conda

# Phony targets: targets that do not correspond to actual files
.PHONY: all html clean

env: environment.yml
	#@echo "Creating or updating Conda environment $(ENV_NAME) from environment.yml..."
	$(CONDA_BIN) env create -f environment.yml --prefix ./$(ENV_NAME) || $(CONDA_BIN) env update -f environment.yml --prefix ./$(ENV_NAME)


html:
	@echo "Building HTML documentation with MyST..."
	myst build --html $(SOURCEDIR) $(BUILDDIR)/html

clean:
	@echo "Cleaning up build directory..."
	rm -rf $(BUILDDIR)
