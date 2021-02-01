# Django React Template

## Known Issues

- For some reason, `django-configurations` is temperamental. Sometimes it will load `.env` values correctly and other times it will not. Further investigation is needed; in the meantime, use `os.getenv('value')` and any necessary post-processing of the resulting string in order to populate values which MUST be set.

## Setup

1. Create `config/.env` and fill out the fields listed in `config.env.example`
2. Run `pip install -r requirements.txt` or, with `pip-tools installed`, `pip-compile && pip install -r requirements.txt`
3. Run `yarn install`
4. Run `python manage.py migrate` to set up initial database

## Running

For development on localhost, run each of the following commands in a separate terminal.
    
1. `nwb serve --no-vendor`
2. `python manage.py runserver`

If you have configured everything correctly, you should see each command complete and notify you
that the project is ready to be viewed. To see your app, open the Django url in your browser (default: `localhost:8000`).


## Development

### Backend

Since we are not changing anything about how Django works with this project setup, development of views, API routes, and
other backend logic remains the same as in a vanilla Django project.

#### Models

`django-react-template` comes with one model already created -- a base model which records the timestamp of a model, and
an inherited user. It is highly recommended that you build atop this paradigm rather than reject it, but if you have
strong feelings to the contrary you should delete `migrations/0001_initial.py` and create your own database models
before running `python manage.py makemigrations` and then your first `python manage.py migrate`.

### Adding a new React component

In this paradigm, React components are compiled and injected into the standard Django template. This means we can take 
advantage of the built-in templating functionality of Django and, with a bit of elbow grease, use the power of React to
make those templates responsive.

`django-react-loader` uses the same basic pattern for any component:

1. First, ensure that the library is loaded in your template: `{% load django_react_components %}`
2. Next, ensure that you have rendered the React runtime bundle: `{% render_bundle 'runtime' %}`
3. Finally, load your React component on the page. `{% react_component 'Home' id='home' %}`
    - You can add any number of props as named keywords, e.g. `{% react_component 'Home' id='home' prop1=value_from_context %}`
    

### Other Notes

- If you use `nwb serve` in your local development environment, you may see a persistent XHR error in the console -- a 
request by the app to some variation of `http://localhost:8000/sockjs-node/info?t=some-number`. This is normal and will 
  not appear on production or otherwise affect the function of your app. It is an artifact of the context bending we are
  doing by placing a React component outside the context of its expected Node environment.

## Building

To prepare the application for deployment, run `nwb build --no-vendor`. This will generate a `webpack_bundles` folder
in your `/static` folder populated with the compiled React components. You may now deploy the app as you would any standard
Django application. 

### Deployment Gotchas

1. Note that calling `nwb build` does not remove existing compiled data from your static folder -- it may be worth deleting
`/static/webpack_bundles` before running a build for a deploy, as otherwise your package may become heavier than it
needs to be.
   - If you find that the number of files collected by `python manage.py collectstatic` continues to grow, this may be
    a sign that you should consider deleting the generated files and the `staticfiles` directory and starting with a
     fresh `python manage.py collectstatic`
