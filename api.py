from fastapi import FastAPI, File, UploadFile
import ai
app = FastAPI()

@app.post("/aii")
async def upload_image(file: UploadFile = File(...)):
    # Zapisz przesłany plik lokalnie
    file_content = await file.read()

    # Zapisz przesłany plik lokalnie
    file_location = f"uploaded_{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(file_content)
    r = ai.predict2(file_content)
    mess = "kot"
    if r[0] == 0:
        mess="pies"
    return {"filename": file.filename, "message": mess}

# uvicorn api:app --host 127.0.0.2 --port 5001 --reload