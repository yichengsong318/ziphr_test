- create virtualenv
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

- run the app
    python manage.py runserver

- http://localhost:8000/api/ for calculating fuel consumption
    use json data for the post request body
    ex: 
    {
        "data": [
            {"id": 3, "passenger": 56}, 
            {"id": 5, "passenger": 14}, 
            {"id": 6, "passenger": 18}, 
            {"id": 8, "passenger": 30}, 
            {"id": 12, "passenger": 65}, 
            {"id": 32, "passenger": 21}, 
            {"id": 15, "passenger": 16}, 
            {"id": 18, "passenger": 45}, 
            {"id": 14, "passenger": 12}, 
            {"id": 17, "passenger": 18}
        ]
    }

- to test api
    python manage.py test