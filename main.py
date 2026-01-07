from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI()

HTML = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Send to Console (FastAPI)</title>
</head>
<body>
  <h1>Send data to server console</h1>

  <h2>Form submit (application/x-www-form-urlencoded)</h2>
  <form action="/submit" method="post">
    <label>Name: <input type="text" name="name" /></label><br/>
    <label>Message: <input type="text" name="message" /></label><br/>
    <button type="submit">Send</button>
  </form>

  <hr/>

  <h2>Send JSON via Fetch</h2>
  <input id="jname" placeholder="name" />
  <input id="jmsg" placeholder="message" />
  <button onclick="sendJson()">Send JSON</button>

  <script>
  async function sendJson(){
    const name = document.getElementById('jname').value;
    const message = document.getElementById('jmsg').value;
    const resp = await fetch('/submit-json', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, message })
    });
    const data = await resp.json();
    alert('Server response: ' + JSON.stringify(data));
  }
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def index():
    # Serve the simple HTML page with a form and a fetch example
    return HTML

@app.post("/submit", response_class=HTMLResponse)
async def submit(name: str = Form(...), message: str = Form(None)):
    # This handler receives form-encoded data from the browser form.
    # Print received values to the server console.
    print(f"Received (form) - name: {name!r}, message: {message!r}")
    return HTMLResponse(f"<p>Received. Check server console. name={name}, message={message}</p><p><a href='/'>Back</a></p>")

@app.post("/submit-json")
async def submit_json(request: Request):
    # This handler receives JSON via fetch()
    data = await request.json()
    print(f"Received (json) - {data!r}")
    return JSONResponse({"status": "ok", "received": data})

if __name__ == "__main__":
    # For direct python main.py execution (uvicorn recommended)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
