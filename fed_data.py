import os
from dotenv import load_dotenv
from fredapi import Fred

'''Fred APIS works well, but they don't have actual annoucmnets it seems like so I just fetched
the unemployment rate to test it. Actual text announcments need a different method

Found this https://github.com/vtasca/fed-statement-scraping instead. Has a dataset for us named communactions.csv.
Have not checked the quality of it. 
'''

def create_client():
    load_dotenv()
    api_key = os.getenv("FED")
    if not api_key:
        raise ValueError("No key was found")
    return Fred(api_key=api_key)



def fetch_data(client, series_id, start_date=None, end_date=None):
    return client.get_series(
        series_id,
        obs_start=start_date,
        obs_end=end_date
    )


def main():
    client = create_client()
    data = fetch_data(client,series_id= "UNRATE", start_date= "2024-01-01", end_date="2024-12-31" )
    print(data)

if __name__ == "__main__":
    main()



