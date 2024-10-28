from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/internal/url/{linkID}/suggestions")
async def get_suggestions(linkID: str):
    return {
        "suggestions": {
            "incoming": [
                {
                    "url_id": "f61600c3-0ed4-4bb5-a83a-152d37bffc5a",
                    "content_id": "content-1",
                    "content": "Learn about caching strategies to boost website performance.",
                    "score": 0.45
                },
                {
                    "url_id": "0ba800ff-2f01-437b-ba1b-13b8a0c503da",
                    "content_id": "content-2",
                    "content": "Firewall security essentials for robust protection.",
                    "score": 0.82
                },
                {
                    "url_id": "371d6409-543f-4ea6-8ca0-81b4549b4fc7",
                    "content_id": "content-3",
                    "content": "Optimize your Shopify store for faster performance.",
                    "score": 0.77
                },
                {
                    "url_id": "b101371d-27e6-4461-a677-0fc3af2eaa18",
                    "content_id": "content-4",
                    "content": "Calculate JSON size efficiently with our guide.",
                    "score": 0.68
                },
                {
                    "url_id": "c5c25055-6461-4a65-8b66-c9cbda9e6579",
                    "content_id": "content-5",
                    "content": "Understanding performance trade-offs with sliders.",
                    "score": 0.71
                }
            ],
            "outgoing": [
                {
                    "url_id": "9088dda5-84a9-4d45-9c65-a7bea0a52a11",
                    "content_id": "content-6",
                    "content": "Overview of RabbitLoader features and benefits.",
                    "score": 0.95
                },
                {
                    "url_id": "3dc8716e-6b07-4a29-9570-2150438922ef",
                    "content_id": "content-7",
                    "content": "Reducing Total Blocking Time effectively.",
                    "score": 0.88
                },
                {
                    "url_id": "fb31f978-5a35-48a2-a755-570ba34c499c",
                    "content_id": "content-8",
                    "content": "Installing RabbitLoader on a Laravel website.",
                    "score": 0.81
                },
                {
                    "url_id": "fe752051-622e-490b-a994-34c53c2be35f",
                    "content_id": "content-9",
                    "content": "Preload fonts to improve load times.",
                    "score": 0.78
                },
                {
                    "url_id": "fd994f9d-f40d-4bb2-be91-62bd975376a8",
                    "content_id": "content-10",
                    "content": "Divi lazy load: optimize loading speeds.",
                    "score": 0.85
                }
            ]
        }
    }
