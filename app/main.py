from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from .export import generate_publications_excel

app = FastAPI(title="Faculty Research Portal API")

# Allow frontend access
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return {"status": "Portal backend running"}


@app.get("/export/publications")
def export_publications():
    buffer = generate_publications_excel()

    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=publications_master.xlsx"
        },
    )
