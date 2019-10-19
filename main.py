import json

def extract(filename):
    f = open(filename)
    data = f.read()
    f.close()

    data = json.loads(data)
    return data

if __name__ == "__main__":
    results = extract(filename="data.txt")
    for result in results:
        print(result)