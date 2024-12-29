import cv2
import os
import math

def extract_frames(video_path, output_dir, num_frames=50):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames < num_frames:
        print("Warning: The video has fewer frames than the requested number of frames to extract.")
        num_frames = total_frames

    print(f"Total frames in video: {total_frames}")

    extracted_count = 0

    for i in range(num_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = cap.read()

        if not success:
            print(f"Error: Could not read frame at index {i}")
            break

        frame_filename = os.path.join(output_dir, f"frame_{extracted_count + 1:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        extracted_count += 1

        print(f"Extracted frame {i} to {frame_filename}")

    cap.release()
    print(f"Extracted {extracted_count} frames in total.")

# Example usage
video_file = "C:\\Users\\sindh\\Downloads\\assist\\VID20230626205037.mp4"  
output_directory = "extracted_frames_for_my_video"  # Directory to save extracted frames
extract_frames(video_file, output_directory, num_frames=100)
