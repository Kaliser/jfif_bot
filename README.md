# JFIF to JPG Discord Bot
A very small bot useful for converting your Twitter images (or other source of jfif files...) to jpgs viewable in discord.

## Prerequisites

- **Python 3.8** or higher
- **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications).
- **Enabled permissions** for your bot.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/kaliser/jfif_bot.git
    cd jfif_bot
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Make config file**:
    - Create a `config.ini` file in the root directory of the project.
    - Add your Discord Bot Token to the `config.ini` file:
        ```
        [discord]
        token = TOKEN_HERE
        prefix = !

        ;prefixes aren't used in the bot but may be helpful if you want to add commands
        ```

4. **Run the bot**:
    ```sh
    python client.py
    ```