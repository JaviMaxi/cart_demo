<h1 align="center">Application Setup</h1>

<h1>Application Setup</h1>
<h2>Instructions:</h2>
<ol>
  <li>Build the Docker containers:</li>
  <pre><code>docker compose build</code></pre>
  <li>Start the Docker containers:</li>
  <pre><code>docker compose up</code></pre>
  <li>Execute the following commands:</li>
  <pre><code>docker container exec -it cart-demo-backend-prod python manage.py migrate</code></pre>
  <pre><code>docker container exec -it cart-demo-backend-prod python manage.py loaddata cart/fixtures/{001_data_cart_categories.json,002_data_cart_articles.json}</code></pre>
  <pre><code>cd cmd</code></pre>
  <pre><code>sh load_backup_media.sh backups/backup_1_media-20230522004922.tar.gz</code></pre>
</ol>
<p>PAge: <code>http://127.0.0.1:8080/home</code></p>
<h2>Admin Access:</h2>
<pre><code>docker container exec -it cart-demo-backend-prod python manage.py createsuperuser</code></pre>
<p>Admin panel: <code>http://127.0.0.1:8080/admin</code></p>
</ul>
<h2>API Testing:</h2>
<p>To test the APIs described in the specifications, you can use the following endpoints:</p>
<ol>
  <li>Create a cart and retrieve the cart ID:</li>
  <p>Endpoint: <code>http://127.0.0.1:8080/v1/cart/create</code></p>
  <p>Request body:</p>
  <pre><code>{
"country": "spain",
"items": [
  {
    "article": {
      "id": 3,
      "name": "Gigabyte AORUS 17",
      "price": "1399.00"
    }
  },
  {
    "article": {
      "id": 4,
      "name": "MSI Katana 15 B12VFK",
      "price": "1099.00"
    }
  }
]
}</code></pre>
<li>Retrieve the contents of a cart by ID:</li>
<p>Endpoint: <code>http://127.0.0.1:8080/v1/cart/?id_cart=1</code></p>
</ol>
<p>Note: Replace <code>127.0.0.1:8080</code> with the appropriate host and port if you are running the application on a different address.</p>
