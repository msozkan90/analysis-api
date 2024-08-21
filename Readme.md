# Python Analysis Api

## Installation

- Clone the project on your local device with using github repository link

### Create Virtual Environment
#### Go to project location
```bash
cd core
```
#### Windows
```bash
python -m venv env

.\env\Scripts\activate

```

#### Linux / MacOS
```bash
python3 -m venv env

source env/bin/activate
```

### Install requirements.txt

```python
pip install -r requirements.txt
```

### Rename .env.example to .env
```bash
mv .env.example .env
```

### Apply Migrations and Run the Server
```python
python manage.py runserver # start the project on port localhost:8000
```

## Endpoints
http://localhost:8000/api/conversion-rate/

- Returns the conversion rate for each customer_id, along with the highest and lowest conversion rates.

http://localhost:8000/api/status-distribution/

- Provides a summary of the distribution of status across different types and categories. This should include total revenue and conversions for each status.

http://localhost:8000/api/category-type-performance/

- Returns the total revenue and conversions grouped by category and type. It should also highlight the top-performing category and type combination.

http://localhost:8000/api/filtered-aggregation/

- Exposes aggregated data for rows where type is CONVERSION, returning the average revenue and conversions per customer_id.