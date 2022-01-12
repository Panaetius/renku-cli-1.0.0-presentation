
# Renku CLI 1.0 new features



## Commands

Execute data preprocessing

`renku run python prepare-data.py`

`renku workflow ls`

`git reset --hard HEAD^`

Execute data preprocessing with named Plan

`renku run --name preprocessing python prepare-data.py`

Execute model training

`renku run --name train python train.py --data data/X_train --target data/Y_train --model models/trained_model --gamma 0.1 --c 0.0001`

Evaluate model

`renku run --name evaluation python evaluate_model.py --data data/X_test --target data/Y_test --model models/trained_model --result results.txt --matrix confusion_matrix.png`

Check results

`cat results.txt`

Run whole pipeline again to recreate results.txt

`renku rerun results.txt`

Compare results

`cat results.txt`

Check status of repo

`renku status`

Modify input data

`head -n 150 data/table_219.csv > data/table_219.csv && git add data/table_219.txt && git commit -m "modify source data"`

Check status and update all workflow outputs

`renku status`

`renku update --all`


List all Plans

`renku workflow ls`

Visualize Graph

`renku workflow visualize results.txt`

`renku workflow visualize -i results.txt`

Edit Plans to make them more easily useable

`renku workflow show train`
`renku workflow edit --description "Train a model" --rename-param  data-2=data --rename-param target-3=target --rename-param model-4=model --rename-param gamma-5=gamma --rename-param c-6=c train`

Compose Plans together into combined Plan

`renku workflow compose --link train.model=evaluation.model-4 --map model=train.model --map gamma=train.gamma --map c=train.c pipeline train evaluation`

Execute combined Plan using Toil (achieved the same as `renku rerun`)

`renku workflow execute --provider toil -s gamma=1.4 pipeline`
`renku workflow execute --provider cwltool -s gamma=1.4 pipeline`

Perform many experiments

`renku workflow iterate --provider toil --map gamma=[0.1,0.5,1.0,1.5,2.0] --map c=[0.0001,0.001,0.01,0.1,1,10] --map evaluation.output-5=output/results_{iter_index}.txt --map evaluation.output-6=outputs/confusion_matrix_{iter_index}.png pipeline`