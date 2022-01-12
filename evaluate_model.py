import argparse
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from renku.api import Output
import matplotlib.pyplot as plt


def evaluate_model(data, target, model, result, matrix):
    data = pd.read_csv(data, index_col=0)
    target = pd.read_csv(target, index_col=0)

    with open(model, "rb") as f:
        clf = pickle.load(f)

    prediction = clf.predict(data)

    labels = ["adelie", "chinstrap", "gentoo"]

    conf_matrix = confusion_matrix(target, prediction, labels=labels)
    score = clf.score(data, target)

    with open(result, "w") as f:
        f.write(f"Score: {score}")

    ConfusionMatrixDisplay(conf_matrix, display_labels=labels).plot()
    plt.savefig(matrix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str)
    parser.add_argument("--data", type=str)
    parser.add_argument("--target", type=str)
    parser.add_argument("--result", type=str)
    parser.add_argument("--matrix", type=str)

    args = parser.parse_args()

    evaluate_model(args.data, args.target, args.model, args.result, args.matrix)
