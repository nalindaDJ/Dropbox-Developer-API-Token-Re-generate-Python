<insert regenerate_toimport requests
import re

# Dropbox App credentials
APP_KEY = "Your Key"
APP_SECRET = "Your Secret"
REFRESH_TOKEN = "Your refresh token"

# Dropbox API endpoint for token renewal
TOKEN_URL = "https://api.dropbox.com/oauth2/token"

# Path to the PHP configuration file
PHP_FILE_PATH = "newAPI.php"

def renew_access_token():
    """
    Renews the Dropbox access token using the refresh token.
    """
    try:
        # Request payload
        payload = {
            "refresh_token": REFRESH_TOKEN,
            "grant_type": "refresh_token",
            "client_id": APP_KEY,
            "client_secret": APP_SECRET
        }

        # Make the POST request to refresh the token
        response = requests.post(TOKEN_URL, data=payload)

        if response.status_code == 200:
            data = response.json()
            access_token = data.get("access_token")
            print(f"Access token renewed successfully: {access_token}")
            update_php_file(access_token)
        else:
            print(f"Failed to renew access token: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred while renewing the access token: {e}")

def update_php_file(new_token):
    """
    Updates the DROPBOX_TOKEN in the PHP configuration file.
    """
    try:
        with open(PHP_FILE_PATH, "r") as file:
            content = file.read()

        # Replace the current token with the new one
        updated_content = re.sub(
            r'define\("DROPBOX_TOKEN", ".*?"\);',
            f'define("DROPBOX_TOKEN", "{new_token}");',
            content
        )

        with open(PHP_FILE_PATH, "w") as file:
            file.write(updated_content)

        print("PHP file updated successfully with the new access token.")
    except Exception as e:
        print(f"Failed to update the PHP file: {e}")
        raise

if __name__ == "__main__":
    renew_access_token()
