import requests


# Download the profile picture
def download_pfp(pfp_url, save_path):
    try:
        img_data = requests.get(pfp_url).content
        with open(save_path, 'wb') as handler:
            handler.write(img_data)

        return save_path
    except Exception as e:
        print(f"Failed to download pfp: {e}")
        return None
