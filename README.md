# fantasyhelper
This script enables you to automate changes to your Yahoo fantasy team.

First you need to create a Yahoo API key [here](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).

In step I.2, click the link that says "create an application".
-Type in an application name and description. You can use a random URL for the Homepage URL and redirect URI sections.
-Under "API Permissions", check the "Fantasy Sports" box and select "Read/Write".

Once the app is created, save the Consumer Key and Consumer Secret values.
Paste these values between their respective quotes in the oauth2.json file.

For the code to work:

-Run the script from Terminal/Command Prompt and log into your Yahoo account through the OAuth process (it will take you to Yahoo automatically).

-Find your league ID in square brackets on your Terminal/Command Prompt console. Copy it to the lg object in the Python script.

From there, play around with the different functions! You can view your team in the console (this will help find player numbers), add, drop, and waiver players.
You can also schedule this to run late at night to beat your friends to the waiver wire.

Enjoy!
