def getEmailTemplate(data):
  return """\
    <html>
      <head>
        <style>
          .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            box-sizing: border-box;
          }
          .header {
            background-color: #f5f5f5;
            padding: 10px;
            text-align: center;
          }
          .content {
            padding: 20px;
            background-color: #f5f5f5;
          }
          .footer {
            background-color: #f5f5f5;
            padding: 10px;
            text-align: center;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <h1>Notificación</h1>
          </div>
          <div class="content">
            <h2>{title}</h2>
            <p>{summary}</p>
            <img src="{url_image}" alt="image" style="width: 100%; height: auto;">
          </div>
          <div class="footer">
            <p>Gracias por leer</p>
          </div>
        </div>
      </body>
    </html>
    """.format(**data)