
import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image

model_inputs = {
    "prompt": "dreamlikeart, girl holding candle at the beach",
    "negative": "out of frame, duplicate, watermark, signature, text",
    "steps": 30,
    "scale": 7.5,
    "height": 768,
    "width": 512,
    "sampler": 'Euler',
    "aesthetics_fix_factor": 0,
    "prompt_strength": 0.75,
    "num_outputs": 1,

}

api_key = "205b51fa-ec6d-496f-9318-2750166c286a"
model_key = "7b08384d-4a95-4e19-8bcb-5d279cd0284f"

# Run the model
out = banana.run(api_key, model_key, model_inputs)
print(len(out['modelOutputs']))
image_byte_string = out['modelOutputs'][0]['image_base64']
image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save('output.jpg')
