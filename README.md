# genshin-plus
Simple script for claiming your daily check-in rewards on hoyolab through the use of TheSadru's genshin API wrapper and launching the Genshin Impact game. Currently only built for the "overseas" Americas server.
 
# Requirements
- Python 3.x (if compiling yourself)
- Pip (if compiling yourself)

# Installation and Setup
- IF COMPILING YOURSELF
- (Recommended: Setup a virtual environment through your ide)
- pip install -r requirements.txt
- Run claim_dailies.py once and then set your cookies and gamepath. Documentation for finding your genshin cookies can be found here: https://thesadru.github.io/genshin.py/authentication/
- Use pyinstaller --onefile -w claim_dailies.py to compile to executable to run
- IF USING EXE
- Run the exe, a genshin_config.json file should be created
- Enter your genshin exe gamepath (Should be entered with double backslashes instead of single to bypass escape)
- Enter ltuid_v2 and ltoken_v2, found on the official genshin daily check-in page in developer tools, under the application tab --> cookies --> https://act.hoyolab.com --> ltuid_v2 and ltoken_v2

# Run
- Simply run the claim_dailies.exe file.
