
# Dropbox API Token Re-Generation

This repository provides Python scripts for integrating with the Dropbox API. It includes tools for obtaining and refreshing OAuth2 tokens.

## Features
- Generate an initial access and refresh token.
- Automatically refresh the access token every 4 hours.

## Setup Instructions

### 1. Prerequisites
- Python 3.x installed on your system.
- A Dropbox App created via [Dropbox Developers](https://www.dropbox.com/developers/apps).

### 2. Configuration
1. Clone the repository:
   ```bash
   git clone https://github.com/nalindaDJ/Dropbox-Developer-API-Token-Re-generate-Python.git
   cd Dropbox-Developer-API-Token-Re-generate-Python
   ```
2. Replace `<YOUR_APP_KEY>` and `<YOUR_APP_SECRET>` in the scripts with your app credentials.

### 3. Usage

#### Regenerate Token
Use the following script to refresh your access token:
```bash
python regenerate_token.py
```

### 4. Automate Token Refresh
To automate token refresh every 4 hours, set up a cron job:
```bash
crontab -e
```
Add the line:
```bash
0 */4 * * * /usr/bin/python3 /path/to/regenerate_token.py
```

### File Descriptions
- `regenerate_token.py`: Script to refresh the access token using the refresh token.
- `newAPI.php`: File where tokens are saved after generation.

---

## License
This project is licensed under the MIT License.
