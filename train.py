import sys
import os
import src.data_utils
import src.model_utils

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python train.py data/listings.csv.gz")
        sys.exit(1)

    data_path = sys.argv[1]
    df = data_utils.load_data(data_path)

    # clean
    df = df[(df["price"] > 0) & (df["price"] < 1000)]
    df = df[["price", "minimum_nights", "number_of_reviews", "availability_365", "room_type"]]

    model, meta = model_utils.train_model(df)
    print("Model trained. Metadata:", meta)
