# Installing this package (MacOS)
To install this package and its dependencies in a new conda environment, simply run:
```shell
conda create -n week3 python=3.8
conda install -n week3 -c conda-forge python-graphviz
conda install -n week3 pytorch torchvision -c pytorch
conda activate week3

(week3) pip install -e cogworks_week3
```

# Installing this package (Windows/Linux)
To install this package and its dependencies in a new conda environment, simply run:
```shell
conda create -n week3 python=3.8 jupyter notebook numpy matplotlib numba scikit-learn nltk
conda install -n week3 -c conda-forge python-graphviz
conda install -n week3 pytorch torchvision cpuponly -c pytorch
conda activate week3

(week3) pip install -e cogworks_week3
```
