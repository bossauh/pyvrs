import asyncio
from typing import Callable

import nest_asyncio
from pyaudio_mixer import InputTrack

from advanced_vrs import vrs

nest_asyncio.apply()


async def main() -> None:
    async def callback(result: vrs.Result, followup: bool = False, callback: Callable = None) -> None:
        print(result)

    input_track = InputTrack("Microphone", sounddevice_parameters={
        "samplerate": 16000,
        "channels": 1,
        "dtype": "int16",
    })
    vad = vrs.VAD("data/vad.h5")
    recognizer = vrs.VRS(
        vad,
        "data/vosk",
        input_track,
        ["jarvis"],
        callback,
        asyncio.get_event_loop(),
        "data/temp_speech.wav"
    )

    await recognizer.start()
    await asyncio.sleep(10000)


if __name__ == "__main__":
    asyncio.run(main())
