# Raksha Kar Maa - AI Road Safety Predictior
# Train.py - Model Training File
print("Jai Maa - Training Shuru Ho Rahi Hai")


import pandas as pd
import numpy as np
from sklearn.model_selection imprt train_test_split
from sklearn.preprocessing imprt StandardScaler
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.models import sequential
from tensorflow.keras.layers imprt Dense, Dropout
import pickle

print("Data Taiyaar Kar Rahe Hain...")
data = {
    'speed': np.random.randint(20, 120, 1000),
    'weather': np.random.randint(0, 3, 1000), # 0=Clear, 1=Rain, 2=Fog
    'time-of-day': np.random.randint(0, 24, 1000),
    'driver_age': np.random.randint(18, 70, 1000),
    'road_type': np.random.randint(0, 2, 1000), # 0=Highway, 1=City
    'alcohol_level': np.random.uniform(0, 0.1, 1000)
}


# Risk Calculate Kar Rahe Hain - Simple Logic
df['risk'] = 0
df.loc[(df['speed'] > 80) | (df['weather'] == 1) | (df['alcohol_level'] > 0.03),'risk'] = 1
X = df.drop('risk', axis=1)
Y = df['risk']


# 2. Data Ko Split Kar Rahe Hain

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, TEST_SIZE=0.2,RANDOM_STATE=42)


# 3. Data Ko Scale Kar Rahe Hain
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Scaler Save Kar Lo - App.py Me Kaam Aayega
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
    print("Scaler Save Ho Gaya: scaler.pkl")


    #4. AI Model Bana Rahe Hain -Maa Kaa Dimaag
    print("AI Model Bana Rahe Hain...")
    model = Sequential([
        Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.2),
        Dense(16, activation='relu'),Dropout(0.2),
        Dropout(0.2)
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
                  
    #5. Model ko Train Kar Rahe Hain
    print(" Training Chalu Hai...2-3 Minute Lagega...")
    model.fit(X_train, Y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)


    # 6. Model Test Kar Rahe Hain
    loss, accuracy = model.evaluate(X_test, Y_test) 
    print(f"Model Accuracy: {accuracy*100:.2f}%")


    #.7 Model Save Kar Rahe Hain
    model.save('road_safety_model.h5')
    import pickle
    pickle.dump(scaler , open('scaler.pkl', 'wb')) # scaler save karo
    
    print("JAI MAA - MODEL SAVE HO GAYA: road_safety_model.h5")
    print("ab 'py app.py' Chala ke Server Start Karo")
    
}