import imageio
import os
import cv2

from src.constants import FRAME_DIR
from src.constants import RESULT_DIR


class FrameCollector:
    def __init__(self):
        pass
    def get_frame(self, input_path):
        self.input_path = input_path
        for filename in os.listdir(input_path):
            if filename.endswith('.mp4'):
                video_path = os.path.join(input_path, filename)
                video_id = filename.split(".")[0]
                output_path = os.path.join(RESULT_DIR, FRAME_DIR)
                self.get_frames_every_x_seconds(video_id, video_path, 1, output_dir=output_path, save=True)
    def get_frames_every_x_seconds(self, video_id, video_path, interval_seconds=2, output_dir=os.path.join(RESULT_DIR, FRAME_DIR), use_opencv=True, save=True):
        """
        Extracts frames from a video at a specified interval.

        Args:
            video_path (str): Path to the input video file.
            interval_seconds (int, optional): Interval in seconds between frames. Defaults to 2.
            output_dir (str, optional): Path to the directory for saving the JPEG images. Defaults to FRAME_DIR in RESULT_DIR.
            use_opencv (bool, optional): Whether to use OpenCV (True) or imageio (False) for extraction. Defaults to True.
            save (bool, optional): Save frames form extraction or no. Defaults to True.

        Returns:
            bool: True if successful, False otherwise.
        """
        if interval_seconds <= 0:
            print("Error: Interval must be a positive number.")
            return False

        cap = cv2.VideoCapture(
            video_path) if use_opencv else imageio.get_reader(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS) if use_opencv else cap.get_meta_data()[
            'fps']

        if not cap.isOpened():
            print("Error opening video file")
            return False

        duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / \
            fps if use_opencv else cap.get_meta_data()['duration']
        timestamps = [
            i * interval_seconds for i in range(int(duration // interval_seconds))]

        if use_opencv:
            return self.get_frames_at_timestamps_opencv(video_id, video_path, timestamps, output_dir=output_dir, save=save)
        else:
            return self.get_frames_at_timestamps(video_id, video_path, timestamps, use_opencv=False, output_dir=output_dir, save=save)

    def get_frames_at_timestamps(self, video_id, video_path, timestamps, use_opencv=True, output_dir=os.path.join(RESULT_DIR, FRAME_DIR), save=True):
        """
        Extracts frames from a video at the specified timestamps.

        Args:
            video_path (str): Path to the input video file.
            timestamps (list): List of timestamps in seconds to extract frames at.
            output_dir (str): Path to the directory for saving the JPEG images.
            save (bool, optional): Save frames form extraction or no. Defaults to True.

        Returns:
            None
        """
        frames = []

        if save:
            self.__create_output_dir(output_dir)

        if use_opencv:
            return self.get_frames_at_timestamps_opencv(
                video_path, timestamps, output_dir, save=save)

        reader = imageio.get_reader(video_path)
        fps = reader.get_meta_data()['fps']
        duration = reader.get_meta_data()['duration']
        for timestamp in timestamps:
            if timestamp > duration:
                print(f"Error {timestamp} because duration = {duration}.")
                return False
        # Calculate frame numbers for each timestamp
        frame_numbers = [(timestamp * fps) for timestamp in timestamps]

        # Retrieve frames with error handling
        for frame_number in frame_numbers:
            try:
                frame = reader.get_data(frame_number)

                if save:
                    output_path = f"{output_dir}/{video_id}_frame_{frame_number:.2f}.jpg"
                    imageio.imwrite(output_path, frame)
                else:
                    frames.append(frame)
            except IndexError:
                print(f"Frame at timestamp {timestamp} not found. Skipping.")

        reader.close()

        if save:
            return True
        
        return frames

    def get_frames_at_timestamps_opencv(self, video_id, video_path, timestamps, output_dir, save=True):
        """
        Extracts frames from a video at specific durations and saves them to a directory.

        Args:
            video_path: The path to the video file.
            output_dir: The directory to save the frames.
            timestamps: A list of timestamps at which to extract frames.
            save (bool, optional): Save frames form extraction or no. Defaults to True.

        """
        frames = []

        if save:
            self.__create_output_dir(output_dir)
        
        cap = cv2.VideoCapture(video_path)

        # Check if the video capture was successful
        if not cap.isOpened():
            print("Error opening video file")
            return False

        # Get video FPS
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Extract frames at specified timestamps
        for i, timestamp in enumerate(timestamps):
            frame_index = timestamp * fps

            # Set frame position
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_index))

            ret, frame = cap.read()
            if ret:
                if save:
                    output_path = f"{output_dir}/{video_id}_frame_{frame_index:.2f}.jpg"
                    cv2.imwrite(output_path, frame)
                else:
                    frames.append(frame)
            else:
                print(f"Error extracting frame at {timestamp} seconds")

        cap.release()
        if save:
            return True

        return frames
    
    def __create_output_dir(self, output_dir):
        try:
            os.makedirs(output_dir)
        except OSError as e:
            if os.path.isdir(output_dir):
                print(f"Folder '{output_dir}' already exists.")
            else:
                print(f"Error creating folder: {e}")