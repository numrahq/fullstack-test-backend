Here are some of the things I've noticed with the codebase that could have some improvement

# Python

## Private methods

If I understood correctly, Python doesn't have private methods but we can indicate this using the "double underscore prefix" convention.

At this point in time, it seems that the following changes could be done `api/invoice_api.py`'s `approve` and `reject` methods could benefit from that

## Retunrned types

We can enhance the code by explicitly telling which types should be returned by the functions. My IDE was a bit lost on this.

## Error treatment

It's good to have at least one generic way to hook up "catching" errors with an error treatment.

As the business logic progress, specialized catches can be put in place, allowing specialized treaments.

## API configurations are hard-coded (implemented)

Data from the API configuration can be set in a similar fashion that the DB cnfiguration.

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

## Invoice status

There's no way to know which valid status exist at the moment, and how each status changes into another status.

For example, it is not clear at the moment, if it's acceptable to have a rejected invoice to be approved later. Depending on the answer and amount of states, different implementations can be used, from simple if-elses to state machines.

## PDF

If invoice can be of different types, probably we need a way to register metainformation about the uplaoded file

# Testing

## Lack of instructions

The readme lacks instructions to run the tests

## GET does not guarantee mock is being used

If we're goind with unit test, it makes sense for the API's mock to have an assertion to see if the expectation is not hard-coded

## Feedback loop (implemented)

It's time consuming to run tests manually. HGaving the tests run every change motivates people to at least be aware of the state of the codebase

Implemented by installing `pytest-watch`, run with `poetry run ptw`

## Test as documentation

Tho it's technically possible to "change" the returned type for tests, it can be confusing for someone reading the tests as documentation.

In the test for the GET endpoints, both test return an array, which is not what one of the actual endpoints returns. The test still works due to mocks, but might mislead new collaborators.

## Cleanup

In other languages I've worked with, it was a good idea to clear mocks between tests to keep all tests trully isolated.

## Reusage

Tho it's better to isolate code where possible, a tradeoff worth discussing is what could be reused from tests.

For instance, in the API test, there's a lot of initialization code happening over and over again.

# Architecture

## Dependency injection

At the moment, it seems okay to add code dependencies as parameters but as the application grows, it might be better to use some mechanism to inject dependencies in a more decoupled way.

## Dependency rule

Apparently, there are some conventions in Python that would allow us to force which package can use which other package.

This is useful to highlight architecural dependencies, for instance, when following a clean architecure approach internal layers must be ignorante about its most-immediate external layer.

## Separation of concerns

The repository is also updating the domain, instead of just commiting/rejecting changes on the domain. At first this seems a neglible detail but it tends to:

- Create anemic domains: the model become just a "bag of data"
- Leak responsabilities: if the domain doesn't change itself, we break OOP's concept of encapsulation
- Difficulty on enforcing consistency rules: rules about consistent state of the model can be anywhere, making it hard to support the codebase

## Business explicitness

Tho the code gets a bit more complicated, it's nice to be explicit about possible scenarios that might happen. For instance, at the moment, if I call approve and then reject, the latter operation overwrites the first, it's not clear if this is a desired outcome.

The API layer should call either another piece of code that knows how to handle many different scenarios. In some architectures, this is a service or use case layer, where we can write code that is concerned with such things.

The service's code knows each possible valid business variation, which includes blocking invalida scenarios.
