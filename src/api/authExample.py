from google_auth_oauthlib.flow import InstalledAppFlow
from google.apps import meet_v2

SCOPES = ['https://www.googleapis.com/auth/meetings.space.created']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('oauth.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

    client = meet_v2.SpacesServiceClient(credentials=creds)
    request = meet_v2.CreateSpaceRequest()
    response = client.create_space(request=request)
    print(f'Space created: {response.meeting_uri}')

if __name__ == '__main__':
    main()
