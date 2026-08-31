import os
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, roc_curve
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__, static_folder='static', static_url_path='/static')

df = None
le = LabelEncoder()

def load_data():
    global df
    if df is None:
        df = pd.read_csv('mushrooms.csv')
        for col in df.columns:
            df[col] = le.fit_transform(df[col])
    return df

@app.route('/')
def index():
    return send_from_directory('static', 'ml-dashboard.html')

@app.route('/train', methods=['POST'])
def train():
    data = request.json
    classifier = data.get('classifier', 'SVM')
    params = data.get('params', {})
    df = load_data()
    X = df.drop(columns=['type'])
    y = df['type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    if classifier == 'SVM':
        model = SVC(C=params.get('C', 1.0), kernel='rbf', gamma='scale')
    elif classifier == 'Logistic Regression':
        model = LogisticRegression(C=params.get('C', 1.0), max_iter=params.get('max_iter', 100))
    else:
        model = RandomForestClassifier(n_estimators=params.get('n_estimators', 100), max_depth=params.get('max_depth', 5), bootstrap=params.get('bootstrap', True), n_jobs=-1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='binary')
    rec = recall_score(y_test, y_pred, average='binary')
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(4,3))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.set_title('Confusion Matrix')
    plt.colorbar(im)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    cm_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    if hasattr(model, 'predict_proba'):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = model.decision_function(X_test)
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    fig, ax = plt.subplots(figsize=(4,3))
    ax.plot(fpr, tpr, color='darkorange', lw=2)
    ax.plot([0,1],[0,1], color='navy', lw=1, linestyle='--')
    ax.set_title('ROC Curve')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    roc_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    # Get raw data preview (first 10 rows, encoded as HTML)
    raw_preview = df.head(10).to_html(classes='dataframe', header="true", border=0)

    return jsonify({
        'accuracy': round(acc, 4),
        'precision': round(prec, 4),
        'recall': round(rec, 4),
        'confusion_matrix_image': f'data:image/png;base64,{cm_b64}',
        'roc_image': f'data:image/png;base64,{roc_b64}',
        'sample_count': len(df),
        'raw_data': raw_preview
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
