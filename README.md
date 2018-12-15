# net-me
###This is a template for the tasks I find myself doing in any job.  The purpose of this repo is to do a quick git pull into my new environment, and get automating.

*I'm making a sandwich while this report is run, or at least trying to.*

1. Clone the repository
    ```
    git clone https://github.com/jumbalaya09/net-me.git
    ```
2. Pip install the requirements
    ```
    pip install -r requirements.txt
    ```
3. Setup a .ini file in the app.py directory.
    ```
    atom .ini
    ```

    At minimum it should look like this:
    ```
    [PROD]
    SECRET_KEY = <key goes here>


    [TEST]
    DEBUG = True
    SECRET_KEY = <key goes here>
    ```

    Be on the lookout for anything that has 'config' in it.   You can add these as you go.

4. Test Test Test.  I haven't written any unit tests, maybe one day.
5. DBs.  I prefer Mongo, I'll add that in the template soon.
6. Logins.  Considering it.
7. Deploy.  I'll add the deployment docs later using nginx, gunicorn, and linux. For now just look at the Digital Ocean docs, even though they are slightly off for CentOS.
8. Certs.  Certbot.
