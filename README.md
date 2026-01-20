Project: Little Lemon Capstone - Backend API

Testable API Endpoints:

1. Menu API
   - GET: http://127.0.0.1:8000/api/menu/
   - POST: http://127.0.0.1:8000/api/menu/
   - PUT: http://127.0.0.1:8000/api/menu/<id>/
   - DELETE: http://127.0.0.1:8000/api/menu/<id>/

2. Booking API
   - GET/POST: http://127.0.0.1:8000/restaurant/booking/tables/

3. Authentication (Djoser)
   - Register: http://127.0.0.1:8000/auth/users/
   - Login (Token): http://127.0.0.1:8000/auth/token/login/
   - Logout (Token): http://127.0.0.1:8000/auth/token/logout/

4. Auth Token Endpoint
   - POST: http://127.0.0.1:8000/api-token-auth/

Instructions:

- Use Bearer Token for authentication in Insomnia.
- Create a user via `/auth/users/`, then obtain token from `/auth/token/login/`.

Database:

- Connected to MySQL (configured in `settings.py`).

Frontend:

- Visit home at `http://127.0.0.1:8000/restaurant/` for static content.
