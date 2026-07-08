import io
import time
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from detector import detect_objects
from annotation import draw_annotations
from image_info import get_image_info
from report import (
    create_detection_report, convert_to_csv, generate_pdf_report
)
from object_counter import count_objects
import os
st.set_page_config(page_title="AI Smart Image Annotation System")
# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Page Configuration
st.set_page_config(page_title="Smart Image Annotation System")

# Title
st.title("🖼️  Smart Image Annotation System")
st.caption("Detect and annotate multiple objects in images using the YOLOv8s deep learning model.")
st.divider()

# Sidebar
st.sidebar.title("📌 Project Information")

st.sidebar.markdown("""
### Smart Image Annotation System

**Model:** YOLOv8s

**Framework:** Streamlit

**Language:** Python

**Purpose:**
Detect and annotate objects in images using Artificial Intelligence.

**Developer:** Harman Kaur

**Summer Training:** 2026
""")
# Confidence Threshold Slider

confidence_threshold = st.sidebar.slider(
    "🎯 Confidence Threshold",
    min_value=0.0,
    max_value=1.0,
    value=0.50,
    step=0.05
)
#About Project
with st.expander("ℹ️ About This Project"):
    st.write("""
This application uses the YOLOv8s deep learning model to detect and annotate objects in images.

### Features
- Upload JPG, JPEG, or PNG images
- Detect multiple object classes
- Display confidence scores
- Detection statistics
- Object details table
- Download annotated image
- Processing time measurement
""")

st.info("📤 Upload a JPG, JPEG, or PNG image and click **Detect Objects** to begin.")

# Upload Image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    info = get_image_info(image, uploaded_file)
    
    st.subheader("🖼 Image Information")

    col1, col2 = st.columns(2)

    with col1:
      st.write(f"**Width:** {info['width']} px")
      st.write(f"**Height:** {info['height']} px")
      st.write(f"**Format:** {info['format']}")

    with col2:
      st.write(f"**Color Mode:** {info['mode']}")
      st.write(f"**File Size:** {info['size']:.2f} KB")
    # Create two columns for images
    image_col1, image_col2 = st.columns(2)

    with image_col1:
     st.subheader("🖼 Original Image")
     st.image(image, use_container_width=True)

    # Detect Button
    if st.button("Detect Objects"):
        with st.spinner("Detecting objects..."):
            start_time = time.time()

            # Run YOLO
            results = detect_objects(image, confidence_threshold)
            result = results[0]

            boxes = result.boxes
            names = result.names

            # Draw Bounding Boxes
            annotated_image = draw_annotations(image, result)
            
            # ----------------------------
            # Detection Statistics
            # ----------------------------
            object_names = []

            for i in range(len(boxes)):
                class_id = int(boxes.cls[i])
                object_names.append(names[class_id].title())

            unique_objects = sorted(set(object_names))
            object_counts = count_objects(object_names)
            # ----------------------------
            # Detection Summary
            # ----------------------------
            st.subheader("📋 Detection Summary")

            col1, col2 = st.columns(2)

            with col1:
              st.metric("Total Objects", len(boxes))

            with col2:
             st.metric("Unique Classes", len(unique_objects))

            st.subheader("📊 Detection Statistics")

            st.write(f"**Total Objects:** {len(boxes)}")
            st.write(f"**Unique Object Types:** {len(unique_objects)}")

            st.write("**Detected Classes:**")
            for obj in unique_objects:
                st.write(f"• {obj}")
            st.subheader("📦 Object Counts")

            for obj, count in object_counts.items():
                st.write(f"**{obj}:** {count}")
            # ----------------------------
            # Object Details Table
            # ----------------------------
            st.divider()
            st.subheader("Detected Object Details")

            data = []

            for i in range(len(boxes)):
                class_id = int(boxes.cls[i])
                confidence = float(boxes.conf[i])

                data.append({
                    "No.": i + 1,
                    "Object": names[class_id].title(),
                    "Confidence": f"{confidence:.2%}"
                })

            df = create_detection_report(data)
            st.table(df)
            
            # Save CSV in outputs folder
            
            df.to_csv("outputs/detection_report.csv", index=False)
            csv = convert_to_csv(df)
            st.download_button(
             label="📄 Download Detection Report (CSV)",
             data=csv,
             file_name="detection_report.csv",
             mime="text/csv"
            )

            with image_col2:
             st.subheader("🎯 Detected Image")
             st.image(annotated_image, use_container_width=True)
            # Convert NumPy array to PIL Image
            annotated_pil = Image.fromarray(annotated_image)

            # Save annotated image to outputs folder
            annotated_pil.save("outputs/annotated_image.png")

            # Save image in memory so the download button has actual bytes
            buffer = io.BytesIO()
            annotated_pil.save(buffer, format="PNG")
            buffer.seek(0)

            # Download Button
            st.download_button(
                label="📥 Download Annotated Image",
                data=buffer.getvalue(),
                file_name="annotated_image.png",
                mime="image/png"
            )
            # Generate PDF Report
            pdf_file = "outputs/detection_report.pdf"
            generate_pdf_report(df, pdf_file)
            # Read PDF
            with open(pdf_file, "rb") as pdf:
             PDFbyte = pdf.read()
            # Download PDF Button
            st.download_button(
            label="📑 Download Detection Report (PDF)",
            data=PDFbyte,
            file_name="detection_report.pdf",
            mime="application/pdf"
           )
            end_time = time.time()
            processing_time = end_time - start_time

            st.info(f"⏱ Processing Time: {processing_time:.2f} seconds")
            st.success("✅ Object Detection Completed Successfully!")
            st.divider()

            st.markdown(
               """
               <div style="text-align:center; color:gray; font-size:15px;">
               <b>Smart Image Annotation System</b><br>
               Developed by <b>Harman Kaur</b><br>
               Summer Training Project - 2026
              </div>
              """,
              unsafe_allow_html=True
           )