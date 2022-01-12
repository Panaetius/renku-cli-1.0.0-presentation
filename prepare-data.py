import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from janitor import clean_names
from renku.api import Input

# combine datasets
penguins_1 = pd.read_csv(Input("data/table_219.csv"))
penguins_2 = pd.read_csv(Input("data/table_220.csv"))
penguins_3 = pd.read_csv(Input("data/table_221.csv"))

penguins = pd.concat([penguins_1, penguins_2, penguins_3])

# replace null values
imputer = SimpleImputer(strategy="most_frequent")
penguins.iloc[:, :] = imputer.fit_transform(penguins)

penguins = penguins.pipe(clean_names)

# with pd.option_context('display.max_columns', 4040):
#     print(penguins.describe(include='all'))

penguins["species"] = penguins["species"].map(
    {
        "Adelie Penguin (Pygoscelis adeliae)": "adelie",
        "Gentoo penguin (Pygoscelis papua)": "gentoo",
        "Chinstrap penguin (Pygoscelis antarctica)": "chinstrap",
    }
)

data = penguins[
    ["culmen_length_mm_", "culmen_depth_mm_", "flipper_length_mm_", "body_mass_g_"]
]
target = penguins["species"]

X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.2)

X_train.to_csv("data/X_train")
X_test.to_csv("data/X_test")
Y_train.to_csv("data/Y_train")
Y_test.to_csv("data/Y_test")
