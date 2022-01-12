import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import pickle


def train_model(data, target, model, gamma, c):
    data = pd.read_csv(data, index_col=0)
    target = pd.read_csv(target, index_col=0)

    clf = make_pipeline(
        StandardScaler(),
        SVC(kernel="linear", gamma=gamma, C=c),
    )
    clf = clf.fit(data, target)

    with open(model, "wb") as f:
        pickle.dump(clf, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str)
    parser.add_argument("--target", type=str)
    parser.add_argument("--model", type=str)
    parser.add_argument("--gamma", type=float)
    parser.add_argument("--c", type=float)

    args = parser.parse_args()

    train_model(args.data, args.target, args.model, args.gamma, args.c)
