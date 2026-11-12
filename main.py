import cv2
import matplotlib.pyplot as plt
import numpy as np

def DisplayImage(title,image):
    plt.figure(figsize=(8,8))
    if len(image.shape)==2:
        plt.imshow(image,cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def InteractiveEdgeDetection(image_path):
    print("HELLOOO")
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    DisplayImage("Original Grayscale Image", gray_image)
    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacial Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")
    while True:
        choice = input("Please enter your choice..(1-6)")
        if choice == "1":
            sobelx=cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
            sobely=cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))
            DisplayImage("Sobel Edge Detection",combined_sobel)
        elif choice == "2":
           print("Adjust threshold for Canny (default: 100 and 200)") 
           lower = int(input("Enter lower threshold"))
           upper = int(input("Enter upper threshold"))
           edges = cv2.Canny(gray_image,lower,upper)
           DisplayImage("Canny Edge Detection",edges)    
        elif choice == "3":
            l=cv2.Laplacian(gray_image,cv2.CV_64F)
            DisplayImage("Laplacian Edge Detection",np.abs(l).astype(np.uint8))
        elif choice == "4":
            print("Adjust kernal size for Gaussian blur (it must be odd)")
            kernal_size = int(input("Enter kernal size..."))
            blurred = cv2.GaussianBlur(image,(kernal_size, kernal_size),0)
            DisplayImage("Gaussian Smoothing",blurred)
        elif choice == "5":
            print("Adjust kernal size for Median filtering (it must be odd)")
            kernal_size = int(input("Enter kernal size..."))
            median_filtered = cv2.medianBlur(image,kernal_size)
            DisplayImage("Median Filtering",median_filtered)
        elif choice == "6":
            print("Exiting..")
            break
        else:
            print("Invalid choice.. 100Please select a no between 1 to 6")
InteractiveEdgeDetection("family.jpg")