import openai
import whisper
import os
openai.api_key = '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' #my key
def find_keywords(sentence):
    response = openai.Completion.create(
      model="text-davinci-002",
    prompt = f'Summarize the given sentence.\nsentence: {sentence}\nsummarized sentence:',
      temperature=0,
      max_tokens=30,
      frequency_penalty=0,
      presence_penalty=0,
    )
    for i in response.choices:
        print(i.text)
    text = response.choices[0].text
    return text
def extract_important(sentence):
    response = openai.Completion.create(
      model="text-davinci-002",
    prompt = f'extract the image description from sentence \n sentence:{sentence}\nimage description:',
      temperature=0,
      max_tokens=50,
      frequency_penalty=0,
      presence_penalty=0,
    )
    for i in response.choices:
        print(i.text)
    text = response.choices[0].text
    return text


def generate_camera_description(sentence):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt = 'given the image description, generate the following\n1 camera name\n2 Lens\n3 type of shot\n4 iso settings\n5 light\nimage quality\nsentence:{}\nsettings',
#    prompt = f'given the image description, generate iso settings in numeric formfor the perfect image\n sentence: Generate an image of a nurse\n iso settings: ISO 100, aperture 5.6, shutter speed 1/125 sec.\nsentence:{sentence}\iso settings:',
      temperature=0.7,
      max_tokens=50,
      frequency_penalty=0,
      presence_penalty=0,
      n=1,
    )
    for i in response.choices:
        print(i.text)
    text = response.choices[0].text
    return text

def get_dalle_prompt(whisper_output):
  image_description = extract_important(whisper_output)
  index = 0
  while True:
    camera_options = generate_camera_description(image_description)
    for i in range(len(camera_options)):
      if camera_options[i][0]=='1':
        index=i
        break
    camera_options = camera_options[index:]

    camera_options = camera_options.lstrip()
    camera_options = camera_options.split('\n')
    output = image_description
    flag = True
    for i in camera_options:
      line = i.split('.',1)
      if len(line)!=2:
        line = i.split(':',1)
        if len(line)!=2:
          flag = False
          break
      output+=f',{line[-1]}'
    if flag:
      break
  print(output)
  return output

def generate_dalle_image(description):
  img_response=openai.Image.create(prompt = description,n=1,size="512x512")
  print(img_response)
  return img_response['data'][0]['url']

def detect_language(audio,model):
  mel = whisper.log_mel_spectrogram(audio).to(model.device)
  # detect the spoken language
  _, probs = model.detect_language(mel)
  print(f"Detected language: {max(probs, key=probs.get)}")
  return max(probs, key=probs.get)
def transcribe_audio(model,audio_path):
  audio = whisper.load_audio(audio_path)
  audio = whisper.pad_or_trim(audio)
  mel = whisper.log_mel_spectrogram(audio).to(model.device)

  # detect the spoken language
  _, probs = model.detect_language(mel)
  print(f"Detected language: {max(probs, key=probs.get)}")
  language =max(probs, key=probs.get)
  options = dict(language=language, beam_size=5, best_of=5)
  transcribe_options = dict(task="transcribe", **options)
  translate_options = dict(task="translate", **options)
  transcription = model.transcribe(audio, **transcribe_options,fp16 = False)["text"]
  translation = model.transcribe(audio, **translate_options,fp16 = False)["text"]
  print(transcription)
  print(translation)
  return translation
  #detect_language('temp.wav',base_model)
  result = model.transcribe(audio_path)
  print(result)
  print(result['text'])
  return result['text']
