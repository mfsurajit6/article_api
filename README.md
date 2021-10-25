# Article API

The goal of this project is to design api endpoints of a simple blog web stites and protect the routes using custom authentication.

---
## Specification

- Python 3.8.10
- DjagoRestFramework

## End Points

- **POST** /user/signup/ - need name, email, password to register a user
- **POST** /user/signin/ - need email, password to authenticate the a user and returns a token.
- **GET** /user/profile/ - need Authorization token in the header like, Token authorizationtoken to get the user's profile
- **PUT** /user/profile/ - need Authorization token in the header like, Token authorizationtoken to update the user's profile
- **DELETE** /user/profile/ - need Authorization token in the header like, Token authorizationtoken to delete the user's profile
- **POST** /user/logout/ - need Authorization token in the header like, Token authorizationtoken to logout a user

- **POST** - /article/add/ - need Authorization token in the header like, Token authorizationtoken, title and description in the body to add an article
- **POST** - /article/ - to retrive all the available article
- **POST** - /article/<id>/ - to retrive a specific article
- **POST** - /article/update/<id>/ - need Authorization token in the header like, Token authorizationtoken, title and description in the body to update an article
- **POST** - /article/delete/<id>/ - need Authorization token in the header like, Token authorizationtoken, title and description in the body to delete an article




## Contributors

- Fahad Mohd Sahid
- Udit Das
- Surajit Das