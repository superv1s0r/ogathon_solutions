import requests
#Si se quiere probar, cambiad el puerto
BASE_URL = "http://localhost:8080"

def test_virus():
    params = {"n": 3}  # Ahora n se pasa como parámetro de query
    r = requests.get(f"{BASE_URL}/solution-1", params=params)
    print("Propagación vírica:", r.json())

def test_cifrado():
    params = {"n": 44}  # También como parámetro de query
    r = requests.get(f"{BASE_URL}/solution-2", params=params)
    print("Cifrado por secuencia:", r.json())

def test_reciclaje():
    data = {
        "matrix": [
            [1, 3, 2],
            [2, 1, 3],
            [3, 2, 1]
        ]
    }
    r = requests.post(f"{BASE_URL}/solution-3", json=data)
    print("Reciclaje efectivo:", r.json())

if __name__ == "__main__":
    print("🔎 Ejecutando tests de los 3 endpoints...")
    test_virus()
    test_cifrado()
    test_reciclaje()

