# KNOW-ROX
Knowledge-based framework for robot ontology-based explanations.


### Python3 virtual environment configuration and dependencies

In the repository, we already provide a virtual environment but it was built for our computer and it will probably not work in yours. You can easily delete it and create and configure your own environment executing the following commands in a terminal (note that python3-venv needs to bee installed).

```
cd <know_rox_folder>/python_environment
python3 -m venv know_rox_venv
source know_rox_venv/bin/activate

python3 -m pip install pandas ollama pydantic-ai
```

It is also necessary to install the python modules included in the source folder. 

```
cd <know_rox_folder>

python3 -m pip install .
```

It is also possible to install them in 'editable' (development) mode if you want to make some modifications in those modules. 

```
cd <know_rox_folder>

python3 -m pip install -e .
```


### Downloading files from an external github repository (explanatory_narratives_cra)
In order to avoid creating a duplicate of the logical rules to compare planes formalized and implemented in [explanatory_narratives_cra](https://github.com/albertoOA/explanatory_narratives_cra), ***know-rox*** includes a script to download and update the pertinent files. It is possible to program a github action to download them regularly, but for now it will be a manual process. Note that it is necessary to have subversion (svn) installed before running the script. 

```
cd <know_rox_folder>
chmod +x scripts/sh/update_shared_files_ontology_based_narratives.sh 
./scripts/sh/update_shared_files_ontology_based_narratives.sh
``` 