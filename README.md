# fullstack-test:backend
> Backend component of the Take Home Test for fullstack candidates to Autonifai

## What is this repo?
This repo is a backend starter project for Autonifai's Take Home Test. 
 It exposes HTTP endpoints to be consumed by the frontend app.

## Endpoints
- `/invoices`: exposes information about invoices contained in the DB 
- TBD

## What are you required to do?
- implement the logic to expose an invoice's PDF file from an Amazon S3 bucket for the frontend to consume 
- implement respective automated tests
- **(optional, bonus points)** identify points of improvement to the existing codebase

## Running this repo locally

### Requirements:
- Docker
- Python 3.11
- Poetry

### Running the project

**Step 1**: spin up Postgres using Docker
```commandline
docker compose up -d
```

**Step 2**: configure environment variables
- create a file called `.env` in the root of your local project
- copy the constants from `.env.example`
- apply the applicable values from `docker-compose.yml` into the newly created `.env` file

**Step 3**: create & populate DB tables
- run the SQL files contained in the `sql` folder

**Step 4**: start the project
```commandline
poetry shell
poetry run python fullstack_test/run.py
```

**Step 5**: test whether the endpoints are returning data
```commandline
curl http://localhost:8000/invoices
```

If everything is alright, the response should be something like this:
```commandline
[{"due_date":"2024-01-23T17:04:54.953206+00:00","po_number":null,"number":"INV-123","payment_terms":30,"description":"x2 MacBook Pro","discount":0.0,"total_amount":16000.0,"gl_code":"EQ12","status":"TO_BE_REVIEWED","id":1,"issued_date":"2024-01-23T17:04:54.953206+00:00","line_item_details":"x2 MacBook Pro","pre_tax_amount":14000.0,"tax_amount":2000.0,"currency":"EUR","cost_centre":"Equipment"}]%
```

# Questions & troubleshooting
If you need support with the repo or have any questions, please reach out to your recruiter. We'll get back to you ASAP.