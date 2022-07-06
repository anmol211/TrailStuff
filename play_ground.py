import pickle
import pandas as pd

from sklearn.preprocessing import MultiLabelBinarizer

df = pd.DataFrame(columns=['labels'])
df = df.append([{"labels": ["w2"]},
                {"labels": ["eoi"]},
                {"labels": ["paystubs"]},
                {"labels": ["bank statements"]}
                ],
               ignore_index=True)
labels = df.pop('labels')
print(labels)
mlb = MultiLabelBinarizer()
labels = mlb.fit_transform(labels)
classes = mlb.classes_

with open("/home/userd136/Downloads/model_1112022/files/50ff25c7-0212-4665-85dd-a0470c126582-v1/document_classifier_classes_mortgage-internal-v1.txt", 'wb+') as file_class:
    pickle.dump(classes, file_class, protocol=pickle.HIGHEST_PROTOCOL)

with open("/home/userd136/Downloads/model_1112022/files/50ff25c7-0212-4665-85dd-a0470c126582-v1/document_classifier_classes_mortgage-internal-v1.txt", 'rb') as classes:
    classes = pickle.load(classes)

print(classes)
