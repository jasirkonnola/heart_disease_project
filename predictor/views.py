from django.shortcuts import render
from .forms import HeartForm
import joblib
import numpy as np

model = joblib.load("ml/heart_model.pkl")

def predict(request):

    result = None

    if request.method == "POST":

        form = HeartForm(request.POST)

        if form.is_valid():

            data = list(form.cleaned_data.values())

            prediction = model.predict([data])

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