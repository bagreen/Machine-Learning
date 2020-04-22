import keras

def load_data():
    # loads data from cifar10 dataset
    (X_train_full, y_train_full), (X_test, y_test) = keras.datasets.cifar10.load_data()

    # need to normalize the RGB values
    X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

    # establish class names to be classified under (10 total)
    class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

    # prints the classification of image 42, kept this here in case you wanted to check how I answered question 2
    #print(class_names[int(y_train[41])])

    return X_train, X_valid, y_train, y_valid


def build_model():
    # create sequential model (simplest keras model)
    model = keras.models.Sequential()
    
    # convolutional layers
    model.add(keras.layers.Conv2D(25, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(keras.layers.Conv2D(25, (3, 3), activation='relu'))

    # pooling layer
    model.add(keras.layers.MaxPooling2D((2, 2)))
    
    # final convolutional layer
    model.add(keras.layers.Conv2D(25, (3, 3), activation='relu'))

    # final pooling layer
    model.add(keras.layers.MaxPooling2D((2, 2)))

    # flatten layer
    model.add(keras.layers.Flatten())

    # dense layer
    model.add(keras.layers.Dense(500, activation='relu'))

    # softmax layer
    model.add(keras.layers.Dense(10, activation='softmax'))

    # optimizer to use, found sgd works best
    optimizer = 'sgd'

    # compile the model with data
    model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    return model


def main():
    # gets values and builds model
    X_train, X_valid, y_train, y_valid = load_data()    
    model = build_model()

    # atempts to fit model with data
    history = model.fit(X_train, y_train, epochs=50, validation_data=(X_valid, y_valid))


if __name__ == '__main__':
    main()
