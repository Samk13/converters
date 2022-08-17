import asyncio
from nasa_controlled_vocabularies.load_data import load_data
from nasa_controlled_vocabularies.write_data import write_data

# row_data = "nasa_voc/nasa_controlled_vocabularies/downloads/thesaurus-CSV.csv"
row_data = "nasa_vocabularies/nasa_controlled_vocabularies/downloads/nasa_test.csv"
# output_file = (
#     "nasa_voc/nasa_controlled_vocabularies/vocabularies/clean_thesaurus_CSV.csv"
# )
# output_file = "nasa_voc/nasa_controlled_vocabularies/vocabularies/nasa_test.csv"


async def main():
    """initiate the app"""
    cleaned_csv = await asyncio.create_task(load_data(row_data))
    await asyncio.create_task(write_data(cleaned_csv))


if __name__ == "__main__":
    asyncio.run(main())
