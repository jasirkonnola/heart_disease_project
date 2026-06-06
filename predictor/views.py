from django.shortcuts import render
from django.conf import settings
from .forms import HeartForm
import joblib
import os
import pandas as pd

# Load model using settings.BASE_DIR for robust absolute path resolution
model_path = os.path.join(settings.BASE_DIR, "ml", "heart_model.pkl")
model = joblib.load(model_path)

def predict(request):

    result = None

    if request.method == "POST":

        form = HeartForm(request.POST)

        if form.is_valid():

            # Map the 11 submitted form fields to the 20 features expected by the model
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            cp = form.cleaned_data['cp']
            trestbps = form.cleaned_data['trestbps']
            chol = form.cleaned_data['chol']
            fbs = form.cleaned_data['fbs']
            restecg = form.cleaned_data['restecg']
            thalach = form.cleaned_data['thalach']
            exang = form.cleaned_data['exang']
            oldpeak = form.cleaned_data['oldpeak']
            slope = form.cleaned_data['slope']

            feature_dict = {
                'Age': [age],
                'RestingBP': [trestbps],
                'Cholesterol': [chol],
                'FastingBS': [fbs],
                'MaxHR': [thalach],
                'Oldpeak': [oldpeak],
                'Sex_F': [1 if sex == 0 else 0],
                'Sex_M': [1 if sex == 1 else 0],
                'ChestPainType_ASY': [1 if cp == 3 else 0],
                'ChestPainType_ATA': [1 if cp == 1 else 0],
                'ChestPainType_NAP': [1 if cp == 2 else 0],
                'ChestPainType_TA': [1 if cp == 0 else 0],
                'RestingECG_LVH': [1 if restecg == 2 else 0],
                'RestingECG_Normal': [1 if restecg == 0 else 0],
                'RestingECG_ST': [1 if restecg == 1 else 0],
                'ExerciseAngina_N': [1 if exang == 0 else 0],
                'ExerciseAngina_Y': [1 if exang == 1 else 0],
                'ST_Slope_Down': [1 if slope == 2 else 0],
                'ST_Slope_Flat': [1 if slope == 1 else 0],
                'ST_Slope_Up': [1 if slope == 0 else 0],
            }

            input_df = pd.DataFrame(feature_dict)
            prediction = model.predict(input_df)

            if prediction[0] == 1:
                result = "Heart Disease Detected"
            else:
                result = "No Heart Disease"

    else:
        form = HeartForm()

    return render(
        request,
        "predictor/predict.html",
        {"form": form, "result": result}
    )