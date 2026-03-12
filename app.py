from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
import warnings
import os


warnings.filterwarnings('ignore')

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Exact feature order as used during training (matches scaler.feature_names_in_ and model.feature_names_in_)
FEATURE_ORDER = [
    'nottingham_prognostic_index',
    'tumor_size',
    'lymph_nodes_examined_positive',
    'chemotherapy',
    'hormone_therapy',
    'neoplasm_histologic_grade',
    'radio_therapy',
    'age_at_diagnosis',
    'er_status',
    'her2_status',
    'inferred_menopausal_state',
    'aurka'
]

ER_MAP   = {'Positive': 1, 'Negative': 0}
HER2_MAP = {'Positive': 1, 'Negative': 0}
MENO_MAP = {'Post': 1,     'Pre': 0}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/healthcheck')
def healthcheck():
    return jsonify({
        'status': 'ok',
        'model': type(model).__name__,
        'classes': model.classes_.tolist()
    })


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Build a dict of numeric feature values
        feature_dict = {
            'nottingham_prognostic_index': float(data['nottingham_prognostic_index']),
            'tumor_size':                  float(data['tumor_size']),
            'lymph_nodes_examined_positive': float(data['lymph_nodes_examined_positive']),
            'chemotherapy':                int(data['chemotherapy']),
            'hormone_therapy':             int(data['hormone_therapy']),
            'neoplasm_histologic_grade':   float(data['neoplasm_histologic_grade']),
            'radio_therapy':               int(data['radio_therapy']),
            'age_at_diagnosis':            float(data['age_at_diagnosis']),
            'er_status':                   ER_MAP[data['er_status']],
            'her2_status':                 HER2_MAP[data['her2_status']],
            'inferred_menopausal_state':   MENO_MAP[data['inferred_menopausal_state']],
            'aurka':                       float(data['aurka']),
        }

        # Build a DataFrame with named columns so sklearn doesn't raise feature-name warnings
        df_input = pd.DataFrame([feature_dict], columns=FEATURE_ORDER)

        # BUG FIX: RandomForest was trained on UNSCALED data in the notebook!
        # Do not apply scaler.transform() here.
        prediction      = model.predict(df_input)[0]
        probabilities   = model.predict_proba(df_input)[0]

        classes  = model.classes_.tolist()
        prob_dict = {str(int(cls)): float(prob) for cls, prob in zip(classes, probabilities)}

        return jsonify({
            'success':       True,
            'prediction':    str(int(prediction)),
            'probabilities': prob_dict,
            'confidence':    float(max(probabilities)) * 100
        })

    except KeyError as e:
        return jsonify({'success': False, 'error': f'Missing field: {e}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
