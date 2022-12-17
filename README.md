# Image-gen-B

A tool to generate images from natural language input from humans

## endpoints

endpoint: /api/generate_image

please do send data in form data not in json

form data: "audio_path":path

expected response

{
    "image_link": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-pE0mDunGnei3Y98Fo82KYJLU/user-dicu1xGmToJwolJcrQOYBmAk/img-R7rWUTPHgBdcOdCdrzz4KQSq.png?st=2022-12-15T03%3A00%3A30Z&se=2022-12-15T05%3A00%3A30Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-15T00%3A42%3A20Z&ske=2022-12-16T00%3A42%3A20Z&sks=b&skv=2021-08-06&sig=SF5SuBVj2a4Ie08kV9equP9u5wSAMx9jXOhGnZKBlu4%3D",
    "transcribed_text": " I'd like an image of a fire avatar destroying someone."
}