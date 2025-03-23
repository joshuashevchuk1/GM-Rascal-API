import asyncio

from google.apps import meet_v2


async def sample_get_conference_record():
    print('hello')
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.GetConferenceRecordRequest(
        name="meet.google.com/gse-useg-nta",
    )

    # Make the request
    response = await client.get_conference_record(request=request)

    # Handle the response
    print(response)

asyncio.run(sample_get_conference_record())