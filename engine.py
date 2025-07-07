import cv2
from ultralytics import YOLO
import numpy as np 
import torch 

class CustomerSegmentationWithYolo():
    def __init__(self, erode_intensity=2, erode_size=5):
        self.model = YOLO('yolov8m-seg.pt')
        self.background_image=cv2.imread('./static/background2.jpg')
        self.erode_size = erode_size
        self.erode_intensity=erode_intensity

    def generate_mask_from_result(self, results):
        for result in results:
            if result.masks:
                # Get teh array results
                masks=result.masks.data
                boxes=result.boxes.data

                # Extract classes 
                clss = boxes[:, 5]

                # Get the incides of results where class is 0 (people in COCO)
                people_indices = torch.where(clss==0)

                ## Use these indices to extract the relevant masks
                people_masks = masks[people_indices]

                if len(people_masks) == 0:
                    return None
                
                ## Scale for visualizing results by getting the original frame
                people_mask = torch.any(people_masks, dim=0).to(torch.uint8) * 255

                ## To improve the edges of prediction
                kernel=np.ones((self.erode_size, self.erode_size), np.uint8)
                eroded_mask = cv2.erode(people_mask.cpu().numpy(), kernel, iterations=self.erode_intensity)

                return eroded_mask
            else:
                return None
            
    def apply_blur_with_mask(self, frame, mask, blur_strength=21):
        blur_strength=(blur_strength, blur_strength)
        blurred_frame=cv2.GaussianBlur(frame, blur_strength, 0)

        # Ensure that the mask is binary
        mask = (mask > 0).astype(np.uint8)

        # Expand mask to 3 channels
        mask_3d = cv2.merge([mask, mask, mask])

        # combine blurred and original frame
        result_frame = np.where(mask_3d == 1, frame, blurred_frame)

        return result_frame
    
    def apply_black_background(self, frame, mask):
        # Create a black background
        black_background=np.zero_like(frame)

        # Apply the mask
        result_frame=np.where(mask[:, :, np.newaxis] == 255, frame, black_background)
        return result_frame

    def apply_custom_background(self, frame, mask):
        # Load the background image
        background_image=cv2.resize(self.background_image, (frame.shape[1], frame.shape[0]))

        # Apply the mask
        result_frame=np.where(mask[:, :, np.newaxis] == 255, frame, background_image)
        return result_frame

