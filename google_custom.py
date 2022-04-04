from googleapiclient.discovery import build
import gspread
import constants as const

class GoogleCustom:
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        api_key: str = None,
        credentials_filename: str = None,
        authorized_user_filename: str = None,
    ):
        self.api_name = api_name
        self.api_version = api_version
        self.api_key = api_key
        self.credentials_filename = credentials_filename
        self.authorized_user_filename = authorized_user_filename

    def construct_youtube_instance(self):
        try:
            service = build(self.api_name, self.api_version, developerKey=self.api_key)
            print("Youtube API Service Created.")
            return service
        except Exception as e:
            print(e)
            return None
        
    def construct_sheets_instance(self):
        try:
            service = gspread.oauth(
                credentials_filename = self.credentials_filename,
                authorized_user_filename = self.authorized_user_filename
            )
            print("Google Sheets API Service Created.")
            return service
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    #youtube
    google_custom_yt = GoogleCustom(const.API_NAME, const.API_VERSION, const.API_KEY)
    yt_service = google_custom_yt.construct_youtube_instance()

    # Google Sheets
    google_custom_sheets = GoogleCustom(
        credentials_filename = const.CREDENTIALS_FILENAME,
        authorized_user_filename = const.AUTHORIZED_USER_FILENAME
    )
    sheets_service = google_custom_sheets.construct_sheets_instance()