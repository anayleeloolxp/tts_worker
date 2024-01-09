import subprocess
import base64
import os
import runpod

def tts_handler(job):
    job_input = job["input"]
    text = job_input.get("text")

    if not text:
        return {"error": "No text provided"}

    output_path = "output.wav"
    try:
        command = ["tts", "--text", text, "--out_path", output_path]
        subprocess.run(command, check=True)

        with open(output_path, "rb") as audio_file:
            encoded_audio = base64.b64encode(audio_file.read()).decode('utf-8')

        # Delete the file after use
        os.remove(output_path)

        return {"audio": encoded_audio}
    except subprocess.CalledProcessError:
        return {"error": "TTS synthesis failed"}
    except Exception as e:
        return {"error": str(e)}

# Start the RunPod serverless function
runpod.serverless.start({"handler": tts_handler})
