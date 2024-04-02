"""
Basic Video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic example of Video Exporting Codec"""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares Video Data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export The video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}")


class H264Hi422VideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)"""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}")


class AudioExporter(ABC):
    """Basic Representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares audio Data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec"""

    def prepare_export(self, video_data):
        print("Preparing audio data for AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}")


class WAVAudioExporter(AudioExporter):
    """WAV audio exporting codec"""

    def prepare_export(self, video_data):
        print("Preparing audio data for WAV export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}")


export_quality: str
while True:
    export_quality = input("Enter desired output quality (low, high, master):")
    if export_quality in ("low", "high", "master"):
        break
    print(f"Unknown output quality option: {export_quality}.")

video_exporter: VideoExporter
audio_exporter: AudioExporter

if export_quality == "low":
    video_exporter = H264BPVideoExporter()
    audio_exporter = AACAudioExporter()
elif export_quality == "high":
    video_exporter = H264Hi422VideoExporter()
    audio_exporter = AACAudioExporter()
else:
    video_exporter = LosslessVideoExporter()
    audio_exporter = WAVAudioExporter()

video_exporter.prepare_export("placeholder_for_video_data")
audio_exporter.prepare_export("placeholder_for_audio_data")

folder = pathlib.Path("/usr/tmp/video")
video_exporter.do_export(folder)
audio_exporter.do_export(folder)

