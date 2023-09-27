# CSE111-Project-Pokedex
This was the final project made in order to show proficency in database design and implementation for CSE111-Database systems.

This is a simple GUI pokedex that produces a list of pokemon based off the search peramiters given and the category chosen.

![pokedexp1](https://github.com/scampos37/CSE111-Project-Pokedex/assets/115961998/3bcca8e4-7f13-4c76-acab-490b28f9362d)
This is what you see upon running the application "database.py". In order to begin getting results, a category must be chosen 
from the dropdown menu at the top right (must click button to show dropdown menu). After choosing the category, One must press 
"Use Selected Search" in order to refresh the app and be given the proper prompts for that category.

![pokedexp2](https://github.com/scampos37/CSE111-Project-Pokedex/assets/115961998/81a71c11-4be8-4838-bdf2-1b789e8ad110)
Afer getting the prompts, you must fill out the prompts based off the pokemon you want to search for. Sadly, due to time
constraints at the time of making this project, the answers to the prompts are case sensitive. This means that all answers
must be written with the first letter being capital and the rest lowercase (i.e. "Fire", "Pikachu", "Dark", "Kanto", "Vulpix")

![pokedexp3](https://github.com/scampos37/CSE111-Project-Pokedex/assets/115961998/ea5c6282-8d48-441a-a854-f030621a24e5)
After filling out the prompts, pressing enter will submit the answers to the app and produce a result. All results go up to the 
7th generation and all data was gathered from online sources and can be found in the csv files in the "datasets" folder. 

Inserts, updates, and deletes to the database can also be made through the app. While it is not secure in a normal situation, it 
was a requirement that was needed to be implemented in order to get full points for the app. "Administrator mode" can be accessed
through the app by typing in the password "12345" after selecting a category into the search bar. The terminal will then ask a question
of what you'd like to change. Pressing the number correlated to the action you want to preform will then provide more questions to fill
out if updating or inserting to the database.
