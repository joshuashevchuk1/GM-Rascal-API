from google.oauth2 import service_account
from google.apps import meet_v2
from google.api_core.client_options import ClientOptions
import asyncio

async def get_conference_records():
    credentials = service_account.Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/meetings.space.readonly"],
        admin="joshua.shevchuk@ookla.com"
    )

    client = meet_v2.ConferenceRecordsServiceAsyncClient(
        credentials=credentials,
        client_options=ClientOptions(api_endpoint="https://meet.googleapis.com")
    )

    request = meet_v2.ListConferenceRecordsRequest()

    response = await client.list_conference_records(request=request)

    async for record in response:
        print(record)

asyncio.run(get_conference_records())
