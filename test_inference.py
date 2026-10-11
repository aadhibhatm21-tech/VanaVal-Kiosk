import onnxruntime as ort
import numpy as np

print("🧠 Step 1: Loading VanaVal Edge-AI Brain...")

# Load the local model
session = ort.InferenceSession("vanaval_model.onnx")

# Inspect the model inputs
input_name = session.get_inputs()[0].name
print("✅ Success: Model loaded into local memory!")
print(f"• Input Sensor Name: {input_name}")

# Simulate a live 640x640 camera frame from the calibration tray
test_camera_frame = np.random.randn(1, 3, 640, 640).astype(np.float32)

print("\n⚡ Step 2: Running local edge inference on simulated tray...")
outputs = session.run(None, {input_name: test_camera_frame})

print(f"🎉 INFERENCE SUCCESSFUL! Output matrix shape: {outputs[0].shape}")
print("🚀 Your AI model is officially running 100% offline on your laptop!")