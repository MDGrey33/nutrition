# NutritionAI App(FastAPI)

The Meal Planner app is a FastAPI based application that uses chatgpt to generate meal plans based on user preferences and dietary restrictions. 
The app also allows users to add new personal information, such as their height, weight, and activity level, to create personalized meal plans.

## Technology
The Meal Planner app is built using the following technologies:

- Python 3.11
- fastapi 0.92.0
- pydantic 1.10.5
- uvicorn 0.20.0

## Getting Started
To get started with the Meal Planner app, follow these steps:

Clone the repository to your local machine using the command:

      git clone https://github.com/MDGrey33/nutritionAI.git --branch FastAPI 

Create a virtual environment using Python 3.11:

      python3.11 -m venv envp11

Activate the virtual environment:

      source envp11/bin/activate

Install the required packages by running:

      pip install -r requirements.txt

Start the Uvicorn server by running:

      uvicorn app.main:app --reload

You can now access the app by going to `http://localhost:8000`.

You can now access the api documentation by going to `http://localhost:8000/docs`.

find the postman collection in `NutritionAI fastapi.postman_collection.json` in the root directory.

## Main Functionality

The Meal Planner app has the following main functionality:

- Allows users to add new personal information, such as their height, weight, and activity level, to create personalized meal plans.
### Comming soon
- Uses chatgpt to generate meal plans based on user preferences and dietary restrictions.
- Allows users to generate new meal plans.
- Allows users to generate recipes for the meals in the plans.

## Contributing

We welcome contributions to the Meal Planner app! To contribute, please fork this repository and submit a pull request with your changes.

Here are some areas that we are particularly interested in improving:

- File management and object-oriented programming
- Parallelizing the `generate_recipes` function
- Creating a mobile app to view meals and submit them to health apps
- Implementing Google authentication
- Training the Ada model for use in generating meal plans (instead of relying on the Davinci model)

If you are interested in training the Ada model, please reach out to us for more information on how to get started. Thank you for your interest in the Meal Planner app!

# Todo list

1. split generate recipe into multiple parallel celery tasks
2. Pull file management to one package
3. pull meal from json to object
4. pull meal plan to object
5. pull recipe to object
6. Make mobile app to
   1. Show meals 
   2. Submit to health app
7. Implement google authentication for