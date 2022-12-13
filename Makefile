create_env:
	conda env create --file environment.yml

update_env:
	conda env update --file environment.yml --prune
