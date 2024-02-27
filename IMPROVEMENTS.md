Here are some of the things I've noticed with the codebase that could have some improvement

# Python

## Private methods

If I understood correctly, Python doesn't have private methods but we can indicate this using the "double underscore prefix" convention.

At this point in time, it seems that the following changes could be done `api/invoice_api.py`'s `approve` and `reject` methods could benefit from that

## Retunrned types

We can enhance the code by explicitly telling which types should be returned by the functions. My IDE was a bit lost on this.

# RESTful API

When going for REST apis it's a common practice to follow the RESTfull conventions. I don't know if this was the intention here, but if it was, there are some possible improvements.

Having the API RESTfull is convenient to have other developers onboard more quickly, and using a standard.

## Excplicit separation of GETs

The GET endpoint for returning a single specific invoice uses a query string, which

- is not according to the conventions
- differes from the other similar endpoints on the project

So it seems having the following endpoints would be better

- `GET /invoices`
- `GET /invoices/{id}`

## Lack of PATCH

At the moment, it's not clear why a POST was used for accepting the invoice and a DELETE was used for reject it. Both endpoints are just changing the status of the invoice, and therefore should be a PATCH, unless there are some business reason like `POST /invoices/{id}/approval` would create an "approval entity" which is not yet on code.

## Uniform response

Some people like normalize the API's responses, always returning an object. So the callers can process metainformation, like errors in a more standarized way.

```json
{
  "data": [] | {} | null,
  "error": {} | null
}
```

Having a standard allows for generalization.

# Docker

## Docker startup

According to the README, `docker compose up -d` should start the app but it doesn't because the volume `docker/postgres/dumps` is missing. People who don't have experince with docker might find a bit difficult to understand this.

We can:

- change the readme to tell devs to create those folders before start the containers
- `docker/postgres/dumps/.gitkeep` to be able to commit an "empty" folder structure

## Dockerizing everything

Python could have been set into docker, will all of its necessary files to run the app from the get go. No need for devs to set up the environment.

# Data modeling

## Autoincrement

It seems that setting autoincrement on the invoice makes sense

## Invoice Structure

Is it safe to assume an invoice always have those same data? Like, is it a world-wide standard?

# Testing

The readme lacks instructions to run the tests

## GET does not guarantee mock is being used

If we're goind with unit test, it makes sense for the API's mock to have an assertion to see if the expectation is not hard-coded

# Architecture

## Dependency injection

At the moment, it seems okay to add code dependencies as parameters but as the application grows, it might be better to use some mechanism to inject dependencies in a more decoupled way.

## Dependency rule

Apparently, there are some conventions in Python that would allow us to force which package can use which other package.

This is useful to highlight architecural dependencies, for instance, when following a clean architecure approach internal layers must be ignorante about its most-immediate external layer.
