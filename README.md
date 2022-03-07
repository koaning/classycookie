# classycookie

Effectively this project just kickstarts a spaCy project with some
scikit-learn benchmarks around. The assumption is that there is a 
`data.csv` file in the `assets` folder. This project takes everything
from there. 

## Assumptions

We assume that there is a `data.csv` file in the `assets` folder. This
file needs to have one column named `"text"` and another one named `"label"`. 
It can also contain an optional column called `"set"` which can contain
either the value `"valid"` and `"train"`. 

