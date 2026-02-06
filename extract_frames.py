
import cv2
import os

def extract_frames(video_path, output_folder, target_fps=24, scale_width=1920):
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate hop to match target FPS roughly
    step = original_fps / target_fps
    
    current_frame = 0
    saved_count = 0
    next_save_frame = 0.0

    print(f"Processing video: {video_path}")
    print(f"Original FPS: {original_fps}, Total Frames: {frame_count}")
    print(f"Target FPS: {target_fps}, Step: {step}")

    while True:
        success, frame = cap.read()
        if not success:
            break

        if current_frame >= next_save_frame:
            # Resize preserving aspect ratio
            height, width = frame.shape[:2]
            scale_height = int(height * (scale_width / width))
            resized_frame = cv2.resize(frame, (scale_width, scale_height), interpolation=cv2.INTER_AREA)

            # Save frame with 1-based index padding
            filename = f"{saved_count + 1:04d}.jpg"
            output_path = os.path.join(output_folder, filename)
            
            # Save as JPEG with quality 85 (optimized)
            cv2.imwrite(output_path, resized_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
            
            saved_count += 1
            next_save_frame += step

        current_frame += 1

    cap.release()
    print(f"Done! Extracted {saved_count} frames to {output_folder}")

if __name__ == "__main__":
    extract_frames("images/Hero_Animation_720.mp4", "images/hero-sequence")
