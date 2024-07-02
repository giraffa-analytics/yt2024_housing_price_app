from domain.domain import ApiRequest, ApiResponse
import pickle
import sklearn
import pandas as pd

class PriceEstimator:
    def __init__(self):
        self.path_to_model = "models/lr_apartment_price_predictor.pkl"
        self.prediction_model = self.load_prediction_model()

    def load_prediction_model(self):
        with open (self.path_to_model, 'rb') as f:
            model = pickle.load(f)
        return model

    def preprocess_input(self, request: ApiRequest):
        m2 = request.size
        year = request.year_built
        bath = request.bathrooms
        # Data
        data = {"const":1.0, "size":m2, "year_built":year, "bathrooms":bath}
        # Convert the dictionary to DataFrame
        input_data = pd.DataFrame.from_dict([data])
        # Add constant
        return input_data

    def predict_price(self, request: ApiRequest) -> ApiResponse:
        input_data = self.preprocess_input(request)
        predicted_price = self.prediction_model.predict(input_data)
        predicted_price = round(predicted_price.values[0],0)

        # Format the returned result
        response = ApiResponse
        response.price = predicted_price
        return response