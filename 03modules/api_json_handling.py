import json, requests

# url="https://www.boredapi.com/api/activity"

def main():
    res = requests.get("https://randomuser.me/api")
    # print(res.status_code)   
    data = json.loads(res.text) 
    print(data['results'][0]['emailcl'])
    print("type of text: ", type(data))


if __name__ == "__main__":
    main()