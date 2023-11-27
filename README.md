
# Telegram Keyword Searcher 🤖

This Python script allows you to search for specific keywords within specified Telegram channels. It operates by scanning messages from the last hour and prints out any occurrences of the keywords.

## Getting Started 🚀

### Prerequisites 📋

Before you run the script, you need to have:

- Python 3.x installed on your machine. You can download Python [here](https://www.python.org/downloads/).
- `telethon` and `pytz` libraries installed. You can install these using pip:

  ```shell
  pip3 install -r requirements.txt
  ```

### Setting Up Telegram API 🔑

1. Log in to [Telegram API](https://my.telegram.org) with your phone number.
2. Navigate to 'API development tools' and fill out the form to obtain your `api_id` and `api_hash`.
3. Note down the `api_id` and `api_hash`.

### Configuration ⚙️

1. Open the script in a text editor.
2. Replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_PHONE_NUMBER` with your actual details.
3. Customize the `key_words` list within the script to include the keywords you wish to search for.
4. Add the channel IDs to a file named `channels.txt`, placing one ID per line, prefixed with `-100`.

## Running the Script 🏃‍♂️

To execute the script, use the following command in your terminal:

```shell
python3 telegram_keyword_searcher.py
```

If it's your first time running the script, you will be prompted to enter your phone number and the verification code you receive via Telegram.

## Results 📄

The script will output messages containing the keywords to a file named `telegram_keyword_searcher_results.txt` and log any warnings or errors to `telegram_searcher.log`.

## Automation with Crontab ⏲️

You can schedule the script to run at regular intervals using `crontab` on Unix-based systems.

1. Open your terminal and enter `crontab -e` to edit your crontab file.
2. Add a line that specifies the interval and the command to run the script. You can use [Crontab Generator](https://crontab-generator.org) or if you want it to run in every hour:

   ```shell
   0 * * * * /usr/bin/python3 /path/to/your/telegram_keyword_searcher.py >> /path/to/your/cron.log 2>&1
   ```

   Make sure to replace `/path/to/your/` with the actual path to the script.

3. Save and exit the editor. The `crontab` service will now automatically run your script at the specified times.

## Note 📝

- The search performed by the script is case-insensitive.
- If you need to adjust the time window for message retrieval, modify the `two_hours_ago` variable in the script.

## License 📜

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 👏

- Thanks to the Telethon library for providing the API wrapper.
- All contributors who helped in the development and refinement of this script.
