# ITB Directory Scraper

This Python script scrapes information from the [Institut Teknologi Bandung (ITB)](https://www.itb.ac.id) directory and saves it to a CSV file. It uses the BeautifulSoup library to parse the HTML content of the directory pages.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- requests
- beautifulsoup4
- csv

You can install them using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Set the following constants at the beginning of the script to configure your scraping session:

    - `BASE_URL`: The base URL of the ITB directory.
    - `TIMEOUT`: The timeout for making HTTP requests.
    - `HEADERS`: User-Agent headers for the HTTP requests.

2. Run the script by executing the following command:

    ```bash
    python itb_directory_scraper.py
    ```

The script will scrape data from the ITB directory for each letter of the alphabet and save it to a CSV file named `data_directory_itb.csv`. The CSV file will contain the following columns:

- Nama (Name)
- URL
- Alamat (Address)
- Kode Pos (Postal Code)
- Telepon (Phone Number)
- Fax
- Email

## Functions

- `extract_text(element)`: Extracts and cleans text from an HTML element.

- `extract_url(element)`: Extracts the URL from an HTML element.

- `extract_info(section)`: Extracts education, research, publication, and books information from an HTML section.

- `extract_address(section)`: Extracts and parses the address information from an HTML section.

- `write_csv(filename, data)`: Writes data to a CSV file with the specified filename.

- `main()`: The main function that orchestrates the scraping process.

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
