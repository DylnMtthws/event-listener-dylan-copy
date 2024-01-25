# Event Listener - Phase 4 Full-Stack Application 

<img width="1440" alt="Screenshot 2024-01-25 at 12 13 03 PM" src="https://github.com/DylnMtthws/event-listener-dylan-copy/assets/128760869/f8d50b34-fb6b-4ca5-a7b8-8cc7c5b614ea">

<img width="1439" alt="Screenshot 2024-01-25 at 12 13 19 PM" src="https://github.com/DylnMtthws/event-listener-dylan-copy/assets/128760869/c21f22f0-5f36-4f96-a17b-9795c858c3b4">

<img width="1439" alt="Screenshot 2024-01-25 at 12 13 55 PM" src="https://github.com/DylnMtthws/event-listener-dylan-copy/assets/128760869/f6cd9b53-e358-45da-a98d-d6254a8c1460">

<img width="1439" alt="Screenshot 2024-01-25 at 12 13 55 PM" src="https://github.com/DylnMtthws/event-listener-dylan-copy/assets/128760869/15035a5e-a16f-44cb-bdab-35f5dd14de43">

---

## Introduction

Event Listener is a volunteer management application designed to streamline the process of tracking volunteers and events for non-profit organizations. It empowers admins to:

Manage volunteers: Add, edit, view, and search volunteer information efficiently.
Organize events: Create, update, and manage details for upcoming events.
Track signups: Seamless coordination of volunteer participation in events.
Visualize relationships: Get insights into volunteer engagement and event coverage through clear visualizations of relationships between volunteers, events, and signups.
Explore OOP and complex table relationships: The application showcases the implementation of object-oriented programming (OOP) principles and the effective management of multi-table relationships in a database, serving as a valuable learning tool for developers.




## Setup

### `server/`

The `server/` directory contains all of the backend code.

To download the dependencies for the backend server, run:

```console
pipenv install
pipenv shell
```

Run the Flask API on [`localhost:5555`](http://localhost:5555) by
running:

```console
python server/app.py
```

Check that your server serves the default route `http://localhost:5555`. You
should see a web page with the heading "Project Server".

### `client/`

The `client/` directory contains all of the frontend code. The file
`package.json` has been configured with common React application dependencies,
include `react-router-dom`. The file also sets the `proxy` field to forward
requests to `"http://localhost:5555". Feel free to change this to another port-
just remember to configure the Flask app to use another port as well!

To download the dependencies for the frontend client, run:

```console
npm install --prefix client
```

You can run your React app on [`localhost:3000`](http://localhost:3000) by
running:

```sh
npm start --prefix client
```

Check that your the React client displays a default page
`http://localhost:3000`. You should see a web page with the heading "Project
Client".
