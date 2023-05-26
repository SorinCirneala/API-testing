# API testing with Python

> [First version](#to-do-list-api)
- basic API with just a few actions
- basic requests, response handling, testcases using pytest
- different modules for API actions, locators and testcases

> [Second version](#grocery-store-api)
- more complex API actions (query, path and body parameters, authentication headers)
- clear separation of modules (test data, test cases, actions, configurations)
- uses test parametrization, marks, multiple assert types

## To Do List API

**Test object:** [To Do List](https://todo.pixegami.io)  
**Specification:** [Docs link](https://todo.pixegami.io/docs)  


## Grocery store API
**Test object:** [Simple Grocery API](https://simple-grocery-store-api.glitch.me/)  
**Specification:** [Github link](https://github.com/vdespa/Postman-Complete-Guide-API-Testing/blob/main/simple-grocery-store-api.md)  
**Initial tests done in Postman:** [Postman colection](https://www.postman.com/sorincirneala/workspace/grocery-store-api-public/collection/22316948-500e3a68-8eb1-4b1f-94c5-a97d7812740c?action=share&creator=22316948)  
> To run the tests you need an [access token](https://github.com/vdespa/Postman-Complete-Guide-API-Testing/blob/main/simple-grocery-store-api.md#Register-a-new-API-client). Store it in /utils/secret.py in a string variable ACCESS_TOKEN.

### Discovered issues: 
1. Get product list does not return status 400 or error message when sending a string or boolean as 'results' parameter.
2. Get product by ID response includes a label even if the request is sent with "product-label=false".
3. Get product list with 0 results returns 20 results. 
