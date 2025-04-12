from google.oauth2 import service_account
from google.apps import meet_v2
from google.api_core.client_options import ClientOptions
import asyncio

async def get_conference_records():
    credentials = service_account.Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/meetings.space.readonly"]
    )

    client = meet_v2.ConferenceRecordsServiceAsyncClient(
        credentials=credentials,
        client_options=ClientOptions(api_endpoint="https://meet.googleapis.com")
    )

    request = meet_v2.GetTranscriptRequest(
        name="aeo-gmnj-wck"
    )

    response = await client.get_transcript(request=request)

    async for record in response:
        print(record)

asyncio.run(get_conference_records())
