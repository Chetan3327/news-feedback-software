from django.shortcuts import render, HttpResponse
from django.conf import settings
from . import tools

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

import pickle
with open(str(settings.BASE_DIR) + '\\news\\trained_models\\positive_negative_neutral_ex.pkl', 'rb') as f:
    MODEL = pickle.load(f)


@api_view(['GET'])
def home(request):
    return HttpResponse("home")

def predict(request):
    input_features = tools.preprocess_statement("hello world")
    predicted_sentiment = MODEL.classify(input_features)
    print("Predicted Sentiment:", predicted_sentiment)
    return HttpResponse("hello")

@api_view(['POST'])
def predict_api(request):
    print(request.data, '========================================================================')
    if(request.method == 'POST'):
        sentence = request.data['sentence']
        print("sentence: ", sentence)
        input_features = tools.preprocess_statement(sentence)
        predicted_sentiment = MODEL.classify(input_features)
        response_data = {
            "sentiment": predicted_sentiment,
        }
        return Response(response_data)

