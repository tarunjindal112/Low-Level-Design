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


class ExportFactory(ABC):
    """
    Factory that represents a combination of video and audio codec.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video recorder instance"""

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio recorder instance"""


class FastExporter(ExportFactory):
    """Factory aimed at providing the high speed, lower quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExportFactory):
    """Factory aimed at providing the slower speed, high quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422VideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExportFactory):
    """Factory aimed at providing the slower speed, master quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExportFactory:
    """Constructs an exporter factory based on the user's preference."""
    factories  = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }

    while True:
        export_quality = input("Enter desired output quality (low, high, master):")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main(fac: ExportFactory):
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


fac = read_exporter()
main(fac)

