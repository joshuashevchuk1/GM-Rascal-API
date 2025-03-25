import asyncio
import logging
import os

from google.auth import default
from google.apps import meet_v2

# Configure logging
logging.basicConfig(level=logging.INFO)

# Ensure authentication is set
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_secret_270393507396-pg5fhh9ko7v7ie2s1drp3jvvv3l64hqo.apps.googleusercontent.com.json"  # Replace with actual path


async def sample_get_conference_record():
    logging.info("Entering sample_get_conference_record")

    # Authenticate and create a client
    credentials, _ = default()
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=credentials)

    # Initialize request argument(s) with a proper conference record name
    request = meet_v2.GetConferenceRecordRequest(
        name="conferenceRecords/your_record_id",  # Replace with actual record ID
    )

    # Make the request
    try:
        response = await client.get_conference_record(request=request)
        print(response)
    except Exception as e:
        logging.error(f"Error fetching conference record: {e}")

    logging.info("Leaving sample_get_conference_record")

asyncio.run(sample_get_conference_record())
