import cv2
import mysql.connector
import json
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

def conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="Maba@@22", 
        database="dane_obrazu",
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )
    
    return conn

def przetworz_obraz2(obraz):
    nparr = np.frombuffer(obraz, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    frame_resized = cv2.resize(frame, (128,128))
    return frame_resized

def add2(obraz,a):
    con = conn()
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS obrazy (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cechy LONGTEXT,
        etykieta INT
        )
    ''')
    
    cechy_json = json.dumps(przetworz_obraz2(obraz).tolist())
    sql = "INSERT INTO obrazy (cechy, etykieta) VALUES (%s, %s)"
    cursor.execute(sql, (cechy_json, a))
    con.commit()
    con.close()
    
def przetworz_obraz(obraz):
    frame_resized = cv2.resize(obraz, (128,128))
    return frame_resized

def add(obraz,a):
    con = conn()
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS obrazy (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cechy LONGTEXT,
        etykieta INT
        )
    ''')
    
    cechy_json = json.dumps(przetworz_obraz(obraz).tolist())
    sql = "INSERT INTO obrazy (cechy, etykieta) VALUES (%s, %s)"
    cursor.execute(sql, (cechy_json, a))
    con.commit()
    con.close()

def train():
    con = conn()
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS obrazy (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cechy LONGTEXT,
        etykieta INT
        )
    ''')
    cursor.execute("SELECT * FROM obrazy ORDER BY etykieta")
    fetchall = cursor.fetchall()
    obrazy = []
    etykiety = []

    for i in fetchall:
        obrazy.append(np.array(json.loads(i[1])))
        etykiety.append(i[2]-1)
    con.close()
    print("wczytano obrazy!")
    obrazy = np.array(obrazy)
    obrazy = obrazy.reshape(obrazy.shape[0], -1)
    etykiety = np.array(etykiety)
    X_train, _, y_train, _ = train_test_split(obrazy, etykiety, test_size=0.1, random_state=42)
    print("Przetworzone obrazy!")
    model = xgb.XGBClassifier(learning_rate=0.001)
    model.fit(X_train, y_train)
    joblib.dump(model, 'model_xgboost.pkl')
    print("skończone")

def predict2(obraz):
    model = joblib.load('model_xgboost.pkl')
    return model.predict(przetworz_obraz2(obraz).reshape(1, -1))

def predict(obraz):
    model = joblib.load('model_xgboost.pkl')
    return model.predict(przetworz_obraz(obraz).reshape(1,-1))
