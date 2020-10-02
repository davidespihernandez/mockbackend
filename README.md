# mockbackend
Mock a backend using FastAPI

# Features

- Allows to create a mocked backend easily
- This can speed up local testing for frontend applications, as you don't need a real backend for testing.
- You'll need the real API documentation to mock the objects and endpoints

# Technology

- FastAPI. A very simple and fast framework
- Uses Python with typing, which makes it more IDE friendly.
- Uses Pydantic models to serialize/deserialize
- Very simple routing system
- Websockets can be done very easily as well

# How to mock an endpoint

- Create the models returned or received by the API using Pydantic BaseModel classes (see models folder)
- Create a list of objects to be retrieved by the detail and list methods (see test_data folder)
- Create the mocker, add other specific methods if needed (see mockers folder)
- Create the router and add it to the main.py file. Add whatever endpoints you need in your router (see routers folder)

# How to execute

There's a docker-compose file in the root folder, that executes the API backend, with hot reloading.
Execute with:

```
docker-compose up --remove-orphans
```

You can also create a virtual environment, install the dependencies in requirements.txt with pip and run it with:

```
uvicorn app.main:app --reload
```

 
