from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
import os
import uvicorn
import sys

app = FastAPI()

@app.get("/{path:path}")
async def serve_file(path: str):
    if path == "" or path.endswith("/"):
        path = os.path.join(path, "index.html")
    file_path = os.path.join("static", path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        return JSONResponse(content={"error": "File not found"}, status_code=404)

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    uvicorn.run(app, host="0.0.0.0", port=port)