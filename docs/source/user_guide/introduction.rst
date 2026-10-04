Introduction
============

Judobase is a platform for managing judo competitions, athlete rankings, and tournament data.

Features:

- **Reverse Engineered:** Reverse engineered base Judobase API methods. Access to data on tournaments, athletes, results is available by python classes ``JudokaAPI``, ``CompetitionAPI``, ``ContestAPI``, ``CountryAPI``, ``RatingAPI``.
- **Extension:** Implemented additional methods to the API to make it more user-friendly. Look at ``JudoBase`` class.
- **Pydantic Schemas:** All data is returned as Pydantic models, making it easy to work with.
- **Async:** All requests are asynchronous, allowing for faster data retrieval.
