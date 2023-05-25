# Learning API testing with Python - My Journey

> [First version](#to-do-list-api)
- based on tutorials
- basic API with just a few actions
- getting used to making requests and handling the responses
- uses a basic design pattern to separate the code
> [Second version](#grocery-store-api)
- my own work, after self research
- more complex API actions (query, path and body parameters, authentication headers)
- completely separated the configuration, actions and tests
- work is still in progress

> Future plans:
- write more tests, organize them in test suites
- document bugs based on executed tests
- implement using test data (run same test with different inputs)
- implement test runner and execute suites on schedule
- implement reports

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