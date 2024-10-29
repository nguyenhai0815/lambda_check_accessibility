import json
from app.check_service import check_accessibility

def lambda_handler(event, context):
    url = event.get("url")
    
    if not url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "URL is required"})
        }

    try:
        result = check_accessibility(url)
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
    except Exception as e:
        print(f"Exception occurred: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
