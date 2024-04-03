# python-sqlmodel

This app uses a local postgres database. Before running the app, you need to create the database with the name `sqlmodel_dev`.

```
DATABASE_URL=postgresql://<user>:<pass>@localhost/sqlmodel_dev uvicorn main:app --reload
```
