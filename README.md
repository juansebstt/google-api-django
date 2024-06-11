<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Google Maps API Integration with Django</h1>

<p>This Django project leverages Google APIs for secure form submission, interactive maps, and multi-stop route optimization. The following APIs are used:</p>

<ol>
    <li><strong>Maps JavaScript API</strong>: Enables the display of interactive maps.</li>
    <li><strong>Places API</strong>: Provides detailed information about places.</li>
    <li><strong>Directions API</strong>: Calculates directions between locations.</li>
    <li><strong>Geocoding API</strong>: Converts addresses into geographic coordinates.</li>
    <li><strong>Distance Matrix API</strong>: Computes travel distance and time for multiple origins and destinations.</li>
    <li><strong>Elevation API</strong>: Provides elevation data for any point on the Earth's surface.</li>
</ol>

<p>Additionally, the project integrates the reCAPTCHA API for enhanced security.</p>

<h2>Requirements</h2>

<p>Ensure you have the following dependencies installed:</p>

<pre>
asgiref==3.8.1
certifi==2024.6.2
charset-normalizer==3.3.2
Django==5.0.6
django-recaptcha==4.0.0
humanfriendly==10.0
idna==3.7
pyreadline3==3.4.1
requests==2.32.3
sqlparse==0.5.0
tzdata==2024.1
urllib3==2.2.1
</pre>

<h2>Installation</h2>

<ol>
    <li>Clone this repository to your local machine.</li>
    <code>git clone https://github.com/your_username/your_project.git</code>
    <li>Install the required dependencies using pip.</li>
    <code>pip install -r requirements.txt</code>
    <li>Set up your Django project and configure the necessary settings.</li>
</ol>

<h2>Usage</h2>

<ol>
    <li>Obtain API keys for Google Maps APIs and reCAPTCHA from the Google Cloud Console.</li>
    <li>Configure your Django settings with the obtained API keys.</li>
    <li>Integrate the desired Google Maps functionality into your Django project using the provided APIs.</li>
    <li>Secure your forms using reCAPTCHA for protection against spam and abuse.</li>
</ol>

<h2>Contributing</h2>

<p>Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature/new-feature</code>).</li>
    <li>Make your changes.</li>
    <li>Commit your changes (<code>git commit -am 'Add new feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/new-feature</code>).</li>
    <li>Create a new Pull Request.</li>
</ol>


</body>
</html>

Don't forget to activate the following Google API's:

reCAPTURE Places API Maps Javascript API Directions API Distance Matrix API Geocoding API.

And configure your API keys with your API information in the settings.py file:

GOOGLE_API_KEY = ""

RECAPTCHA_PUBLIC_KEY = ""

RECAPTCHA_PRIVATE_KEY = ""

Then run

<pre>
Python manage.py makemigrations
</pre>

To finally
<pre>
Python manage.py runserver - On your localhost
</pre>


