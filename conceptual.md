### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python can be used for various tasks while JavaScript is usually used for web development. Smaller differences include Python uses indentation while JavaScript uses curly braces.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  You can use an "if" statement to check if the key exists before accessing it, and you can use the "Get" statement with a default value to retrieve the missing key safely.

- What is a unit test?
Testing individual code components in isolation to ensure they work as intended.

- What is an integration test?
Testing how multiple components work together to verify system functionality.

- What is the role of web application framework, like Flask?
Web app development helps to stramline routing, requests, and provides tools to help build out web applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  You'd use route URL parameters for essential data in the URL and query parameters for optional data or filtering.

- How do you collect data from a URL placeholder parameter using Flask?
By defining it in the route function's argument.

- How do you collect data from the query string using Flask?
request.args.get()

- How do you collect data from the body of the request using Flask?
request.form.get()

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small data piece stored in a user's browser, usually used for session managament, personalization, analytics, and other uses.

- What is the session object in Flask?
Stores user-specific data across requests, like user sessions or settings.

- What does Flask's `jsonify()` do?
Converts Python data into JSON format for easy JSON responses in web applications.
