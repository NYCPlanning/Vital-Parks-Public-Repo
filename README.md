# Vital Parks Public Repository

This repository serves as an example code base to compute travel analysis that powers the the NYC Parks [Vital Parks Explorer](https://www.nycgovparks.org/about/vital-parks/explorer). This repository does **not** include the data visualization but we hope to in the future. It encompasses:

- **Data Ingestion**: Integrates park elements, walkable street data, MTA travel data, Census population data, and other relevant geospatial datasets
- **NetworkX Graph Construction**: Stitch together a walking and transit network
- **Time Travel Analysis**: Computes travel times from park elements to the nearest network node

For more details on the underlying data and processes, visit our [wiki](https://github.com/NYC-Parks/Vital-Parks-Public-Repo/wiki).

# Project Setup Guide 

Coming soon! 

<!--
This project assumes you have [Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install), [Jupyter](https://anaconda.org/anaconda/jupyter), and [Git](https://git-scm.com/downloads) installed. 

## One-Time Setup (Initial Installation)

These steps are only required once to set up the environment.

### 1. Clone the Repository

To clone the repository, run the following command in your **Git Bash**:
```
git clone https://github.com/NYC-Parks/Vital-Parks-Public-Repo.git
```

### 2. Create the conda environment

> [!NOTE]
> The following steps will take place in **Anaconda Prompt**.

To create the conda environment from the yml file to a specified path, open **Anaconda Prompt** and run the following command:
```
conda env create -f E:\path\to\envName.yml --prefix C:path\to\env
```

To create the conda environment from file to a name (it will install the environment in the default location), run the following command:
```
conda env create -f E:\path\to\envName.yml --name YOURENVNAME
```

### 3. Install a kernel for Jupyter notebook for your new environment

To install ipykernel (just once), run: 
```
conda install ipykernel
```

To create new environment kernel for jupyter notebook, run: 
```
ipython kernel install --name=YOURENVNAME
```

For more information about jupyter notebooks and kernels, visit [this link](https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874/).

## Usage (After Setup is Complete)

Once installed, follow these steps each time you run the project.

### 1. Activate your environment

In **Anaconda Prompt**, to activate your environment:

```
conda activate YOURENVNAME
```

### 2. Run the Jupyter notebook.

To run analysis, open Jupyter notebook in the base directory. This will open up a new window.

```
jupyter notebook
```

Set the kernel YOURENVNAME on the top right of the Jupyter notebook page, next to JupyterLab. 

## After usage

### 1. Deactivate your environment

```
conda deactivate YOURENVNAME
```






