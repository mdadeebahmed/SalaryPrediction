
# Deploying ML Model using Flask

This is a simple project to demonstrate how to deploy a Machine Learning model using the Flask API.

---

## Prerequisites

You must have the following libraries installed:

- **Scikit-Learn**
- **Pandas** (for the machine learning model)
- **Flask** (for the API)

**Flask version required:** `0.12.2`  
You can install Flask using either of the following:

```
conda install flask=0.12.2
```
**or**
```
pip install Flask==0.12.2
```

---

## Project Structure

This project has four major components:

1. **model.py** – Contains code for the Machine Learning model that predicts employee salaries based on training data in the `hiring.csv` file.

2. **app.py** – Contains Flask APIs that receive employee details through a GUI or API calls, compute the predicted salary using the model, and return it.

3. **templates/** – A folder that contains the HTML template (`index.html`) which allows the user to input employee details and displays the predicted salary.

4. **static/** – A folder that contains the `css/` directory with `style.css`, used for styling the `index.html` page.

---

## Running the Project

1. Make sure you are in the project’s root directory. Then, create the machine learning model by running:

```
python model.py
```

This will create a serialized version of the model named `model.pkl`.

---

2. Start the Flask API by running:

```
python app.py
```

By default, Flask runs on port `5000`.

---

3. Open your browser and navigate to:

```
http://127.0.0.1:5000/
```
**or**
```
http://localhost:5000/
```

You should now see the homepage.

- Enter **valid numerical values** in all three input fields.
- Click **Predict**.

If everything is set up correctly, the **predicted salary** will be displayed on the page!

You can also check the API output directly by visiting:

```
http://127.0.0.1:5000/predict
```
