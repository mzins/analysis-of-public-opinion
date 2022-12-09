import glob
import json

import pandas as pd
from statsmodels.stats.inter_rater import fleiss_kappa


def build_agreement_df(label_set, directory):
    iaa = []

    for file in glob.glob(f'{directory}*.json'):
        with open(file, 'r') as f:
            annot_data = json.load(f)
            for x in annot_data:
                annotations = x.get("annotations")

                counts = {label:0 for label in label_set}

                for annotation in annotations:
                    content = annotation.get("annotationData").get("content")
                    label = json.loads(content).get("crowd-classifier").get("label")
                    counts[label] += 1

                iaa.append(list(counts.values()))

    return pd.DataFrame(iaa)

opinion_labels = ["NEUTRAL support","FOR student loan forgiveness ","AGAINST student loan forgiveness","cannot judge support"]

opinion_df = build_agreement_df(opinion_labels, "annotations/opinion/")
opinion_df.to_csv("annotations/opinion/opinion_agreement_matrix.csv")
opinion_fk = fleiss_kappa(opinion_df, method='fleiss')


ego_labels = ["Somewhat important","Very important","Not important at all","cannot judge importance" ]

ego_df = build_agreement_df(ego_labels, "annotations/ego-involvement/")
ego_df.to_csv("annotations/ego-involvement/ego_involvement_agreement_matrix.csv")
ego_fk = fleiss_kappa(ego_df, method='fleiss')

print(f"Opinion Fleiss Kappa: {opinion_fk}")
print(f"Ego Involvement Fleiss Kappa: {ego_fk}")
