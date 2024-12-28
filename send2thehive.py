import sys
import requests
import json

def send_to_thehive(title, description, severity, tags, data):
    hive_host = "thehive URL"  
    hive_apikey = "thehive apikey "        

    # Data of alert
    alert = {
        "title": title,
        "description": description,
        "type": "external",
	    "source": "ElastAlert",
	    "sourceRef": "ElastAlert",
        "severity": severity,  # security: 1 (High), 2 (Medium), 3 (Low)
        "tags": tags,
        "artifacts": [
            {
                "dataType": "ip",  # Data type (ip, domain, url,...)
                "data": data,
                "message": "Event detected in logs."
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {hive_apikey}",
        "Content-Type": "application/json"
    }

    try:
        # send POST request to TheHive
        response = requests.post(f"{hive_host}/api/alert", headers=headers, json=alert)
        if response.status_code == 201:
            print("Alert sent thehive successfully!")
        else:
            print(f"Failed to send alert: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    title = sys.argv[1]
    description = sys.argv[2]
    severity = int(sys.argv[3])
    tags = sys.argv[4].split(",")
    data = sys.argv[5]

    send_to_thehive(title, description, severity, tags, data)