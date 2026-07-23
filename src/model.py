from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv1D,
    MaxPooling1D,
    LSTM,
    Dense,
    Dropout,
    Input
)

def build_model():

    model = Sequential([
        Input(shape=(78, 1)),

        Conv1D(
            filters=64,
            kernel_size=3,
            activation="relu"
        ),

        MaxPooling1D(pool_size=2),
        Dropout(0.2),
        LSTM(64),
        Dropout(0.2),
        Dense(32, activation="relu"),
        Dense(1, activation="sigmoid")

    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model

if __name__ == "__main__":
    model = build_model()
    model.summary()