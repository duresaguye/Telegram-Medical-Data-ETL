# Ethiopian Medical Data Warehouse API

This is the API for the Ethiopian Medical Data Warehouse project. It is built using FastAPI and SQLAlchemy.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd ethiopian-medical-data-warehouse/api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python
    >>> from main import models, engine
    >>> models.Base.metadata.create_all(bind=engine)
    >>> print("Tables created successfully!")
    ```

## Running the API

To run the API, use the following command:
```bash
uvicorn main:app --reload
```

## API Endpoints

### Get all detection results
- **URL:** `/detections`
- **Method:** `GET`
- **Response:** `list[DetectionSchema]`

### Create a new detection
- **URL:** `/detections`
- **Method:** `POST`
- **Request Body:** `DetectionSchema`
- **Response:** `DetectionSchema`

## Project Structure

```
/home/dura/Codes/ethiopian-medical-data-warehouse/api/
├── main.py
├── crud.py
├── models.py
├── database.py
├── schemas.py
└── README.md
```

## License

This project is licensed under the MIT License.